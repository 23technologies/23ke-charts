# [gardener-extension-provider-alicloud]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of admission-alicloud requires the SecretBinding provider controller to be enabled - enabled by default for gardener-controller-manager >= 1.42 or can be enabled via the gardener-controller-manager component config. ([gardener/gardener-extension-provider-alicloud#488](https://github.com/gardener/gardener-extension-provider-alicloud/pull/488), [@ialidzhikov](https://github.com/ialidzhikov))
## ✨ New Features
* *[USER]* The Alicloud extension does now support shoot clusters with Kubernetes version 1.24. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md) before upgrading to 1.24. ([gardener/gardener-extension-provider-alicloud#490](https://github.com/gardener/gardener-extension-provider-alicloud/pull/490), [@acumino](https://github.com/acumino))
* *[OPERATOR]* The extension does now automatically rotate its webhook CA and server certificates each `30d`. ([gardener/gardener-extension-provider-alicloud#487](https://github.com/gardener/gardener-extension-provider-alicloud/pull/487), [@rfranzke](https://github.com/rfranzke))
* *[OPERATOR]* This extension is prepared to support the Shoot `ServiceAccount` signing key rotation feature ([see documentation](https://github.com/gardener/gardener/blob/master/docs/usage/shoot_credentials_rotation.md#serviceaccount-token-signing-key)). ([gardener/gardener-extension-provider-alicloud#487](https://github.com/gardener/gardener-extension-provider-alicloud/pull/487), [@rfranzke](https://github.com/rfranzke))
## 🏃 Others
* *[OPERATOR]* The Secrets webhook of admission-alicloud: ([gardener/gardener-extension-provider-alicloud#488](https://github.com/gardener/gardener-extension-provider-alicloud/pull/488), [@ialidzhikov](https://github.com/ialidzhikov))
  * no longer intercepts every Secret UPDATE request but only requests for Secrets that are associated with a SecretBinding with `provider.type=alicloud`.
  * no longer needs to list Shoots (hence, no cache for Shoots)
* *[OPERATOR]* The admission-alicloud component introduces a new SecretBinding validator. It validates requests for SecretBindings and checks whether the SecretBinding refers to a valid Alicloud Secret. ([gardener/gardener-extension-provider-alicloud#488](https://github.com/gardener/gardener-extension-provider-alicloud/pull/488), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* The provider-alicloud extension now installs the external-snapshotter's validating webhook server for VolumeSnapshot and VolumeSnapshotContent objects. For more details check the corresponding [KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/1900-volume-snapshot-validation-webhook#kep-1900-add-additional-validation-to-volume-snapshot-objects). ([gardener/gardener-extension-provider-alicloud#485](https://github.com/gardener/gardener-extension-provider-alicloud/pull/485), [@shaoyongfeng](https://github.com/shaoyongfeng))
* *[OPERATOR]* machine-controller-manager-provider-alicloud RBAC does now allow get/list/watch on VolumeAttachments. ([gardener/gardener-extension-provider-alicloud#481](https://github.com/gardener/gardener-extension-provider-alicloud/pull/481), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* The resource requests and limits for components (seed and shoot) managed by the `provider-alicloud` extension has been adapted based on a production environment analysis. This is done to avoid OOMKills and cpu throttling situations. Furthermore the vpa `minAllowed` settings are now aligned with the cpu and memory request of the respective component` ([gardener/gardener-extension-provider-alicloud#480](https://github.com/gardener/gardener-extension-provider-alicloud/pull/480), [@shaoyongfeng](https://github.com/shaoyongfeng))
# [machine-controller-manager]
## 📖 Documentation
* *[USER]* upgraded k8s dependecy to v1.22.9 (revendor in providers required to see effects) ([gardener/machine-controller-manager#721](https://github.com/gardener/machine-controller-manager/pull/721), [@Mkmittal](https://github.com/Mkmittal))
* *[DEPENDENCY]* Paths transformations in .docforge/manifest.yaml for simplification ([gardener/machine-controller-manager#689](https://github.com/gardener/machine-controller-manager/pull/689), [@Kostov6](https://github.com/Kostov6))
## 🏃 Others
* *[OPERATOR]* Base image updated to alpine `v3.15.4` and build image to golang `1.17.9`. ([gardener/machine-controller-manager#713](https://github.com/gardener/machine-controller-manager/pull/713), [@himanshu-kun](https://github.com/himanshu-kun))
* *[DEPENDENCY]* K8s dependency upgraded to 1.21.12 ([gardener/machine-controller-manager#719](https://github.com/gardener/machine-controller-manager/pull/719), [@Mkmittal](https://github.com/Mkmittal))
# [machine-controller-manager-provider-alicloud]
## 🐛 Bug Fixes
* *[OPERATOR]* An issue causing machine-controller-manager-provider-alicloud on startup to panic with "duplicate metrics collector registration attempted" is now fixed. ([gardener/machine-controller-manager-provider-alicloud#26](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/26), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* An issue causing machine-controller-manager-provider-alicloud on startup to panic with "duplicate metrics collector registration attempted" is now fixed. ([gardener/machine-controller-manager-provider-alicloud#27](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/27), [@ialidzhikov](https://github.com/ialidzhikov))
## 📰 Noteworthy
* *[OPERATOR]* upgraded to mcm version 0.45.0 ([gardener/machine-controller-manager-provider-alicloud#28](https://github.com/gardener/machine-controller-manager-provider-alicloud/pull/28), [@rfranzke](https://github.com/rfranzke))

## Docker Images
gardener-extension-provider-alicloud: `eu.gcr.io/gardener-project/gardener/extensions/provider-alicloud:v1.37.0`
gardener-extension-admission-alicloud: `eu.gcr.io/gardener-project/gardener/extensions/admission-alicloud:v1.37.0`