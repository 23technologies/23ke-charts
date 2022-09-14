# [gardener-extension-provider-gcp]
## ⚠️ Breaking Changes
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-provider-gcp#482](https://github.com/gardener/gardener-extension-provider-gcp/pull/482), [@shafeeqes](https://github.com/shafeeqes))
* *[OPERATOR]* This version of provider-gcp requires Gardener v1.51+. ([gardener/gardener-extension-provider-gcp#457](https://github.com/gardener/gardener-extension-provider-gcp/pull/457), [@istvanballok](https://github.com/istvanballok))
## ✨ New Features
* *[OPERATOR]* `CloudProfileConfig` now supports a new field `.machineImages[].machineImageVersion[].architecture`. It specifies the supported CPU architecture of the given machine image. ([gardener/gardener-extension-provider-gcp#477](https://github.com/gardener/gardener-extension-provider-gcp/pull/477), [@acumino](https://github.com/acumino))
* *[OPERATOR]* `WorkerStatus` now supports a new field `.machineImage[].architecture`. It specifies the supported CPU architecture of the given worker pool. ([gardener/gardener-extension-provider-gcp#477](https://github.com/gardener/gardener-extension-provider-gcp/pull/477), [@acumino](https://github.com/acumino))
## 🏃 Others
* *[OPERATOR]* The `csi-driver-node` pods now have their seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-provider-gcp#481](https://github.com/gardener/gardener-extension-provider-gcp/pull/481), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-gcp#483](https://github.com/gardener/gardener-extension-provider-gcp/pull/483), [@dimitar-kostadinov](https://github.com/dimitar-kostadinov))
  * k8s.gcr.io/cloud-provider-gcp/gcp-compute-persistent-disk-csi-driver: v1.7.2-gke.2 -> v1.7.3
* *[OPERATOR]* The `gardener.cloud-fast` storage class is now deployed with `volumeBindingMode: WaitForFirstConsumer`. This change is required if stateful pods with volumes have a topology related `podAffinity` or `podAntiAffinity` defined, e.g. when Gardener creates control-planes for HA shoot clusters. ([gardener/gardener-extension-provider-gcp#486](https://github.com/gardener/gardener-extension-provider-gcp/pull/486), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* Adjust metric name due to upgrading the kube-state-metrics component ([gardener/gardener-extension-provider-gcp#457](https://github.com/gardener/gardener-extension-provider-gcp/pull/457), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-gcp#460](https://github.com/gardener/gardener-extension-provider-gcp/pull/460), [@acumino](https://github.com/acumino))
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.2 -> v3.2.0 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-attacher: v3.3.0 -> v3.4.0
  * k8s.gcr.io/sig-storage/csi-resizer: v0.5.0 -> v1.5.0
  * k8s.gcr.io/sig-storage/csi-snapshotter: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-validation-webhook: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-controller: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-node-driver-registrar: v1.3.0 -> v2.5.1
  * k8s.gcr.io/sig-storage/livenessprobe: v2.3.0 -> v2.7.0
* *[OPERATOR]* All new calico gcp shoot clusters will be created without an overlay if not explicitly specified in the shoot spec. ([gardener/gardener-extension-provider-gcp#474](https://github.com/gardener/gardener-extension-provider-gcp/pull/474), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-gcp#479](https://github.com/gardener/gardener-extension-provider-gcp/pull/479), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.50.1 -> v1.53.0
  * k8s.io/* : v0.24.2 -> v0.24.3
# [machine-controller-manager]
## ✨ New Features
* *[USER]* Bootstrap token replacement by MCM is now supported for Ignition userData format ([gardener/machine-controller-manager#743](https://github.com/gardener/machine-controller-manager/pull/743), [@Gerrit91](https://github.com/Gerrit91))
## 🐛 Bug Fixes
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#738](https://github.com/gardener/machine-controller-manager/pull/738), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#739](https://github.com/gardener/machine-controller-manager/pull/739), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Migrated clients to use `policy/v1` `PodDisruptionBudget` for kubernetes versions >= 1.21. `policy/v1beta1` PDB is also supported but for k8s < 1.21 ([gardener/machine-controller-manager#744](https://github.com/gardener/machine-controller-manager/pull/744), [@shafeeqes](https://github.com/shafeeqes))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* The golang base image is now updated to 1.16.15. The alpine base image is updated to 3.16.2. ([gardener/terraformer#125](https://github.com/gardener/terraformer/pull/125), [@kon-angelo](https://github.com/kon-angelo))