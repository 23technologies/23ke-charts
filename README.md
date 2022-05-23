# 23ke-charts

In this repository helm charts for the deployment of 23ke are stored.
Moreover, it serves as a helm repository managed by [helm/chart-releaser-action](https://github.com/helm/chart-releaser-action).
Thus, you can

``` shell
helm repo add 23ke-charts https://23technologies.github.io/23ke-charts
helm repo update
```

Then, you should be all set to install the helm charts via `helm install`.

## How to add your own cloudprofile

If you want to add your own cloudprofile, head over to *charts/cloudprofiles/chart*.
Copy one of the existing folders and name the copy as desired. If you want to add an OpenStack based cloud, make sure to copy from another OpenStack based one to make things easier.
In *Chart.yaml* change the `name` parameter to the same name of the folder itself.
In *values.yaml* a lot more needs to be changed.
The `name` should be changed like the step before.
`machineImages` is mapped to the `providerConfig` further down below. Entries defined here become available in the Web-Dashboard as an operating system for your Shoots.
`machineTypes` define the available flavors for your nodes, the `name` attribute here is a mapping to the accoring flavor inside the cloud.
`regions` is a representation of regions and zones of the new cloud.
`providerConfig` is a direct mapping of resources provided from the new cloud, e.g. Images, URL Endpoints, etc. It's a good idea to just look into other existing profiles and adopt entries from them while changing the values accordingly.
Leave the rest of the files and folders untouched.
Finally, head over to *charts/cloudprofiles/values.yaml* and add your profile at the end of the file in the given pattern.
