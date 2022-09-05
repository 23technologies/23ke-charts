# [gardener-extension-networking-cilium]
## ⚠️ Breaking Changes
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-networking-cilium#120](https://github.com/gardener/gardener-extension-networking-cilium/pull/120), [@shafeeqes](https://github.com/shafeeqes))
## 🏃 Others
* *[OPERATOR]* Kubernetes conform hostPort/hostIP handling with cilium clusters. ([gardener/gardener-extension-networking-cilium#128](https://github.com/gardener/gardener-extension-networking-cilium/pull/128), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* Ensure that the kubernetes api server host is always set when running cilium without kube-proxy. ([gardener/gardener-extension-networking-cilium#116](https://github.com/gardener/gardener-extension-networking-cilium/pull/116), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-cilium#117](https://github.com/gardener/gardener-extension-networking-cilium/pull/117), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.50.1 -> v1.52.2
* *[OPERATOR]* Networking provider cilium works again with allowPrivilegedContainers=false. ([gardener/gardener-extension-networking-cilium#119](https://github.com/gardener/gardener-extension-networking-cilium/pull/119), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* Cilium works again with node-local-dns after change of default health check port to 8099. ([gardener/gardener-extension-networking-cilium#121](https://github.com/gardener/gardener-extension-networking-cilium/pull/121), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* The cilium/cilium-kube-proxy-clean-up init container no longer runs in privileged mode. ([gardener/gardener-extension-networking-cilium#123](https://github.com/gardener/gardener-extension-networking-cilium/pull/123), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-cilium#126](https://github.com/gardener/gardener-extension-networking-cilium/pull/126), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.52.2 -> v1.54.0
  * k8s.io/* : v0.24.3 -> v0.24.4
* *[OPERATOR]* Removed support for kubernetes < 1.17 from cilium networking provider. ([gardener/gardener-extension-networking-cilium#127](https://github.com/gardener/gardener-extension-networking-cilium/pull/127), [@ScheererJ](https://github.com/ScheererJ))
* *[DEPENDENCY]* The following dependency is updated: ([gardener/gardener-extension-networking-cilium#118](https://github.com/gardener/gardener-extension-networking-cilium/pull/118), [@shafeeqes](https://github.com/shafeeqes))
  * k8s.io/* : v0.24.2 -> v0.24.3