# [gardener-extension-networking-cilium]
## 🏃 Others
* *[OPERATOR]* Egress gateway feature is now supported in cilium. It allows users to redirect egress pod traffic through specific, gateway nodes. ([gardener/gardener-extension-networking-cilium#102](https://github.com/gardener/gardener-extension-networking-cilium/pull/102), [@jastBytes](https://github.com/jastBytes))
* *[OPERATOR]* Add default memory requests/limits to cilium/hubble-relay container. ([gardener/gardener-extension-networking-cilium#104](https://github.com/gardener/gardener-extension-networking-cilium/pull/104), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* Add default memory requests/limits to etcd-operator container. ([gardener/gardener-extension-networking-cilium#105](https://github.com/gardener/gardener-extension-networking-cilium/pull/105), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* The following dependencies are updated: ([gardener/gardener-extension-networking-cilium#107](https://github.com/gardener/gardener-extension-networking-cilium/pull/107), [@DockToFuture](https://github.com/DockToFuture))
  * github.com/gardener/gardener: v1.47.0 -> v1.50.1
  * sigs.k8s.io/controller-runtime v0.11.1 -> v0.12.1
  * go 1.17 -> 1.18