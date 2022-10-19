# [gardener-extension-provider-openstack]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-openstack requires Gardener v1.51+. ([gardener/gardener-extension-provider-openstack#467](https://github.com/gardener/gardener-extension-provider-openstack/pull/467), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-provider-openstack#485](https://github.com/gardener/gardener-extension-provider-openstack/pull/485), [@shafeeqes](https://github.com/shafeeqes))
* *[OPERATOR]* provider-openstack no longer supports Shoots with Кubernetes version < 1.17. ([gardener/gardener-extension-provider-openstack#496](https://github.com/gardener/gardener-extension-provider-openstack/pull/496), [@dimitar-kostadinov](https://github.com/dimitar-kostadinov))
## ✨ New Features
* *[USER]* The openstack extension does now support shoot clusters with Kubernetes version 1.25. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md) before upgrading to 1.25. ([gardener/gardener-extension-provider-openstack#502](https://github.com/gardener/gardener-extension-provider-openstack/pull/502), [@shafeeqes](https://github.com/shafeeqes))
## 🐛 Bug Fixes
* *[USER]* The automatic enablement of no-overlay network configuration for new Shoots is now reverted. For more details about the motivation, see https://github.com/gardener/gardener-extension-provider-aws/issues/621. ([gardener/gardener-extension-provider-openstack#498](https://github.com/gardener/gardener-extension-provider-openstack/pull/498), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[OPERATOR]* Adjust metric name due to upgrading the kube-state-metrics component ([gardener/gardener-extension-provider-openstack#467](https://github.com/gardener/gardener-extension-provider-openstack/pull/467), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* All new calico openstack shoot clusters will be created without an overlay if not explicitly specified in the shoot spec. ([gardener/gardener-extension-provider-openstack#481](https://github.com/gardener/gardener-extension-provider-openstack/pull/481), [@DockToFuture](https://github.com/DockToFuture))
  * Vendor to gardener v1.50.1.
  * Make metrics bind address configurable
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-openstack#484](https://github.com/gardener/gardener-extension-provider-openstack/pull/484), [@ary1992](https://github.com/ary1992))
  * github.com/gardener/gardener: v1.50.1 -> v1.53.0
  * k8s.io/* : v0.24.2 -> v0.24.3
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-openstack#487](https://github.com/gardener/gardener-extension-provider-openstack/pull/487), [@MartinWeindel](https://github.com/MartinWeindel))
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.0.4 -> v3.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-attacher: v3.3.0 -> v3.5.0
  * k8s.gcr.io/sig-storage/csi-resizer: v0.5.0 -> v1.5.0
  * k8s.gcr.io/sig-storage/csi-snapshotter: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-validation-webhook: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-controller: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-node-driver-registrar: v2.0.1 -> v2.5.1
  * k8s.gcr.io/sig-storage/livenessprobe: v2.3.0 -> v2.7.0
* *[OPERATOR]* The `gardener.cloud-fast` storage class is now deployed with `volumeBindingMode: WaitForFirstConsumer`. This change is required if stateful pods with volumes have a topology related `podAffinity` or `podAntiAffinity` defined, e.g. when Gardener creates control-planes for HA shoot clusters. ([gardener/gardener-extension-provider-openstack#490](https://github.com/gardener/gardener-extension-provider-openstack/pull/490), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `csi-driver-node` daemonset now has its seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-provider-openstack#493](https://github.com/gardener/gardener-extension-provider-openstack/pull/493), [@AleksandarSavchev](https://github.com/AleksandarSavchev))
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-openstack#501](https://github.com/gardener/gardener-extension-provider-openstack/pull/501), [@dimitar-kostadinov](https://github.com/dimitar-kostadinov))
  * k8scloudprovider/openstack-cloud-controller-manager: v1.24.2 -> v1.24.3
* *[OPERATOR]* Update go version `v1.18.3` -> `v1.19.2` ([gardener/gardener-extension-provider-openstack#503](https://github.com/gardener/gardener-extension-provider-openstack/pull/503), [@kon-angelo](https://github.com/kon-angelo))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-provider-openstack#495](https://github.com/gardener/gardener-extension-provider-openstack/pull/495), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.53.0 -> v1.56.0
  * k8s.io/* : v0.24.3 -> v0.25.0
  * sigs.k8s.io/controller-runtime: v0.12.1 -> v0.13.0
# [machine-controller-manager]
## ✨ New Features
* *[USER]* Bootstrap token replacement by MCM is now supported for Ignition userData format ([gardener/machine-controller-manager#743](https://github.com/gardener/machine-controller-manager/pull/743), [@Gerrit91](https://github.com/Gerrit91))
## 🐛 Bug Fixes
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#739](https://github.com/gardener/machine-controller-manager/pull/739), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#738](https://github.com/gardener/machine-controller-manager/pull/738), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Migrated clients to use `policy/v1` `PodDisruptionBudget` for kubernetes versions >= 1.21. `policy/v1beta1` PDB is also supported but for k8s < 1.21 ([gardener/machine-controller-manager#744](https://github.com/gardener/machine-controller-manager/pull/744), [@shafeeqes](https://github.com/shafeeqes))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* The golang base image is now updated to 1.16.15. The alpine base image is updated to 3.16.2. ([gardener/terraformer#125](https://github.com/gardener/terraformer/pull/125), [@kon-angelo](https://github.com/kon-angelo))