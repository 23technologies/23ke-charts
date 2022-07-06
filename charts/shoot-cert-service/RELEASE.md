# [gardener-extension-shoot-cert-service]
## 🏃 Others
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-shoot-cert-service#121](https://github.com/gardener/gardener-extension-shoot-cert-service/pull/121), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* Adjust metric name due to upgrading the kube-state-metrics component ([gardener/gardener-extension-shoot-cert-service#122](https://github.com/gardener/gardener-extension-shoot-cert-service/pull/122), [@istvanballok](https://github.com/istvanballok))
* *[OPERATOR]* vendor to gardener/gardener v1.49.3 ([gardener/gardener-extension-shoot-cert-service#124](https://github.com/gardener/gardener-extension-shoot-cert-service/pull/124), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* No predefined resources to allow to drop cpu limits. ([gardener/gardener-extension-shoot-cert-service#125](https://github.com/gardener/gardener-extension-shoot-cert-service/pull/125), [@MartinWeindel](https://github.com/MartinWeindel))
# [cert-management]
## 🏃 Others
* *[OPERATOR]* Update prometheus-client dependency to v1.12.2 ([gardener/cert-management#107](https://github.com/gardener/cert-management/pull/107), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Update Kubernetes dependencies to `v0.24.1` ([gardener/cert-management#109](https://github.com/gardener/cert-management/pull/109), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Update base image to `alpine:3.16.0` ([gardener/cert-management#110](https://github.com/gardener/cert-management/pull/110), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* The `cert-controller-manager` now uses `distroless` instead of `alpine` as a base image. ([gardener/cert-management#111](https://github.com/gardener/cert-management/pull/111), [@dimityrmirchev](https://github.com/dimityrmirchev))