# [gardener-extension-networking-calico]
## ⚠️ Breaking Changes
* *[OPERATOR]* This version of gardener-extension-networking-calico requires Gardener v1.50+. ([gardener/gardener-extension-networking-calico#192](https://github.com/gardener/gardener-extension-networking-calico/pull/192), [@kris94](https://github.com/kris94))
## 🐛 Bug Fixes
* *[USER]* An issue causing Pod creation to fail for calico-node, calico-typha and calico-kube-controllers components when privileged containers are not allowed is now fixed. ([gardener/gardener-extension-networking-calico#181](https://github.com/gardener/gardener-extension-networking-calico/pull/181), [@ialidzhikov](https://github.com/ialidzhikov))
## 🏃 Others
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-calico#197](https://github.com/gardener/gardener-extension-networking-calico/pull/197), [@DockToFuture](https://github.com/DockToFuture))
  * github.com/gardener/gardener: v1.47.0 -> v1.50.1
  * sigs.k8s.io/controller-runtime v0.11.1 -> v0.12.1
* *[OPERATOR]* Add liveness and readiness probe to admission webhook. ([gardener/gardener-extension-networking-calico#180](https://github.com/gardener/gardener-extension-networking-calico/pull/180), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* Increased memory limit of calico kube-controllers to 2Gi. ([gardener/gardener-extension-networking-calico#184](https://github.com/gardener/gardener-extension-networking-calico/pull/184), [@ScheererJ](https://github.com/ScheererJ))
* *[OPERATOR]* Update calico to v3.23.1 and update dependencies on gardener (v1.47.0) and golang (v1.18). ([gardener/gardener-extension-networking-calico#185](https://github.com/gardener/gardener-extension-networking-calico/pull/185), [@DockToFuture](https://github.com/DockToFuture))
* *[OPERATOR]* The extension now uses `distroless` instead of `alpine` as a base image. ([gardener/gardener-extension-networking-calico#187](https://github.com/gardener/gardener-extension-networking-calico/pull/187), [@dimityrmirchev](https://github.com/dimityrmirchev))
* *[OPERATOR]* Update `cpvpa` to `k8s.gcr.io/cpa/cpvpa:v0.8.4` since it's a multi-arch image. ([gardener/gardener-extension-networking-calico#189](https://github.com/gardener/gardener-extension-networking-calico/pull/189), [@rfranzke](https://github.com/rfranzke))
* *[OPERATOR]* The following dependency is updated: ([gardener/gardener-extension-networking-calico#190](https://github.com/gardener/gardener-extension-networking-calico/pull/190), [@acumino](https://github.com/acumino))
  * k8s.gcr.io/cpa/cluster-proportional-autoscaler: 1.8.3 -> 1.8.5
* *[OPERATOR]* Update calico to v3.23.2. ([gardener/gardener-extension-networking-calico#191](https://github.com/gardener/gardener-extension-networking-calico/pull/191), [@DockToFuture](https://github.com/DockToFuture))