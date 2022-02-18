import glob
import os
import re
import urllib
from urllib import request
from pathlib import Path

import ruamel.yaml
yaml = ruamel.yaml.YAML()


# here go our importet helmcharts
target_dir = "charts/extensions/"

# configure the charts you want to import here
# you need to define the package consiting of github-org/repo,
# the corresponding version, and src and dst directories
config = [
    {
        "package": "gardener/external-dns-management",
        "version": "v0.12.0",
        "name": "external-dns-management",
    },
    {
        "package": "gardener/gardener-extension-networking-calico",
        "version": "v1.23.0",
        "name": "networking-calico",
    },
    {
        "package": "gardener/gardener-extension-networking-cilium",
        "version": "v1.9.0",
        "name": "networking-cilium",
    },
    {
        "package": "gardener/gardener-extension-os-gardenlinux",
        "version": "v0.11.0",
        "name": "os-gardenlinux",
    },
    {
        "package": "gardener/gardener-extension-os-ubuntu",
        "version": "v1.14.0",
        "name": "os-ubuntu",
    },
    {
        "package": "gardener/gardener-extension-provider-alicloud",
        "version": "v1.32.0",
        "name": "provider-alicloud",
    },
    {
        "package": "gardener/gardener-extension-provider-aws",
        "version": "v1.33.1",
        "name": "provider-aws",
    },
    {
        "package": "gardener/gardener-extension-provider-azure",
        "version": "v1.25.0",
        "name": "provider-azure",
    },
    {
        "package": "gardener/gardener-extension-provider-gcp",
        "version": "v1.20.0",
        "name": "provider-gcp",
    },
    {
        "package": "23technologies/gardener-extension-provider-hcloud",
        "version": "v0.4.13",
        "name": "provider-hcloud",
    },
    {
        "package": "gardener/gardener-extension-provider-openstack",
        "version": "v1.23.3",
        "name": "provider-openstack",
    },
    {
        "package": "gardener/gardener-extension-shoot-cert-service",
        "version": "v1.20.0",
        "name": "shoot-cert-service",
    },
    {
        "package": "gardener/gardener-extension-shoot-dns-service",
        "version": "v1.17.0",
        "name": "extension-shoot-dns-service",
    },
]


def import_charts(config, target_dir):

    # Potentially, the controller-registration.yaml can be found at several places in github repos.
    # Therefore, we define a list with urls to try
    urls = [
        "https://raw.githubusercontent.com/"
        + config["package"]
        + "/"
        + config["version"]
        + "/examples/controller-registration.yaml",
        "https://raw.githubusercontent.com/"
        + config["package"]
        + "/"
        + config["version"]
        + "/example/controller-registration.yaml",
        "https://github.com/"
        + config["package"]
        + "/releases/download/"
        + config["version"]
        + "/controller-registration.yaml",
    ]
    
    # now let's fetch the yaml
    for url in urls:
        try:
            x = urllib.request.urlopen(url)
        except:
            pass
        else:
            break

    # assume that we have to documents in our yaml, which is commonly the case for controller-registration.yamls
    content = list(yaml.load_all(x))
    
    content[0]["providerConfig"]["values"] = None
    content[1]["spec"]["resources"] = None

    # setup the path for our target chart
    Path(target_dir + "templates/").mkdir(parents=True, exist_ok=True)
    outf = Path(target_dir + "templates/" + config["name"] + ".yaml")
    try:
        outf.unlink()
    except:
        pass

    # write the target chart including templating
    yaml.explicit_start = True
    with outf.open("a") as ofp:
        ofp.write("{{- if (index .Values " + '"' + config["name"] + '"' + ").enable }}\n")
        yaml.dump(content[0], ofp)
        ofp.write("{{- toYaml (index .Values " + '"' + config["name"] + '"' + ").values | nindent 4 }}\n")
        yaml.dump(content[1], ofp)
        ofp.write("{{- toYaml (index .Values " + '"' + config["name"] + '"' + ").resources | nindent 4 }}\n")
        ofp.write("{{- end }}")
                  
# call the import function for all elements in the config list
for cfg in config:
    import_charts(cfg, target_dir)

# increment the version number of the chart
chartf = Path(target_dir + "Chart.yaml")
chart = yaml.load(chartf)
current_version = semantic_version.Version(chart["version"])
current_version.patch += 1
chart["version"] = str(current_version)
yaml.dump(chart, chartf)
