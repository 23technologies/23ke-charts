# [gardener-extension-provider-azure]
## 🐛 Bug Fixes
* *[USER]* An issue causing Shoot creation to fail for K8s >= 1.23 clusters with `spec.kubenetes.allowPrivilegedContainers=false` is now fixed. ([gardener/gardener-extension-provider-azure#524](https://github.com/gardener/gardener-extension-provider-azure/pull/524), [@ialidzhikov](https://github.com/ialidzhikov))
## Docker Images
gardener-extension-provider-azure: `eu.gcr.io/gardener-project/gardener/extensions/provider-azure:v1.28.1`
gardener-extension-admission-azure: `eu.gcr.io/gardener-project/gardener/extensions/admission-azure:v1.28.1`