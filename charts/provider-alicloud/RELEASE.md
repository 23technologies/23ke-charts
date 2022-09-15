# [gardener-extension-provider-alicloud]
## ⚠️ Breaking Changes
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-provider-alicloud#523](https://github.com/gardener/gardener-extension-provider-alicloud/pull/523), [@shafeeqes](https://github.com/shafeeqes))
* *[OPERATOR]* This version of provider-alicloud requires Gardener v1.50+. ([gardener/gardener-extension-provider-alicloud#507](https://github.com/gardener/gardener-extension-provider-alicloud/pull/507), [@kris94](https://github.com/kris94))
## ✨ New Features
* *[OPERATOR]* validate bastion config values fetch from InfrastructureStatus ([gardener/gardener-extension-provider-alicloud#527](https://github.com/gardener/gardener-extension-provider-alicloud/pull/527), [@tedteng](https://github.com/tedteng))
## 🏃 Others
* *[OPERATOR]* All new calico alicloud shoot clusters will be created without an overlay if not explicitly specified in the shoot spec. ([gardener/gardener-extension-provider-alicloud#518](https://github.com/gardener/gardener-extension-provider-alicloud/pull/518), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-alicloud#521](https://github.com/gardener/gardener-extension-provider-alicloud/pull/521), [@tedteng](https://github.com/tedteng))
  * github.com/gardener/gardener: v1.50.1 -> v1.53.0
* *[OPERATOR]* The `csi-driver-node` daemonset now have its seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-provider-alicloud#524](https://github.com/gardener/gardener-extension-provider-alicloud/pull/524), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* The `gardener.cloud-fast` storage class is now deployed with `volumeBindingMode: WaitForFirstConsumer`. This change is required if stateful pods with volumes have a topology related `podAffinity` or `podAntiAffinity` defined, e.g. when Gardener creates control-planes for HA shoot clusters. ([gardener/gardener-extension-provider-alicloud#528](https://github.com/gardener/gardener-extension-provider-alicloud/pull/528), [@timuthy](https://github.com/timuthy))
# [machine-controller-manager]
## ✨ New Features
* *[USER]* Bootstrap token replacement by MCM is now supported for Ignition userData format ([gardener/machine-controller-manager#743](https://github.com/gardener/machine-controller-manager/pull/743), [@Gerrit91](https://github.com/Gerrit91))
## 🐛 Bug Fixes
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#739](https://github.com/gardener/machine-controller-manager/pull/739), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* resourceName `machine-controller` added for leases in clusterrole. Updated version of Clusterroles and Clusterrolebindings to v1. ([gardener/machine-controller-manager#738](https://github.com/gardener/machine-controller-manager/pull/738), [@rishabh-11](https://github.com/rishabh-11))
## 🏃 Others
* *[OPERATOR]* Migrated clients to use `policy/v1` `PodDisruptionBudget` for kubernetes versions >= 1.21. `policy/v1beta1` PDB is also supported but for k8s < 1.21 ([gardener/machine-controller-manager#744](https://github.com/gardener/machine-controller-manager/pull/744), [@shafeeqes](https://github.com/shafeeqes))
# [machine-controller-manager-provider-alicloud]
## 🏃 Others
* *[USER]* Upgraded to mcm version 0.46.1 ([gardener/machine-controller-manager-provider-alicloud#33](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/33), [@rishabh-11](https://github.com/rishabh-11))
* *[USER]* Updated mcm dependency to v0.47.0 ([gardener/machine-controller-manager-provider-alicloud#36](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/36), [@himanshu-kun](https://github.com/himanshu-kun))
* *[DEVELOPER]* Addition of the existing integration tests in the pipeline. IT will now be run on pipeline for every PR ([gardener/machine-controller-manager-provider-alicloud#34](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/34), [@rishabh-11](https://github.com/rishabh-11))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* The golang base image is now updated to 1.16.15. The alpine base image is updated to 3.16.2. ([gardener/terraformer#125](https://github.com/gardener/terraformer/pull/125), [@kon-angelo](https://github.com/kon-angelo))