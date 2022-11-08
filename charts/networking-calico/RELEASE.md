# [gardener-extension-networking-calico]
## ✨ New Features
* *[OPERATOR]* A new feature gate named `NonPrivilegedCalicoNode` is now added to the networking-calico extension. It allows running the long-lived calico-node container in non-privileged and non-root mode. ([gardener/gardener-extension-networking-calico#209](https://github.com/gardener/gardener-extension-networking-calico/pull/209), [@ialidzhikov](https://github.com/ialidzhikov))
## 🐛 Bug Fixes
* *[OPERATOR]* The networking-calico extension Pod is now automatically restarted when its component configuration ConfigMap changes. ([gardener/gardener-extension-networking-calico#212](https://github.com/gardener/gardener-extension-networking-calico/pull/212), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-calico#210](https://github.com/gardener/gardener-extension-networking-calico/pull/210), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.52.0 -> v1.54.0
  * k8s.io/* : v0.24.3 -> v0.24.4
* *[OPERATOR]* The calico extension supports switching between overlay and non overlay mode ([gardener/gardener-extension-networking-calico#215](https://github.com/gardener/gardener-extension-networking-calico/pull/215), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* Update go version to `v1.19.2`. ([gardener/gardener-extension-networking-calico#217](https://github.com/gardener/gardener-extension-networking-calico/pull/217), [@DockToFuture](https://github.com/DockToFuture))