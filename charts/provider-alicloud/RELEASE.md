# [gardener-extension-provider-alicloud]
## ✨ New Features
* *[USER]* The alicloud extension does now support shoot clusters with Kubernetes version 1.25. You should consider the [Kubernetes release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md) before upgrading to 1.25. (#537, @shafeeqes)
## 🐛 Bug Fixes
* *[USER]* The automatic enablement of no-overlay network configuration for new Shoots is now reverted. For more details about the motivation, see https://github.com/gardener/gardener-extension-provider-aws/issues/621. (#536, @ialidzhikov)
## 🏃 Others
* *[OPERATOR]* Adds a heartbeat controller that creates and renews a `Lease` resource named `gardener-extension-heartbeat` in the namespace where the extension controller is deployed. This `Lease` resource can be used by other controllers to check if the `provider-alicloud` extension controller is running. (#544, @AleksandarSavchev)
* *[OPERATOR]* Update golang version used to 1.19.1 (#535, @shafeeqes)
* *[OPERATOR]* The following images are updated: (#539, @shaoyongfeng)
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.2 -> v2.2.2 (for kubernetes < 1.20)
  * k8s.gcr.io/sig-storage/csi-provisioner: v2.1.2 -> v3.2.0 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-attacher: v3.3.0 -> v3.4.0
  * k8s.gcr.io/sig-storage/csi-resizer: v0.5.0 -> v1.5.0
  * k8s.gcr.io/sig-storage/csi-snapshotter: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-validation-webhook: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/snapshot-controller: v3.0.3 -> v4.2.1 (for kubernetes >= 1.20)
  * k8s.gcr.io/sig-storage/csi-node-driver-registrar: v1.3.0 -> v2.5.1
  * k8s.gcr.io/sig-storage/livenessprobe: v2.3.0 -> v2.7.0
* *[OPERATOR]* block traffic for Telnet and RSH ports (#541, @kevin-lacoo)
* *[OPERATOR]* scheduler.alpha.kubernetes.io/critical-pod annotation is removed as pod priority (spec.priorityClassName) is used instead to mark pods as critical (#543, @dimitar-kostadinov)
* *[DEPENDENCY]* Dependency `github.com/gardener/gardener` is updated `v1.56.0` -> `v1.59.0`. (#544, @AleksandarSavchev)
* *[DEPENDENCY]* The following dependency is updated: (#534, @shafeeqes)
  * github.com/gardener/gardener: v1.53.0 -> v1.56.0
  * k8s.io/* : v0.24.3 -> v0.25.0
  * sigs.k8s.io/controller-runtime: v0.12.1 -> v0.13.0