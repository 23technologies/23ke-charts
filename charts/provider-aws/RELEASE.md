# [gardener-extension-provider-aws]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-aws requires Gardener v1.51+. ([gardener/gardener-extension-provider-aws#566](https://github.com/gardener/gardener-extension-provider-aws/pull/566), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-provider-aws#587](https://github.com/gardener/gardener-extension-provider-aws/pull/587), [@shafeeqes](https://github.com/shafeeqes))
## ✨ New Features
* *[OPERATOR]* Add optional custom-route-controller ([gardener/gardener-extension-provider-aws#591](https://github.com/gardener/gardener-extension-provider-aws/pull/591), [@MartinWeindel](https://github.com/MartinWeindel))
## 🏃 Others
* *[USER]* The following image is updated: ([gardener/gardener-extension-provider-aws#594](https://github.com/gardener/gardener-extension-provider-aws/pull/594), [@kon-angelo](https://github.com/kon-angelo))
  * k8s.gcr.io/provider-aws/aws-ebs-csi-driver: v1.9.0 -> 1.11.2
* *[OPERATOR]* Adjust metric name due to upgrading the kube-state-metrics component ([gardener/gardener-extension-provider-aws#566](https://github.com/gardener/gardener-extension-provider-aws/pull/566), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-aws#585](https://github.com/gardener/gardener-extension-provider-aws/pull/585), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.50.1 -> v1.52.0
* *[OPERATOR]* All new calico aws shoot clusters with kubernetes >= 1.22 will be created without an overlay if not explicitly specified in the shoot spec. ([gardener/gardener-extension-provider-aws#589](https://github.com/gardener/gardener-extension-provider-aws/pull/589), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* The `csi-driver-node` daemonset now have its seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-provider-aws#592](https://github.com/gardener/gardener-extension-provider-aws/pull/592), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* Enable custom aws route controller per default for kubernetes >= 1.22 unless explicitly disabled. ([gardener/gardener-extension-provider-aws#596](https://github.com/gardener/gardener-extension-provider-aws/pull/596), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* The `gardener.cloud-fast` storage class is now deployed with `volumeBindingMode: WaitForFirstConsumer`. This change is required if stateful pods with volumes have a topology related `podAffinity` or `podAntiAffinity` defined, e.g. when Gardener creates control-planes for HA shoot clusters. ([gardener/gardener-extension-provider-aws#597](https://github.com/gardener/gardener-extension-provider-aws/pull/597), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* `QPS` and `Burst` are set in the HealthCheckConfig passed to the Controller. ([gardener/gardener-extension-provider-aws#598](https://github.com/gardener/gardener-extension-provider-aws/pull/598), [@shafeeqes](https://github.com/shafeeqes))
* *[OPERATOR]* The memory limits of the aws cloud-controller-manager has been removed. ([gardener/gardener-extension-provider-aws#605](https://github.com/gardener/gardener-extension-provider-aws/pull/605), [@dkistner](https://github.com/dkistner))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-provider-aws#588](https://github.com/gardener/gardener-extension-provider-aws/pull/588), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.52.0 -> v1.53.0
  * k8s.io/* : v0.24.2 -> v0.24.3
# [aws-custom-route-controller]
## 🐛 Bug Fixes
* *[OPERATOR]* Delete orphaned routes for nodes whose deletion was missed. ([gardener/aws-custom-route-controller#1](https://github.com/gardener/aws-custom-route-controller/pull/1), [@MartinWeindel](https://github.com/MartinWeindel))
# [machine-controller-manager]
## ✨ New Features
* *[USER]* Bootstrap token replacement by MCM is now supported for Ignition userData format ([gardener/machine-controller-manager#743](https://github.com/gardener/machine-controller-manager/pull/743), [@Gerrit91](https://github.com/Gerrit91))
## 🐛 Bug Fixes
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#739](https://github.com/gardener/machine-controller-manager/pull/739), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#738](https://github.com/gardener/machine-controller-manager/pull/738), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Migrated clients to use `policy/v1` `PodDisruptionBudget` for kubernetes versions >= 1.21. `policy/v1beta1` PDB is also supported but for k8s < 1.21 ([gardener/machine-controller-manager#744](https://github.com/gardener/machine-controller-manager/pull/744), [@shafeeqes](https://github.com/shafeeqes))
# [machine-controller-manager-provider-aws]
## ✨ New Features
* *[USER]* Throughput is now configurable for volume types. Its validation i.e. whether it is allowed or not for the particular volume type and is within the range, is done on the provider(AWS) side. Currently only gp3 volume have configurable throughput. ([gardener/machine-controller-manager-provider-aws#95](https://github.com/gardener/machine-controller-manager-provider-aws/pull/95), [@rishabh-11](https://github.com/rishabh-11))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* The golang base image is now updated to 1.16.15. The alpine base image is updated to 3.16.2. ([gardener/terraformer#125](https://github.com/gardener/terraformer/pull/125), [@kon-angelo](https://github.com/kon-angelo))