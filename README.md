# 23ke-charts

In this repository helm charts for the deployment of 23ke are stored.
Moreover, it serves as a helm repository managed by [helm/chart-releaser-action](https://github.com/helm/chart-releaser-action).
Thus, you can

``` shell
helm repo add 23ke-charts https://23technologies.github.io/23ke-charts
helm repo update
```

Then, you should be all set to install the helm charts via `helm install`.
