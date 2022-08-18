# [gardener-extension-networking-calico]
## ⚠️ Breaking Changes
* *[OPERATOR]* Please make sure you're running gardener@v1.52 or above before upgrading to this version. ([gardener/gardener-extension-networking-calico#203](https://github.com/gardener/gardener-extension-networking-calico/pull/203), [@shafeeqes](https://github.com/shafeeqes))
## 🐛 Bug Fixes
* *[OPERATOR]* The `PodDisruptionBudget` for `calico-kube-controllers` is removed, as it is a singleton and can prevent VPA from scaling it up. ([gardener/gardener-extension-networking-calico#183](https://github.com/gardener/gardener-extension-networking-calico/pull/183), [@timebertt](https://github.com/timebertt))
## 🏃 Others
* *[OPERATOR]* The calico-kube-controllers/calico-kube-controllers container no longer runs in privileged mode. ([gardener/gardener-extension-networking-calico#196](https://github.com/gardener/gardener-extension-networking-calico/pull/196), [@ialidzhikov](https://github.com/ialidzhikov))
* *[OPERATOR]* Published docker images for Calico extension come now with multi-arch support including `linux/amd64` and `linux/arm64`. ([gardener/gardener-extension-networking-calico#198](https://github.com/gardener/gardener-extension-networking-calico/pull/198), [@timuthy](https://github.com/timuthy))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-calico#201](https://github.com/gardener/gardener-extension-networking-calico/pull/201), [@shafeeqes](https://github.com/shafeeqes))
  * github.com/gardener/gardener: v1.50.1 -> v1.52.0
* *[OPERATOR]* Update calico to v3.23.3. ([gardener/gardener-extension-networking-calico#202](https://github.com/gardener/gardener-extension-networking-calico/pull/202), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* Pods for `calico-kube-controllers`, `calico-node`, `calico-node-vertical-autoscaler`, `calico-typha`, `calico-typha-horizontal-autoscaler` and `calico-typha-vertical-autoscaler` components now have their seccomp profile set to "RuntimeDefault". ([gardener/gardener-extension-networking-calico#204](https://github.com/gardener/gardener-extension-networking-calico/pull/204), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-calico#205](https://github.com/gardener/gardener-extension-networking-calico/pull/205), [@shafeeqes](https://github.com/shafeeqes))
  * k8s.io/* : v0.24.2 -> v0.24.3
* *[OPERATOR]* The following image is updated: ([gardener/gardener-extension-networking-calico#206](https://github.com/gardener/gardener-extension-networking-calico/pull/206), [@ialidzhikov](https://github.com/ialidzhikov))
  * k8s.gcr.io/cpa/cluster-proportional-autoscaler: v1.8.5 -> v1.8.6