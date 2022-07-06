# [gardener-extension-provider-gcp]
## 🐛 Bug Fixes
* *[OPERATOR]* Fixed an issue that caused the VPA object for `csi-driver-node` to no longer match any Pods and effectively disabled vertical autoscaling for the DaemonSet. ([gardener/gardener-extension-provider-gcp#453](https://github.com/gardener/gardener-extension-provider-gcp/pull/453), [@ialidzhikov](https://github.com/ialidzhikov))