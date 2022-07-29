# [machine-controller-manager]
## ⚠️ Breaking Changes
* *[OPERATOR]* The default leader election resource lock of `machine-controller-manager` has been changed from `endpointsleases` to `leases`. ([gardener/machine-controller-manager#711](https://github.com/gardener/machine-controller-manager/pull/711), [@acumino](https://github.com/acumino))
  * Please make sure, that you had at least `machine-controller-manager@v0.43.0` running before upgrading to `v0.46.0`, so that it has successfully acquired leadership with the hybrid resource lock (`endpointsleases`) at least once.
## 🐛 Bug Fixes
* *[USER]* Rollout freeze won't happen due to `Unknown` machines now. ([gardener/machine-controller-manager#733](https://github.com/gardener/machine-controller-manager/pull/733), [@himanshu-kun](https://github.com/himanshu-kun))
## 🏃 Others
* *[OPERATOR]* Published docker images for Machine-Controller-Manager are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/machine-controller-manager#732](https://github.com/gardener/machine-controller-manager/pull/732), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The `machine-controller-manager` container now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager#734](https://github.com/gardener/machine-controller-manager/pull/734), [@dimityrmirchev](https://github.com/dimityrmirchev))
# [machine-controller-manager-provider-alicloud]
## 🏃 Others
* *[OPERATOR]* upgraded to mcm version 0.46.0 ([gardener/machine-controller-manager-provider-alicloud#32](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/32), [@shaoyongfeng](https://github.com/shaoyongfeng))
* *[OPERATOR]* machine-controller-manager-provider-alicloud now uses `distroless` instead of `alpine` as a base image. ([gardener/machine-controller-manager-provider-alicloud#31](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/31), [@ialidzhikov](https://github.com/ialidzhikov))
* *[DEVELOPER]* Local IT for provider alicloud have been added ([gardener/machine-controller-manager-provider-alicloud#29](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/29), [@Mkmittal](https://github.com/Mkmittal))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Terraform google provider is updated to v4.19.0 ([gardener/terraformer#119](https://github.com/gardener/terraformer/pull/119), [@bd3lage](https://github.com/bd3lage))

## Docker Images
gardener-extension-provider-alicloud: `eu.gcr.io/gardener-project/gardener/extensions/provider-alicloud:v1.39.0`
gardener-extension-admission-alicloud: `eu.gcr.io/gardener-project/gardener/extensions/admission-alicloud:v1.39.0`