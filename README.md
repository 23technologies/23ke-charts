# 23ke-charts

## :warning: **This repository is not further maintained** :warning:

### However,
we will continue to maintain and release Gardener charts in the following Git repositories:
* [Gardener chart releaser](https://github.com/gardener-community/gardener-chart-releaser)
* [Gardener charts](https://github.com/gardener-community/gardener-charts)
* [Cloudprofiles](https://github.com/gardener-community/cloudprofiles)
* [Etcd](https://github.com/gardener-community/etcd)
* [Garden-Kube-Apiserver](https://github.com/gardener-community/garden-kube-apiserver)

The corresponding helm repository can be found at gardener-community.github.io/gardener-charts and added to the helm repo list by: 
``` shell
helm repo add gardener-community-charts https://gardener-community.github.io/gardener-charts
helm repo update
```

### Depreciation plan for this repo
We will keep the automatic release process running for another few months. Consequently, new releases of the charts are expected to appear here for a while. We plan to switch off all bots supporting the release cycle by the end of November 2022. Therefore, we encourage every user of this repo to switch to the [Gardener Communitiy](https://github.com/gardener-community/) repositories.
