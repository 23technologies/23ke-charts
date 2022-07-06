# [gardener-extension-provider-aws]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of admission-aws requires the SecretBinding provider controller to be enabled - enabled by default for gardener-controller-manager >= 1.42 or can be enabled via the gardener-controller-manager component config. ([gardener/gardener-extension-provider-aws#551](https://github.com/gardener/gardener-extension-provider-aws/pull/551), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* This extension is only compatible with Gardener versions `>= v1.37`. ([gardener/gardener-extension-provider-aws#538](https://github.com/gardener/gardener-extension-provider-aws/pull/538), [@timebertt](https://github.com/timebertt))
## ✨ New Features
* *[USER]* The AWS extension does now support shoot clusters with Kubernetes version 1.24. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md) before upgrading to 1.24. ([gardener/gardener-extension-provider-aws#553](https://github.com/gardener/gardener-extension-provider-aws/pull/553), [@acumino](https://github.com/acumino))
* *[OPERATOR]* The extension does now automatically rotate its webhook CA and server certificates each `30d`. ([gardener/gardener-extension-provider-aws#550](https://github.com/gardener/gardener-extension-provider-aws/pull/550), [@rfranzke](https://github.com/rfranzke))
* *[OPERATOR]* This extension is prepared to support the Shoot `ServiceAccount` signing key rotation feature ([see documentation](https://github.com/gardener/gardener/blob/master/docs/usage/shoot_credentials_rotation.md#serviceaccount-token-signing-key)). ([gardener/gardener-extension-provider-aws#550](https://github.com/gardener/gardener-extension-provider-aws/pull/550), [@rfranzke](https://github.com/rfranzke))
* *[OPERATOR]* This extension is prepared to support the Shoot CA rotation feature ([GEP-18](https://github.com/gardener/gardener/issues/3292)). ([gardener/gardener-extension-provider-aws#538](https://github.com/gardener/gardener-extension-provider-aws/pull/538), [@timebertt](https://github.com/timebertt))
## 🐛 Bug Fixes
* *[OPERATOR]* An issue causing admission-aws to fail a Shoot creation request with `.spec.provider.infrastructureConfig=nil` with 500 Internal server error is now fixed. admission-aws now properly indicates in the response that the corresponding field is required. ([gardener/gardener-extension-provider-aws#549](https://github.com/gardener/gardener-extension-provider-aws/pull/549), [@ialidzhikov](https://github.com/ialidzhikov))
## 📖 Documentation
* *[USER]* add link to K8s v1.23 conformance tests ([gardener/gardener-extension-provider-aws#537](https://github.com/gardener/gardener-extension-provider-aws/pull/537), [@hendrikKahl](https://github.com/hendrikKahl))
* *[DEPENDENCY]* Paths transformations in .docforge/manifest.yaml for simplification ([gardener/gardener-extension-provider-aws#517](https://github.com/gardener/gardener-extension-provider-aws/pull/517), [@Kostov6](https://github.com/Kostov6))
## 🏃 Others
* *[USER]* The following image is updated: ([gardener/gardener-extension-provider-aws#541](https://github.com/gardener/gardener-extension-provider-aws/pull/541), [@kon-angelo](https://github.com/kon-angelo))
  * k8s.gcr.io/provider-aws/aws-ebs-csi-driver: v1.5.0 -> v1.5.3
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-provider-aws#553](https://github.com/gardener/gardener-extension-provider-aws/pull/553), [@acumino](https://github.com/acumino))
  * eu.gcr.io/gardener-project/kubernetes/cloud-provider-aws: 1.23.6 -> 1.24.0(For shoots with Kubernetes version 1.24)
* *[OPERATOR]* The Secrets webhook of admission-aws: ([gardener/gardener-extension-provider-aws#551](https://github.com/gardener/gardener-extension-provider-aws/pull/551), [@ialidzhikov](https://github.com/ialidzhikov))
  * no longer intercepts every Secret UPDATE request but only requests for Secrets that are associated with a SecretBinding with `provider.type=aws`.
  * no longer needs to list Shoots (hence, no cache for Shoots)
* *[OPERATOR]* The admission-aws component introduces a new SecretBinding validator. It validates requests for SecretBindings and checks whether the SecretBinding refers to a valid AWS Secret. ([gardener/gardener-extension-provider-aws#551](https://github.com/gardener/gardener-extension-provider-aws/pull/551), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* The following images used by the mtu-customizer DaemonSet are updated: ([gardener/gardener-extension-provider-aws#548](https://github.com/gardener/gardener-extension-provider-aws/pull/548), [@ialidzhikov](https://github.com/ialidzhikov))
  * alpine: 3.12.1 -> 3.15.4
  * k8s.gcr.io/pause: 3.1 -> 3.7
* *[OPERATOR]* The dashboards: Cloud Controller Manager and CSI Driver are removed from Grafana ([gardener/gardener-extension-provider-aws#534](https://github.com/gardener/gardener-extension-provider-aws/pull/534), [@Kristian-ZH](https://github.com/Kristian-ZH))
* *[OPERATOR]* The resource requests and limits for components (seed and shoot) managed by the `provider-aws` extension has been adapted based on a production environment analysis. This is done to avoid OOMKills and cpu throttling situations. Furthermore the vpa `minAllowed` settings are now aligned with the cpu and memory request of the respective component` ([gardener/gardener-extension-provider-aws#527](https://github.com/gardener/gardener-extension-provider-aws/pull/527), [@dkistner](https://github.com/dkistner))
# [aws-lb-readvertiser]
## 🏃 Others
* *[OPERATOR]* Updated alpine base image to `v3.15.4` ([gardener/aws-lb-readvertiser#20](https://github.com/gardener/aws-lb-readvertiser/pull/20), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* The release tags from now are prefixed with `v`. ([gardener/aws-lb-readvertiser#18](https://github.com/gardener/aws-lb-readvertiser/pull/18), [@ialidzhikov](https://github.com/ialidzhikov))
# [cloud-provider-aws]
## ✨ New Features
* *[DEPENDENCY]* `k8s.io/legacy-cloud-providers` is now updated to `v1.21.12`. ([gardener/cloud-provider-aws@6e0c40b2ccad](https://github.com/gardener/cloud-provider-aws/commit/6e0c40b2ccadbe44167c9730f378faf28474d1b2))
* *[DEPENDENCY]* `k8s.io/legacy-cloud-providers` is now updated to `v1.22.9`. ([gardener/cloud-provider-aws@a8cb9b6b1aba](https://github.com/gardener/cloud-provider-aws/commit/a8cb9b6b1aba4dd8630daecfee2647aa0ea0069d))
* *[DEPENDENCY]* `k8s.io/legacy-cloud-providers` is now updated to `v1.23.6`. ([gardener/cloud-provider-aws@47e83c698b7b](https://github.com/gardener/cloud-provider-aws/commit/47e83c698b7b1ce0f2e8f1437e024d34ffd0fcd7))
## 🏃 Others
* *[DEVELOPER]* The alpine version has been updated to `v3.15.4`. ([gardener/cloud-provider-aws@d451e4ca38fc](https://github.com/gardener/cloud-provider-aws/commit/d451e4ca38fcb67bfa9c355f605039619c136c9e))
* *[DEVELOPER]* The Golang version has been updated to `v1.16.15`. ([gardener/cloud-provider-aws@d451e4ca38fc](https://github.com/gardener/cloud-provider-aws/commit/d451e4ca38fcb67bfa9c355f605039619c136c9e))
* *[DEVELOPER]* The alpine version has been updated to `v3.15.4`. ([gardener/cloud-provider-aws@9a33c6496ef4](https://github.com/gardener/cloud-provider-aws/commit/9a33c6496ef4b77cc1f93ea81084259765349d71))
* *[DEVELOPER]* The Golang version has been updated to `v1.16.15`. ([gardener/cloud-provider-aws@9a33c6496ef4](https://github.com/gardener/cloud-provider-aws/commit/9a33c6496ef4b77cc1f93ea81084259765349d71))
* *[DEVELOPER]* The alpine version has been updated to `v3.15.4`. ([gardener/cloud-provider-aws@c8f610c5c43f](https://github.com/gardener/cloud-provider-aws/commit/c8f610c5c43f9cf31d720604c0d0f11fbd2e96e0))
* *[DEVELOPER]* The Golang version has been updated to `v1.17.9`. ([gardener/cloud-provider-aws@c8f610c5c43f](https://github.com/gardener/cloud-provider-aws/commit/c8f610c5c43f9cf31d720604c0d0f11fbd2e96e0))
# [machine-controller-manager]
## 📖 Documentation
* *[USER]* upgraded k8s dependecy to v1.22.9 (revendor in providers required to see effects) ([gardener/machine-controller-manager#721](https://github.com/gardener/machine-controller-manager/pull/721), [@Mkmittal](https://github.com/Mkmittal))
* *[DEPENDENCY]* Paths transformations in .docforge/manifest.yaml for simplification ([gardener/machine-controller-manager#689](https://github.com/gardener/machine-controller-manager/pull/689), [@Kostov6](https://github.com/Kostov6))
## 🏃 Others
* *[OPERATOR]* Base image updated to alpine `v3.15.4` and build image to golang `1.17.9`. ([gardener/machine-controller-manager#713](https://github.com/gardener/machine-controller-manager/pull/713), [@himanshu-kun](https://github.com/himanshu-kun))
* *[DEPENDENCY]* K8s dependency upgraded to 1.21.12 ([gardener/machine-controller-manager#719](https://github.com/gardener/machine-controller-manager/pull/719), [@Mkmittal](https://github.com/Mkmittal))
# [machine-controller-manager-provider-aws]
## 📰 Noteworthy
* *[OPERATOR]* upgraded to mcm version 0.45.0 ([gardener/machine-controller-manager-provider-aws#88](https://github.com/gardener/machine-controller-manager-provider-aws/pull/88), [@rfranzke](https://github.com/rfranzke))
# [terraformer]
## 🏃 Others
* *[OPERATOR]* Update alpine to 3.15.4 ([gardener/terraformer#117](https://github.com/gardener/terraformer/pull/117), [@rfranzke](https://github.com/rfranzke))