# [gardener-extension-provider-azure]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-azure requires Gardener v1.51+. ([gardener/gardener-extension-provider-azure#529](https://github.com/gardener/gardener-extension-provider-azure/pull/529), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-provider-azure#558](https://github.com/gardener/gardener-extension-provider-azure/pull/558), [@shafeeqes](https://github.com/shafeeqes))
## ✨ New Features
* *[OPERATOR]* `CloudProfileConfig` now supports a new field `.machineImages[].machineImageVersion[].architecture`. It specifies the supported CPU architecture of the given machine image. ([gardener/gardener-extension-provider-azure#562](https://github.com/gardener/gardener-extension-provider-azure/pull/562), [@acumino](https://github.com/acumino))
* *[OPERATOR]* `WorkerStatus` now supports a new field `.machineImage[].architecture`. It specifies the supported CPU architecture of the given worker pool. ([gardener/gardener-extension-provider-azure#562](https://github.com/gardener/gardener-extension-provider-azure/pull/562), [@acumino](https://github.com/acumino))
* *[OPERATOR]* support for Azure shared gallery images for workers is added ([gardener/gardener-extension-provider-azure#567](https://github.com/gardener/gardener-extension-provider-azure/pull/567), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Adjust metric name due to upgrading the kube-state-metrics component ([gardener/gardener-extension-provider-azure#529](https://github.com/gardener/gardener-extension-provider-azure/pull/529), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-azure#550](https://github.com/gardener/gardener-extension-provider-azure/pull/550), [@kon-angelo](https://github.com/kon-angelo))
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.1 -> v3.2.0
  * k8s.gcr.io/sig-storage/csi-attacher: v3.3.0 -> v3.4.0
  * k8s.gcr.io/sig-storage/csi-resizer: v1.1.0 -> v1.5.0
  * k8s.gcr.io/sig-storage/csi-snapshotter: v3.0.3 -> v4.2.1
  * k8s.gcr.io/sig-storage/snapshot-validation-webhook: v3.0.3 -> v4.2.1
  * k8s.gcr.io/sig-storage/snapshot-controller: v3.0.3 -> v4.2.1
  * k8s.gcr.io/sig-storage/csi-node-driver-registrar: v2.1.0 -> v2.5.1
  * k8s.gcr.io/sig-storage/livenessprobe: v2.3.0 -> v2.7.0
* *[OPERATOR]* The `csi-driver-node` and `cloud-node-manager` pods now have their seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-provider-azure#559](https://github.com/gardener/gardener-extension-provider-azure/pull/559), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* fix own vNet resource group name fetch in bastion creation ([gardener/gardener-extension-provider-azure#560](https://github.com/gardener/gardener-extension-provider-azure/pull/560), [@tedteng](https://github.com/tedteng))
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-azure#563](https://github.com/gardener/gardener-extension-provider-azure/pull/563), [@kon-angelo](https://github.com/kon-angelo))
  * mcr.microsoft.com/k8s/csi/azurefile-csi: v1.19.0 -> v1.20.0
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-azure#564](https://github.com/gardener/gardener-extension-provider-azure/pull/564), [@kon-angelo](https://github.com/kon-angelo))
  * mcr.microsoft.com/k8s/csi/azuredisk-csi: v1.16.0 -> v1.22.0
* *[OPERATOR]* The `gardener.cloud-fast` storage class is now deployed with `volumeBindingMode: WaitForFirstConsumer`. This change is required if stateful pods with volumes have a topology related `podAffinity` or `podAntiAffinity` defined, e.g. when Gardener creates control-planes for HA shoot clusters. ([gardener/gardener-extension-provider-azure#565](https://github.com/gardener/gardener-extension-provider-azure/pull/565), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* switch ginkgo v1 to ginkgo v2 in bastion test ([gardener/gardener-extension-provider-azure#566](https://github.com/gardener/gardener-extension-provider-azure/pull/566), [@tedteng](https://github.com/tedteng))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-provider-azure#554](https://github.com/gardener/gardener-extension-provider-azure/pull/554), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.50.1 -> v1.53.0
  * k8s.io/* : v0.24.2 -> v0.24.3
# [machine-controller-manager]
## ✨ New Features
* *[USER]* Bootstrap token replacement by MCM is now supported for Ignition userData format ([gardener/machine-controller-manager#743](https://github.com/gardener/machine-controller-manager/pull/743), [@Gerrit91](https://github.com/Gerrit91))
## 🐛 Bug Fixes
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#739](https://github.com/gardener/machine-controller-manager/pull/739), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#738](https://github.com/gardener/machine-controller-manager/pull/738), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Migrated clients to use `policy/v1` `PodDisruptionBudget` for kubernetes versions >= 1.21. `policy/v1beta1` PDB is also supported but for k8s < 1.21 ([gardener/machine-controller-manager#744](https://github.com/gardener/machine-controller-manager/pull/744), [@shafeeqes](https://github.com/shafeeqes))
# [machine-controller-manager-provider-azure]
## 🏃 Others
* *[USER]* Updates deployment YAML used in IT when controllers are run as containers in the cluster. ([gardener/machine-controller-manager-provider-azure#70](https://github.com/gardener/machine-controller-manager-provider-azure/pull/70), [@rishabh-11](https://github.com/rishabh-11))
* *[USER]* Machine-Controller-Manager Provider-Azure now supports managing virtual machines based on shared image gallery images. ([gardener/machine-controller-manager-provider-azure#73](https://github.com/gardener/machine-controller-manager-provider-azure/pull/73), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* An issue that let the safety controller block the machine deletion if the Azure resource group is not available has been fixed. ([gardener/machine-controller-manager-provider-azure#72](https://github.com/gardener/machine-controller-manager-provider-azure/pull/72), [@dkistner](https://github.com/dkistner))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* The golang base image is now updated to 1.16.15. The alpine base image is updated to 3.16.2. ([gardener/terraformer#125](https://github.com/gardener/terraformer/pull/125), [@kon-angelo](https://github.com/kon-angelo))