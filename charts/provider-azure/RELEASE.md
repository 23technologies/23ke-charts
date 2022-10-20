# [gardener-extension-provider-azure]
## ⚠️ Breaking Changes
* *[OPERATOR]* provider-azure no longer supports Shoots with Кubernetes version < 1.17. ([gardener/gardener-extension-provider-azure#573](https://github.com/gardener/gardener-extension-provider-azure/pull/573), [@dimitar-kostadinov](https://github.com/dimitar-kostadinov))
## ✨ New Features
* *[USER]* The Azure extension does now support shoot clusters with Kubernetes version 1.25. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md) before upgrading to 1.25. ([gardener/gardener-extension-provider-azure#575](https://github.com/gardener/gardener-extension-provider-azure/pull/575), [@shafeeqes](https://github.com/shafeeqes))
## 🏃 Others
* *[OPERATOR]* Update version of `github.com/gardener/remedy-controller` v0.10.0 ([gardener/gardener-extension-provider-azure#576](https://github.com/gardener/gardener-extension-provider-azure/pull/576), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Update `azurefile-csi-driver` to v1.21.0 ([gardener/gardener-extension-provider-azure#577](https://github.com/gardener/gardener-extension-provider-azure/pull/577), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* The following images are updated: ([gardener/gardener-extension-provider-azure#581](https://github.com/gardener/gardener-extension-provider-azure/pull/581), [@dkistner](https://github.com/dkistner))
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-controller-manager: v1.23.14 -> v1.23.21 (for K8s 1.23 Shoots)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-node-manager: v1.23.14 -> v1.23.21 (for K8s 1.23 Shoots)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-controller-manager: v1.24.2 -> v1.24.8 (for K8s 1.24 Shoots)
  * mcr.microsoft.com/oss/kubernetes/azure-cloud-node-manager: v1.24.2 -> v1.24.8 (for K8s 1.24 Shoots)
* *[OPERATOR]* Update go version `v1.18.3` -> `v1.19.2` ([gardener/gardener-extension-provider-azure#582](https://github.com/gardener/gardener-extension-provider-azure/pull/582), [@kon-angelo](https://github.com/kon-angelo))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-provider-azure#572](https://github.com/gardener/gardener-extension-provider-azure/pull/572), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.53.0 -> v1.56.0
  * k8s.io/* : v0.24.3 -> v0.25.0
  * sigs.k8s.io/controller-runtime: v0.12.1 -> v0.13.0