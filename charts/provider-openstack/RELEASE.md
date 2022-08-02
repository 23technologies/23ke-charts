# [gardener-extension-provider-openstack]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of provider-openstack requires Gardener v1.50.0. ([gardener/gardener-extension-provider-openstack#463](https://github.com/gardener/gardener-extension-provider-openstack/pull/463), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* This version of provider-openstack requires Gardener v1.50+. ([gardener/gardener-extension-provider-openstack#468](https://github.com/gardener/gardener-extension-provider-openstack/pull/468), [@kris94](https://github.com/kris94))
## 🐛 Bug Fixes
* *[USER]* An issue preventing ControlPlane resource to be successfully reconciled for K8s 1.24 Shoots is now fixed. ([gardener/gardener-extension-provider-openstack#459](https://github.com/gardener/gardener-extension-provider-openstack/pull/459), [@ialidzhikov](https://github.com/ialidzhikov))
* *[USER]* The following image is updated: ([gardener/gardener-extension-provider-openstack#462](https://github.com/gardener/gardener-extension-provider-openstack/pull/462), [@ialidzhikov](https://github.com/ialidzhikov))
  * k8scloudprovider/openstack-cloud-controller-manager: v1.24.1 -> v1.24.2
* *[USER]* The following image is updated: ([gardener/gardener-extension-provider-openstack#466](https://github.com/gardener/gardener-extension-provider-openstack/pull/466), [@ialidzhikov](https://github.com/ialidzhikov))
  * k8scloudprovider/openstack-cloud-controller-manager: v1.23.1 -> v1.23.2
* *[OPERATOR]* provider-openstack now mutates the `cluster-autoscaler` Deployment by implementing the `EnsureClusterAutoscalerDeployment` function. This is required in the context of https://github.com/kubernetes/autoscaler/issues/4517 - cluster-autoscaler supports `--feature-gates` flag and provider extensions have to mutate the cluster-autoscaler Deployment to add the CSI related feature gates to it. ([gardener/gardener-extension-provider-openstack#463](https://github.com/gardener/gardener-extension-provider-openstack/pull/463), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* Use openstack cloud-controller-manager `v1.22.0` for Shoots with target k8s version `v1.23.x`. [ref](https://github.com/kubernetes/cloud-provider-openstack/issues/1795) ([gardener/gardener-extension-provider-openstack#469](https://github.com/gardener/gardener-extension-provider-openstack/pull/469), [@dkistner](https://github.com/dkistner))
## 🏃 Others
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-openstack#480](https://github.com/gardener/gardener-extension-provider-openstack/pull/480), [@ialidzhikov](https://github.com/ialidzhikov))
  * docker.io/k8scloudprovider/cinder-csi-plugin: v1.23.0 -> v1.23.4 (for Kubernetes 1.23 Shoots)
* *[OPERATOR]* Handle extensionsv1alpha1.Bastion resources for SSH access to worker instances ([gardener/gardener-extension-provider-openstack#365](https://github.com/gardener/gardener-extension-provider-openstack/pull/365), [@tedteng](https://github.com/tedteng))
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-provider-openstack#465](https://github.com/gardener/gardener-extension-provider-openstack/pull/465), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-openstack#471](https://github.com/gardener/gardener-extension-provider-openstack/pull/471), [@ialidzhikov](https://github.com/ialidzhikov))
  * k8scloudprovider/openstack-cloud-controller-manager: v1.22.0 -> v1.23.3 (for Kubernetes 1.23 Shoots)
* *[OPERATOR]* Update Go version used to `v1.18` ([gardener/gardener-extension-provider-openstack#473](https://github.com/gardener/gardener-extension-provider-openstack/pull/473), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-openstack#476](https://github.com/gardener/gardener-extension-provider-openstack/pull/476), [@ialidzhikov](https://github.com/ialidzhikov))
  * docker.io/k8scloudprovider/cinder-csi-plugin: v1.20.0 -> v1.20.3 (for Kubernetes 1.20 Shoots)
  * docker.io/k8scloudprovider/cinder-csi-plugin: v1.24.0 -> v1.24.2 (for Kubernetes 1.24 Shoots)
# [machine-controller-manager]
## ⚠️ Breaking Changes
* *[OPERATOR]* The default leader election resource lock of `machine-controller-manager` has been changed from `endpointsleases` to `leases`. ([gardener/machine-controller-manager#711](https://github.com/gardener/machine-controller-manager/pull/711), [@acumino](https://github.com/acumino))
  * Please make sure, that you had at least `machine-controller-manager@v0.43.0` running before upgrading to `v0.46.0`, so that it has successfully acquired leadership with the hybrid resource lock (`endpointsleases`) at least once.
## 🐛 Bug Fixes
* *[USER]* Rollout freeze won't happen due to `Unknown` machines now. ([gardener/machine-controller-manager#733](https://github.com/gardener/machine-controller-manager/pull/733), [@himanshu-kun](https://github.com/himanshu-kun))
## 🏃 Others
* *[OPERATOR]* Published docker images for Machine-Controller-Manager are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/machine-controller-manager#732](https://github.com/gardener/machine-controller-manager/pull/732), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `machine-controller-manager` container now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager#734](https://github.com/gardener/machine-controller-manager/pull/734), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager-provider-openstack]
## 🐛 Bug Fixes
* *[OPERATOR]* Fixed missing volume status VolumeStatusDownloading when creating volume ([gardener/machine-controller-manager-provider-openstack#61](https://github.com/gardener/machine-controller-manager-provider-openstack/pull/61), [@namsral](https://github.com/namsral))
## 🏃 Others
* *[USER]* Update Go version to `v1.18` ([gardener/machine-controller-manager-provider-openstack#66](https://github.com/gardener/machine-controller-manager-provider-openstack/pull/66), [@kon-angelo](https://github.com/kon-angelo))
* *[USER]* Fix an issue where automatic revendoring did not assign correct permissions to CI scripts. ([gardener/machine-controller-manager-provider-openstack#69](https://github.com/gardener/machine-controller-manager-provider-openstack/pull/69), [@kon-angelo](https://github.com/kon-angelo))
* *[USER]* Use distroless base image ([gardener/machine-controller-manager-provider-openstack#62](https://github.com/gardener/machine-controller-manager-provider-openstack/pull/62), [@kon-angelo](https://github.com/kon-angelo))
* *[DEVELOPER]* probeResources() now doesn't try to delete orphan resources but only lists them. ([gardener/machine-controller-manager-provider-openstack#65](https://github.com/gardener/machine-controller-manager-provider-openstack/pull/65), [@kon-angelo](https://github.com/kon-angelo))
  * The beforeSuite for IT test now calls for cleanup of orphan resources separately.
  * The Integration Test, which looks for orphan resources, now doesn't try to delete the orphan resources and just waits for them to be done automatically.
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Terraform google provider is updated to v4.19.0 ([gardener/terraformer#119](https://github.com/gardener/terraformer/pull/119), [@bd3lage](https://github.com/bd3lage))