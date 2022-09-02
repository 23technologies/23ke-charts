# [gardener-extension-runtime-gvisor]
## ⚠️ Breaking Changes
* *[OPERATOR]* Please make sure you're running gardener@v1.53 or above before upgrading to this version. ([gardener/gardener-extension-runtime-gvisor#56](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/56), [@shafeeqes](https://github.com/shafeeqes))
## 🐛 Bug Fixes
* *[DEVELOPER]* An issue causing the integration test execution to fail due to outdated golang version is now fixed. ([gardener/gardener-extension-runtime-gvisor#45](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/45), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[OPERATOR]* Updated the alpine base image for the installation pods to 3.16.1. ([gardener/gardener-extension-runtime-gvisor#53](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/53), [@kris94](https://github.com/kris94))
* *[OPERATOR]* Golang version is updated to 1.18.5 ([gardener/gardener-extension-runtime-gvisor#53](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/53), [@kris94](https://github.com/kris94))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-runtime-gvisor#55](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/55), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.45.0 -> v1.53.0
  * k8s.io/* : v0.23.3 -> v0.24.3
  * sigs.k8s.io/controller-runtime: v0.11.1 -> v0.12.1
* *[OPERATOR]* Published docker images for gvisor are now multi-arch ready. They support `linux/amd64` and `linux/arm64`. ([gardener/gardener-extension-runtime-gvisor#57](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/57), [@acumino](https://github.com/acumino))
## 📰 Noteworthy
* *[OPERATOR]* This version of gardener-extension-runtime-gvisor requires Gardener v1.50+. ([gardener/gardener-extension-runtime-gvisor#48](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/48), [@kris94](https://github.com/kris94))
* *[OPERATOR]* The extension container now uses `distroless` as a base image. ([gardener/gardener-extension-runtime-gvisor#49](https://github.com/gardener/gardener-extension-runtime-gvisor/pull/49), [@dimityrmirchev](https://github.com/dimityrmirchev))