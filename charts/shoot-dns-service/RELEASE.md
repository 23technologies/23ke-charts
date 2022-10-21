# [gardener-extension-shoot-dns-service]
## 🏃 Others
* *[OPERATOR]* `shoot-dns-server` Pod now runs with the appropriate priority set according to the following [document](https://github.com/gardener/gardener/blob/v1.57.1/docs/development/priority-classes.md). ([gardener/gardener-extension-shoot-dns-service#163](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/163), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* Update builder image from `golang:1.19.1` to `golang:1.19.2` ([gardener/gardener-extension-shoot-dns-service#165](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/165), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Update dependency gardener/gardener `v1.52.2` to `v1.56.0` ([gardener/gardener-extension-shoot-dns-service#165](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/165), [@MartinWeindel](https://github.com/MartinWeindel))
# [external-dns-management]
## 🏃 Others
* *[OPERATOR]* Updated controller-manager-library dependency including K8s dependencies `v1.24.1` to `v1.25.0`. ([gardener/external-dns-management#281](https://github.com/gardener/external-dns-management/pull/281), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Ignore slave objects of non-responsible DNS classes. ([gardener/external-dns-management#279](https://github.com/gardener/external-dns-management/pull/279), [@MartinWeindel](https://github.com/MartinWeindel))