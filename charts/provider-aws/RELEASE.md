# [gardener-extension-provider-aws]
## ⚠️ Breaking Changes
* *[USER]* The `gp2` StorageClass is now removed. ([gardener/gardener-extension-provider-aws#576](https://github.com/gardener/gardener-extension-provider-aws/pull/576), [@StenlyTU](https://github.com/StenlyTU))
* *[OPERATOR]* This version of provider-aws requires Gardener v1.50.0. ([gardener/gardener-extension-provider-aws#562](https://github.com/gardener/gardener-extension-provider-aws/pull/562), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* This version of provider-aws requires Gardener v1.50+. ([gardener/gardener-extension-provider-aws#571](https://github.com/gardener/gardener-extension-provider-aws/pull/571), [@kris94](https://github.com/kris94))
## ✨ New Features
* *[OPERATOR]* `CloudProfileConfig` now supports a new field `.machineImages[].versions[].regions[].architecture`. It specifies the supported CPU architecture of the given machine image AMI. ([gardener/gardener-extension-provider-aws#565](https://github.com/gardener/gardener-extension-provider-aws/pull/565), [@acumino](https://github.com/acumino))
* *[OPERATOR]* `WorkerStatus` now supports a new field `.machineImage[].architecture`. It specifies the supported CPU architecture of the given worker pool. ([gardener/gardener-extension-provider-aws#565](https://github.com/gardener/gardener-extension-provider-aws/pull/565), [@acumino](https://github.com/acumino))
## 🐛 Bug Fixes
* *[USER]* Users can now set IOPS for a GP3 volume type. Validation of IOPS (i.e. whether it is allowed and is in the specified range for a volume type) is done on the AWS side, so feedback will arrive once the volume is created. ([gardener/gardener-extension-provider-aws#561](https://github.com/gardener/gardener-extension-provider-aws/pull/561), [@rishabh-11](https://github.com/rishabh-11))
* *[OPERATOR]* provider-aws now mutates the `cluster-autoscaler` Deployment by implementing the `EnsureClusterAutoscalerDeployment` function. This is required in the context of https://github.com/kubernetes/autoscaler/issues/4517 - cluster-autoscaler supports `--feature-gates` flag and provider extensions have to mutate the cluster-autoscaler Deployment to add the CSI related feature gates to it. ([gardener/gardener-extension-provider-aws#562](https://github.com/gardener/gardener-extension-provider-aws/pull/562), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[USER]* The following images are updated: ([gardener/gardener-extension-provider-aws#540](https://github.com/gardener/gardener-extension-provider-aws/pull/540), [@acumino](https://github.com/acumino))
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.2 -> v2.2.2 (for kubernetes < 1.20)
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.2 -> v3.2.0 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-attacher: v3.3.0 -> v3.4.0
  * k8s.gcr.io/sig-storage/csi-resizer: v0.5.0 -> v1.5.0
  * k8s.gcr.io/sig-storage/csi-snapshotter: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-validation-webhook: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-controller: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-node-driver-registrar: v1.3.0 -> v2.5.1
  * k8s.gcr.io/sig-storage/livenessprobe: v2.3.0 -> v2.7.0
* *[USER]* The following image is updated: ([gardener/gardener-extension-provider-aws#574](https://github.com/gardener/gardener-extension-provider-aws/pull/574), [@ialidzhikov](https://github.com/ialidzhikov))
  * k8s.gcr.io/provider-aws/aws-ebs-csi-driver: v1.5.3 -> v1.9.0
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-provider-aws#564](https://github.com/gardener/gardener-extension-provider-aws/pull/564), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-provider-aws#568](https://github.com/gardener/gardener-extension-provider-aws/pull/568), [@acumino](https://github.com/acumino))
  * github.com/gardener/gardener: v1.48.0 -> v1.50.0
* *[OPERATOR]* Update golang version used to 1.18 ([gardener/gardener-extension-provider-aws#569](https://github.com/gardener/gardener-extension-provider-aws/pull/569), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Update MTU-resizer alpine image ([gardener/gardener-extension-provider-aws#579](https://github.com/gardener/gardener-extension-provider-aws/pull/579), [@kon-angelo](https://github.com/kon-angelo))
# [aws-lb-readvertiser]
## 🏃 Others
* *[OPERATOR]* Use `go mod` instead of `dep` ([gardener/aws-lb-readvertiser#21](https://github.com/gardener/aws-lb-readvertiser/pull/21), [@kon-angelo](https://github.com/kon-angelo))
  * Update golang version used.
* *[OPERATOR]* The `aws-lb-readvertiser` now uses `distroless` instead of `alpine` as a base image. ([gardener/aws-lb-readvertiser#23](https://github.com/gardener/aws-lb-readvertiser/pull/23), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager]
## ⚠️ Breaking Changes
* *[OPERATOR]* The default leader election resource lock of `machine-controller-manager` has been changed from `endpointsleases` to `leases`. ([gardener/machine-controller-manager#711](https://github.com/gardener/machine-controller-manager/pull/711), [@acumino](https://github.com/acumino))
  * Please make sure, that you had at least `machine-controller-manager@v0.43.0` running before upgrading to `v0.46.0`, so that it has successfully acquired leadership with the hybrid resource lock (`endpointsleases`) at least once.
## 🐛 Bug Fixes
* *[USER]* Rollout freeze won't happen due to `Unknown` machines now. ([gardener/machine-controller-manager#733](https://github.com/gardener/machine-controller-manager/pull/733), [@himanshu-kun](https://github.com/himanshu-kun))
## 🏃 Others
* *[OPERATOR]* Published docker images for Machine-Controller-Manager are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/machine-controller-manager#732](https://github.com/gardener/machine-controller-manager/pull/732), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `machine-controller-manager` container now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager#734](https://github.com/gardener/machine-controller-manager/pull/734), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager-provider-aws]
## 🏃 Others
* *[OPERATOR]* machine-controller-manager-provider-aws now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager-provider-aws#90](https://github.com/gardener/machine-controller-manager-provider-aws/pull/90), [@ialidzhikov](https://github.com/ialidzhikov))
* *[DEVELOPER]* probeResources() now doesn't try to delete orphan resources but only lists them. ([gardener/machine-controller-manager-provider-aws#85](https://github.com/gardener/machine-controller-manager-provider-aws/pull/85), [@Mkmittal](https://github.com/Mkmittal))
  * The beforeSuite for IT test now calls for cleanup of orphan resources separately.
  * The Integration Test, which looks for orphan resources, now doesn't try to delete the orphan resources and just waits for them to be done automatically.
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Terraform google provider is updated to v4.19.0 ([gardener/terraformer#119](https://github.com/gardener/terraformer/pull/119), [@bd3lage](https://github.com/bd3lage))