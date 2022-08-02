# [gardener-extension-provider-azure]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-azure requires Gardener v1.50.0. ([gardener/gardener-extension-provider-azure#523](https://github.com/gardener/gardener-extension-provider-azure/pull/523), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* This version of provider-azure requires Gardener v1.50+. ([gardener/gardener-extension-provider-azure#533](https://github.com/gardener/gardener-extension-provider-azure/pull/533), [@kris94](https://github.com/kris94))
## ✨ New Features
* *[USER]* Add bastion support for multi-subnet deployments ([gardener/gardener-extension-provider-azure#518](https://github.com/gardener/gardener-extension-provider-azure/pull/518), [@kon-angelo](https://github.com/kon-angelo))
## 🐛 Bug Fixes
* *[USER]* An issue causing Shoot creation to fail for K8s >= 1.23 clusters with `spec.kubenetes.allowPrivilegedContainers=false` is now fixed. ([gardener/gardener-extension-provider-azure#521](https://github.com/gardener/gardener-extension-provider-azure/pull/521), [@ialidzhikov](https://github.com/ialidzhikov))
* *[USER]* The following images are updated: ([gardener/gardener-extension-provider-azure#522](https://github.com/gardener/gardener-extension-provider-azure/pull/522), [@ialidzhikov](https://github.com/ialidzhikov))
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-controller-manager: v1.23.2 -> v1.23.13
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-node-manager: v1.23.2 -> v1.23.13
* *[USER]* An issue preventing azure CCM to create routes for K8s < 1.21 Shoot clusters is now fixed. ([gardener/gardener-extension-provider-azure#544](https://github.com/gardener/gardener-extension-provider-azure/pull/544), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* provider-azure now mutates the `cluster-autoscaler` Deployment by implementing the `EnsureClusterAutoscalerDeployment` function. This is required in the context of https://github.com/kubernetes/autoscaler/issues/4517 - cluster-autoscaler supports `--feature-gates` flag and provider extensions have to mutate the cluster-autoscaler Deployment to add the CSI related feature gates to it. ([gardener/gardener-extension-provider-azure#523](https://github.com/gardener/gardener-extension-provider-azure/pull/523), [@ialidzhikov](https://github.com/ialidzhikov))
## 📖 Documentation
* *[USER]* A detailed list of Azure provider/service permissions/actions that are required to manage Azure Shoot clusters is now available [here](https://github.com/gardener/gardener-extension-provider-azure/blob/master/docs/azure-permissions.md). ([gardener/gardener-extension-provider-azure#536](https://github.com/gardener/gardener-extension-provider-azure/pull/536), [@dkistner](https://github.com/dkistner))
## 🏃 Others
* *[USER]* Changing the default StorageClass for Azure shoots from Standard_LRS(HDD) to StandardSSD_LRS(SSD) ([gardener/gardener-extension-provider-azure#535](https://github.com/gardener/gardener-extension-provider-azure/pull/535), [@StenlyTU](https://github.com/StenlyTU))
* *[OPERATOR]* Updated azurefile-csi to `v1.19.0` ([gardener/gardener-extension-provider-azure#520](https://github.com/gardener/gardener-extension-provider-azure/pull/520), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-provider-azure#526](https://github.com/gardener/gardener-extension-provider-azure/pull/526), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* add support for Azure community gallery images for workers ([gardener/gardener-extension-provider-azure#527](https://github.com/gardener/gardener-extension-provider-azure/pull/527), [@MrBatschner](https://github.com/MrBatschner))
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-azure#531](https://github.com/gardener/gardener-extension-provider-azure/pull/531), [@kon-angelo](https://github.com/kon-angelo))
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-controller-manager: v1.23.13 -> v1.23.14 (for kubernetes 1.23)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-node-manager: v1.23.13 -> v1.23.14 (for kubernetes 1.23)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-controller-manager: v1.24.0 -> v1.24.2 (for kubernetes 1.24)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-node-manager: v1.24.0 -> v1.24.2 (for kubernetes 1.24)
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-azure#537](https://github.com/gardener/gardener-extension-provider-azure/pull/537), [@acumino](https://github.com/acumino))
  * github.com/gardener/gardener: v1.48.0 -> v1.50.1
* *[OPERATOR]* Update Go version to `v1.18` ([gardener/gardener-extension-provider-azure#538](https://github.com/gardener/gardener-extension-provider-azure/pull/538), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Disable cloud-controller-manager node CIDR allocation. ([gardener/gardener-extension-provider-azure#539](https://github.com/gardener/gardener-extension-provider-azure/pull/539), [@kon-angelo](https://github.com/kon-angelo))
# [machine-controller-manager]
## ⚠️ Breaking Changes
* *[OPERATOR]* The default leader election resource lock of `machine-controller-manager` has been changed from `endpointsleases` to `leases`. ([gardener/machine-controller-manager#711](https://github.com/gardener/machine-controller-manager/pull/711), [@acumino](https://github.com/acumino))
  * Please make sure, that you had at least `machine-controller-manager@v0.43.0` running before upgrading to `v0.46.0`, so that it has successfully acquired leadership with the hybrid resource lock (`endpointsleases`) at least once.
## 🐛 Bug Fixes
* *[USER]* Rollout freeze won't happen due to `Unknown` machines now. ([gardener/machine-controller-manager#733](https://github.com/gardener/machine-controller-manager/pull/733), [@himanshu-kun](https://github.com/himanshu-kun))
## 🏃 Others
* *[OPERATOR]* Published docker images for Machine-Controller-Manager are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/machine-controller-manager#732](https://github.com/gardener/machine-controller-manager/pull/732), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `machine-controller-manager` container now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager#734](https://github.com/gardener/machine-controller-manager/pull/734), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager-provider-azure]
## 🏃 Others
* *[OPERATOR]* machine-controller-manager-provider-azure now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager-provider-azure#67](https://github.com/gardener/machine-controller-manager-provider-azure/pull/67), [@ialidzhikov](https://github.com/ialidzhikov))
* *[DEVELOPER]* probeResources() now doesn't try to delete orphan resources but only lists them. ([gardener/machine-controller-manager-provider-azure#65](https://github.com/gardener/machine-controller-manager-provider-azure/pull/65), [@Mkmittal](https://github.com/Mkmittal))
  * The beforeSuite for IT test now calls for cleanup of orphan resources separately.
  * The Integration Test, which looks for orphan resources, now doesn't try to delete the orphan resources and just waits for them to be done automatically.
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Terraform google provider is updated to v4.19.0 ([gardener/terraformer#119](https://github.com/gardener/terraformer/pull/119), [@bd3lage](https://github.com/bd3lage))