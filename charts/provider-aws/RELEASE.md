# [gardener-extension-provider-aws]
## ✨ New Features
* *[USER]* The aws extension does now support shoot clusters with Kubernetes version 1.25. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md) before upgrading to 1.25. ([gardener/gardener-extension-provider-aws#624](https://github.com/gardener/gardener-extension-provider-aws/pull/624), [@shafeeqes](https://github.com/shafeeqes))
## 🐛 Bug Fixes
* *[USER]* Disable automatic enablement of no-overlay network configuration for cluster >=1.22 ([gardener/gardener-extension-provider-aws#622](https://github.com/gardener/gardener-extension-provider-aws/pull/622), [@kon-angelo](https://github.com/kon-angelo))
## 🏃 Others
* *[OPERATOR]* Add route table associations for VPC endpoints ([gardener/gardener-extension-provider-aws#611](https://github.com/gardener/gardener-extension-provider-aws/pull/611), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Correctly enable aws custom route controller if required to ensure overlay free cluster operation. ([gardener/gardener-extension-provider-aws#612](https://github.com/gardener/gardener-extension-provider-aws/pull/612), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* Update EBS CSI driver to `v1.11.3` ([gardener/gardener-extension-provider-aws#616](https://github.com/gardener/gardener-extension-provider-aws/pull/616), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Update pause container image to v3.8 ([gardener/gardener-extension-provider-aws#627](https://github.com/gardener/gardener-extension-provider-aws/pull/627), [@kon-angelo](https://github.com/kon-angelo))
* *[OPERATOR]* Update golang for builder image: `1.18.3` -> `1.19.2` ([gardener/gardener-extension-provider-aws#602](https://github.com/gardener/gardener-extension-provider-aws/pull/602), [@MartinWeindel](https://github.com/MartinWeindel))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-provider-aws#609](https://github.com/gardener/gardener-extension-provider-aws/pull/609), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.53.0 -> v1.56.0
  * k8s.io/* : v0.24.3 -> v0.25.0
  * sigs.k8s.io/controller-runtime: v0.12.1 -> v0.13.0
# [machine-controller-manager-provider-aws]
## 🏃 Others
* *[DEPENDENCY]* The following dependency is updated: ([gardener/machine-controller-manager-provider-aws#96](https://github.com/gardener/machine-controller-manager-provider-aws/pull/96), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/machine-controller-manager v0.46.1 -> 0.47.0