# [gardener-extension-shoot-dns-service]
## 🏃 Others
* *[OPERATOR]* A fixed memory limit was set for the shoot-dns-service component, in accordance with measurements of actual field usage. CPU limit of same container was removed. ([gardener/gardener-extension-shoot-dns-service#130](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/130), [@andrerun](https://github.com/andrerun))
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-shoot-dns-service#137](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/137), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* Switch to autoscaling.k8s.io/v1 for VPA objects ([gardener/gardener-extension-shoot-dns-service#138](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/138), [@voelzmo](https://github.com/voelzmo))
* *[OPERATOR]* vendor to gardener/gardener v1.49.3 ([gardener/gardener-extension-shoot-dns-service#140](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/140), [@hendrikKahl](https://github.com/hendrikKahl))
* *[OPERATOR]* No predefined resources to allow to drop cpu limits. ([gardener/gardener-extension-shoot-dns-service#141](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/141), [@MartinWeindel](https://github.com/MartinWeindel))
# [external-dns-management]
## ⚠️ Breaking Changes
* *[OPERATOR]* Persisting zone state caches with option `--cache-dir` is not supported anymore. ([gardener/external-dns-management#261](https://github.com/gardener/external-dns-management/pull/261), [@MartinWeindel](https://github.com/MartinWeindel))
## ✨ New Features
* *[OPERATOR]* Check for forwarded domains in same account. ([gardener/external-dns-management#262](https://github.com/gardener/external-dns-management/pull/262), [@MartinWeindel](https://github.com/MartinWeindel))
## 🐛 Bug Fixes
* *[USER]* Zones of forwarded subdomains are not included anymore automatically, if the `spec.domains.include` specifies the domain of the base zone only. If base domain and forwarded subdomain should both be included, the forwarded subdomain must be specified explicitly either as domain or zone include. ([gardener/external-dns-management#260](https://github.com/gardener/external-dns-management/pull/260), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Don't cleanup entries belonging to a provider of  an equivalent zone. ([gardener/external-dns-management#257](https://github.com/gardener/external-dns-management/pull/257), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Manage zone state cache globally ([gardener/external-dns-management#261](https://github.com/gardener/external-dns-management/pull/261), [@MartinWeindel](https://github.com/MartinWeindel))
## 🏃 Others
* *[OPERATOR]* Updated gophercloud Openstack SDK to version `v0.24.0` ([gardener/external-dns-management#258](https://github.com/gardener/external-dns-management/pull/258), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Restart if watch fails because of disappeared resource ([gardener/external-dns-management#266](https://github.com/gardener/external-dns-management/pull/266), [@MartinWeindel](https://github.com/MartinWeindel))
* *[OPERATOR]* Using distroless base image ([gardener/external-dns-management#267](https://github.com/gardener/external-dns-management/pull/267), [@MartinWeindel](https://github.com/MartinWeindel))