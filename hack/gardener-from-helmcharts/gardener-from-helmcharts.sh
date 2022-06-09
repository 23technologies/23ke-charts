#!/usr/bin/env bash

# Prerequisites:
# * A kubernetes cluster
# * A domain name and valid certificates

source config.env

# get the service-ip-range in the cluster as described here:
# https://stackoverflow.com/a/61685899
SVCRANGE=$(echo '{"apiVersion":"v1","kind":"Service","metadata":{"name":"tst"},"spec":{"clusterIP":"1.1.1.1","ports":[{"port":443}]}}' | kubectl apply -f - 2>&1 | sed 's/.*valid IPs is //')

# now set the clusterIP for the gardener API service by selecting a random ip-adress from the
# service CIDR
# see also: https://stackoverflow.com/a/31412705
export GARDENER_API_SERVICE_CLUSTER_IP=$(nmap -sL -n $SVCRANGE | awk '/Nmap scan report/{print $NF}' | sed -n 258p)

function helm_upgrade () {
    name=$1
    repo=$2
    namespace=$3
		valuesdir=$4
    varargin=${@:5}
    helm upgrade -i $name $repo/$name \
    --namespace $namespace \
    --create-namespace \
    -f <(cat $valuesdir/base-values.yaml | envsubst) \
    -f <(cat $valuesdir/values.yaml | envsubst) \
    $varargin
}

# add helm repositories and update
helm repo add jetstack https://charts.jetstack.io
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update


# create a namespace called garden
kubectl create ns garden

# install cert-manager
helm_upgrade cert-manager jetstack cert-manager --wait

# deploy clusterissuers
kubectl apply -f letsencrypt.yaml --wait

# if you don't have an ingress already...
helm_upgrade ingress-nginx ingress-nginx ingress-nginx --wait

# create the cas and certificates
kubectl apply -f <(cat cert-manager-ca.yaml | envsubst) -n garden --wait


# now we fetch the secrets from the cluster and save it to environment variables
# These will be substituted in the values.yaml by envsubst
function get_secrets(){
    sec_name=$1
    VAR_CA_CRT=${sec_name//-/_}
    VAR_CA_CRT=${VAR_CA_CRT~~}_CA_CRT
    VAR_TLS_CRT=${sec_name//-/_}
    VAR_TLS_CRT=${VAR_TLS_CRT~~}_TLS_CRT
    VAR_TLS_KEY=${sec_name//-/_}
    VAR_TLS_KEY=${VAR_TLS_KEY~~}_TLS_KEY

    local IFS=$newline

    # first get the secrets
    local ca_crt=$(kubectl get secret -n garden $sec_name -o go-template='{{ index .data "ca.crt" | base64decode }}')
    local tls_crt=$(kubectl get secret -n garden $sec_name -o go-template='{{ index .data "tls.crt" | base64decode }}')
    local tls_key=$(kubectl get secret -n garden $sec_name -o go-template='{{ index .data "tls.key" | base64decode }}')

    # replace all newlines with \n
    ca_crt=\"${ca_crt//$'\n'/\\n}\"
    tls_crt=\"${tls_crt//$'\n'/\\n}\"
    tls_key=\"${tls_key//$'\n'/\\n}\"

    # set the actual variables
    export $VAR_CA_CRT=$ca_crt
    export $VAR_TLS_CRT=$tls_crt
    export $VAR_TLS_KEY=$tls_key
}

SECRETS=("etcd-client-tls"
"etcd-tls"
"gardener-admission-controller-tls"
"gardener-apiserver-tls"
"gardener-ca-keypair"
"kube-admin-tls"
"kube-aggregator-tls"
"kube-apiserver-tls"
"kube-controllermanager-tls"
"kube-serviceaccount-tls")

# This will result in exportert variables in the form:
# SECRET_CA_CRT, SECRET_TLS_CRT, SECRET_TLS_KEY
for sec in ${SECRETS[@]}
do
    while [[ ! $(kubectl get secret -n garden $sec) ]]
    do
	sleep 1
    done
	get_secrets $sec
done

###############################################################################
#                       Install garden-etcd and identity                      #
###############################################################################

# install garden-etc and identity
helm_upgrade garden-etcd ../../charts/ garden garden-etcd --wait
helm_upgrade identity ../../charts garden identity --wait

# create a namespace called flux-system
kubectl create ns flux-system

###############################################################################
#                        Install garden-kube-apiserver                        #
###############################################################################

# now install the garden-kube-apiserver
helm_upgrade garden-kube-apiserver ../../charts/ garden garden-kube-apiserver --wait

# fetch the apiserver kubeconfig
kubectl get secret garden-kubeconfig-for-admin -n garden -o go-template='{{ .data.kubeconfig | base64decode }}' > apiserver-in-shoot-kubeconfig.yaml

###############################################################################
#                        Install gardener-controlplane                        #
###############################################################################

# fetch the gardener-internal-kubeconfig secret first
export GARDENER_INTERNAL_KUBECONFIG=$(kubectl get secret gardener-internal-kubeconfig -n flux-system -o go-template='{{ .data.value | base64decode }}')
GARDENER_INTERNAL_KUBECONFIG=\"${GARDENER_INTERNAL_KUBECONFIG//$'\n'/\\n}\"

# install gardener-controlplane-{application,runtime} and gardener-dashboard
helm_upgrade gardener-controlplane ../../charts/ garden gardener-controlplane-application --kubeconfig apiserver-in-shoot-kubeconfig.yaml

###############################################################################
#                    install gardener-controlplane-runtime                    #
###############################################################################

helm_upgrade gardener-controlplane ../../charts garden gardener-controlplane-runtime --wait

###############################################################################
#                          install gardener dashboard                         #
###############################################################################
helm_upgrade gardener-dashboard ../../charts garden gardener-dashboard --wait
