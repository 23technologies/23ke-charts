# [gardener-extension-shoot-dns-service]
## 📖 Documentation
* *[OPERATOR]* Enable DNSProvider management and add image section ([gardener/gardener-extension-shoot-dns-service#166](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/166), [@MartinWeindel](https://github.com/MartinWeindel))
## 🏃 Others
* *[OPERATOR]* Adds a heartbeat controller that creates and renews a `Lease` resource named `gardener-extension-heartbeat` in the namespace where the extension controller is deployed. This `Lease` resource can be used by other controllers to check if the `shoot-dns-service` extension controller is running. ([gardener/gardener-extension-shoot-dns-service#168](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/168), [@AleksandarSavchev](https://github.com/AleksandarSavchev))
* *[DEPENDENCY]* Dependency `github.com/gardener/gardener` is updated `v1.56.0` -> `v1.59.0`. ([gardener/gardener-extension-shoot-dns-service#168](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/168), [@AleksandarSavchev](https://github.com/AleksandarSavchev))
# [external-dns-management]
## 🏃 Others
* *[USER]* Allow more CNAME targets ([gardener/external-dns-management#285](https://github.com/gardener/external-dns-management/pull/285), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Updated builder image golang: `v1.19.2` => `v1.19.3` ([gardener/external-dns-management#286](https://github.com/gardener/external-dns-management/pull/286), [@MartinWeindel](https://github.com/MartinWeindel))