# [gardener-extension-shoot-dns-service]
## 🐛 Bug Fixes
* *[OPERATOR]* Fixed deployment of CRDs for dns-controller-manager if value `dnsControllerManager.createCRDs` is set to  `true` ([gardener/gardener-extension-shoot-dns-service#159](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/159), [@MartinWeindel](https://github.com/MartinWeindel))
## 🏃 Others
* *[OPERATOR]* Upgraded builder from golang version `1.18.5` -> `1.19.1` ([gardener/gardener-extension-shoot-dns-service#159](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/159), [@MartinWeindel](https://github.com/MartinWeindel))
# [external-dns-management]
## 🏃 Others
* *[USER]* Tolerate apex label `@` for Azure DNS on domain name validation ([gardener/external-dns-management#277](https://github.com/gardener/external-dns-management/pull/277), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Update builder image from golang `1.18.5` ->  `1.19.1` ([gardener/external-dns-management#278](https://github.com/gardener/external-dns-management/pull/278), [@MartinWeindel](https://github.com/MartinWeindel))