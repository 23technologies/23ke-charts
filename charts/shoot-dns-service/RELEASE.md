# [gardener-extension-shoot-dns-service]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of gardener-extension-shoot-dns-service requires Gardener v1.52+. ([gardener/gardener-extension-shoot-dns-service#146](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/146), [@gardener-robot-ci-1](https://github.com/gardener-robot-ci-1))
* *[OPERATOR]* This version of gardener-extension-shoot-dns-service requires Gardener v1.50+. ([gardener/gardener-extension-shoot-dns-service#143](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/143), [@kris94](https://github.com/kris94))
## 🏃 Others
* *[OPERATOR]* doc user ([gardener/gardener-extension-shoot-dns-service#144](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/144), [@etiennnr](https://github.com/etiennnr))
* *[OPERATOR]* Add optional deployment for dns-controller-manager ([gardener/gardener-extension-shoot-dns-service#145](https://github.com/gardener/gardener-extension-shoot-dns-service/pull/145), [@MartinWeindel](https://github.com/MartinWeindel))
# [external-dns-management]
## ✨ New Features
* *[USER]* Weighted routing policy is now supported for AWS Route53 and Google CloudDNS. ([gardener/external-dns-management#270](https://github.com/gardener/external-dns-management/pull/270), [@MartinWeindel](https://github.com/MartinWeindel))
  * There can now be multiple `DNSEntries` for the same domain name (distinguished by the `setIdentifier` in the `spec.routingPolicy` section). For details see https://github.com/gardener/external-dns-management/tree/master/docs/aws-route53#weighted-routing-policy
## 🐛 Bug Fixes
* *[OPERATOR]* [openstack-designate] Select correct recordset on updating wildcard domain names ([gardener/external-dns-management#268](https://github.com/gardener/external-dns-management/pull/268), [@MartinWeindel](https://github.com/MartinWeindel))