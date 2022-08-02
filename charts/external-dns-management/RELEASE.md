# [external-dns-management]
## ✨ New Features
* *[USER]* Weighted routing policy is now supported for AWS Route53 and Google CloudDNS. ([gardener/external-dns-management#270](https://github.com/gardener/external-dns-management/pull/270), [@MartinWeindel](https://github.com/MartinWeindel))
  * There can now be multiple `DNSEntries` for the same domain name (distinguished by the `setIdentifier` in the `spec.routingPolicy` section). For details see https://github.com/gardener/external-dns-management/tree/master/docs/aws-route53#weighted-routing-policy
## 🐛 Bug Fixes
* *[OPERATOR]* [openstack-designate] Select correct recordset on updating wildcard domain names ([gardener/external-dns-management#268](https://github.com/gardener/external-dns-management/pull/268), [@MartinWeindel](https://github.com/MartinWeindel))