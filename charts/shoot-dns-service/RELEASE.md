# [gardener-extension-shoot-dns-service]
## 🏃 Others
* *[USER]* Improve error message for DNS entry failed deletion ([gardener/gardener-extension-shoot-dns-service#155](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/155), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* The `PodSecurityPolicy` `extensions.gardener.cloud.shoot-dns-service.dns-controller-manager` is not deployed for seeds with k8s `version >=1.24` ([gardener/gardener-extension-shoot-dns-service#153](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/153), [@shafeeqes](https://github.com/shafeeqes))
# [external-dns-management]
## 🏃 Others
* *[OPERATOR]* The `PodSecurityPolicy` `dns-controller-manager` is not deployed for seeds with k8s `>=1.24` ([gardener/external-dns-management#273](https://github.com/gardener/external-dns-management/pull/273), [@shafeeqes](https://github.com/shafeeqes))
* *[OPERATOR]* Reconcile deleting entries after its provider has been repaired ([gardener/external-dns-management#275](https://github.com/gardener/external-dns-management/pull/275), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Updated build image golang:v1.18.3 -> v1.18.5 ([gardener/external-dns-management#275](https://github.com/gardener/external-dns-management/pull/275), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Add flag --disable-dnsname-validation to optionally disable the validation of DNS names according to RFC 1123. ([gardener/external-dns-management#276](https://github.com/gardener/external-dns-management/pull/276), [@MartinWeindel](https://github.com/MartinWeindel))