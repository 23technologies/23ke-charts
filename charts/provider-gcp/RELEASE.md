# [gardener-extension-provider-gcp]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-gcp requires Gardener v1.50.0. ([gardener/gardener-extension-provider-gcp#454](https://github.com/gardener/gardener-extension-provider-gcp/pull/454), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* This version of provider-gcp requires Gardener v1.50+. ([gardener/gardener-extension-provider-gcp#462](https://github.com/gardener/gardener-extension-provider-gcp/pull/462), [@kris94](https://github.com/kris94))
## ✨ New Features
* *[USER]* Users could now attach GPU to their machines in a worker pool. ([gardener/gardener-extension-provider-gcp#438](https://github.com/gardener/gardener-extension-provider-gcp/pull/438), [@himanshu-kun](https://github.com/himanshu-kun))
## 🐛 Bug Fixes
* *[OPERATOR]* Fixed an issue that caused the VPA object for `csi-driver-node` to no longer match any Pods and effectively disabled vertical autoscaling for the DaemonSet. ([gardener/gardener-extension-provider-gcp#452](https://github.com/gardener/gardener-extension-provider-gcp/pull/452), [@voelzmo](https://github.com/voelzmo))
* *[OPERATOR]* provider-gcp now mutates the `cluster-autoscaler` Deployment by implementing the `EnsureClusterAutoscalerDeployment` function. This is required in the context of https://github.com/kubernetes/autoscaler/issues/4517 - cluster-autoscaler supports `--feature-gates` flag and provider extensions have to mutate the cluster-autoscaler Deployment to add the CSI related feature gates to it. ([gardener/gardener-extension-provider-gcp#454](https://github.com/gardener/gardener-extension-provider-gcp/pull/454), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[USER]* Changing the default StorageClass for GCP shoots from pd-standard(HDD) to pd-balanced(SSD). ([gardener/gardener-extension-provider-gcp#463](https://github.com/gardener/gardener-extension-provider-gcp/pull/463), [@StenlyTU](https://github.com/StenlyTU))
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-provider-gcp#456](https://github.com/gardener/gardener-extension-provider-gcp/pull/456), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* CSI Driver version has been updated to `1.7.2-gke.2` ([gardener/gardener-extension-provider-gcp#458](https://github.com/gardener/gardener-extension-provider-gcp/pull/458), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Update go version to `v1.18` ([gardener/gardener-extension-provider-gcp#459](https://github.com/gardener/gardener-extension-provider-gcp/pull/459), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-gcp#461](https://github.com/gardener/gardener-extension-provider-gcp/pull/461), [@bd3lage](https://github.com/bd3lage))
  * github.com/gardener/gardener: v1.48.0 -> v1.50.1
* *[OPERATOR]* port 80 in external firewall rule is dropped. ([gardener/gardener-extension-provider-gcp#468](https://github.com/gardener/gardener-extension-provider-gcp/pull/468), [@DockToFuture](https://github.com/DockToFuture))
# [machine-controller-manager]
## ⚠️ Breaking Changes
* *[OPERATOR]* The default leader election resource lock of `machine-controller-manager` has been changed from `endpointsleases` to `leases`. ([gardener/machine-controller-manager#711](https://github.com/gardener/machine-controller-manager/pull/711), [@acumino](https://github.com/acumino))
  * Please make sure, that you had at least `machine-controller-manager@v0.43.0` running before upgrading to `v0.46.0`, so that it has successfully acquired leadership with the hybrid resource lock (`endpointsleases`) at least once.
## 🐛 Bug Fixes
* *[USER]* Rollout freeze won't happen due to `Unknown` machines now. ([gardener/machine-controller-manager#733](https://github.com/gardener/machine-controller-manager/pull/733), [@himanshu-kun](https://github.com/himanshu-kun))
## 🏃 Others
* *[OPERATOR]* Published docker images for Machine-Controller-Manager are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/machine-controller-manager#732](https://github.com/gardener/machine-controller-manager/pull/732), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `machine-controller-manager` container now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager#734](https://github.com/gardener/machine-controller-manager/pull/734), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager-provider-gcp]
## 🏃 Others
* *[USER]* A bug causing machine spec validation to fail has been fixed. ([gardener/machine-controller-manager-provider-gcp#53](https://github.com/gardener/machine-controller-manager-provider-gcp/pull/53), [@himanshu-kun](https://github.com/himanshu-kun))
* *[OPERATOR]* machine-controller-manager-provider-gcp now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager-provider-gcp#50](https://github.com/gardener/machine-controller-manager-provider-gcp/pull/50), [@ialidzhikov](https://github.com/ialidzhikov))
## 📰 Noteworthy
* *[USER]* VM with GPU attached can now be created on GCP. Note for a2 series machine , no need to specify `acceleratorType` and `count` as it already comes with inbuilt GPU. ([gardener/machine-controller-manager-provider-gcp#41](https://github.com/gardener/machine-controller-manager-provider-gcp/pull/41), [@himanshu-kun](https://github.com/himanshu-kun))
* *[DEVELOPER]* probeResources() now doesn't try to delete orphan resources but only lists them. ([gardener/machine-controller-manager-provider-gcp#47](https://github.com/gardener/machine-controller-manager-provider-gcp/pull/47), [@Mkmittal](https://github.com/Mkmittal))
  * The beforeSuite for IT test now calls for cleanup of orphan resources separately.
  * The Integration Test, which looks for orphan resources, now doesn't try to delete the orphan resources and just waits for them to be done automatically.
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Terraform google provider is updated to v4.19.0 ([gardener/terraformer#119](https://github.com/gardener/terraformer/pull/119), [@bd3lage](https://github.com/bd3lage))