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
        "version": "v0.11.4",
        "name": "external-dns-management",
    },
    {
        "package": "gardener/gardener-extension-networking-calico",
        "version": "v1.19.0",
        "name": "networking-calico",
    },
    {
        "package": "gardener/gardener-extension-networking-cilium",
        "version": "v1.8.0",
        "name": "networking-cilium",
    },
    {
        "package": "gardener/gardener-extension-os-gardenlinux",
        "version": "v0.11.0",
        "name": "os-gardenlinux",
    },
    {
        "package": "gardener/gardener-extension-os-ubuntu",
        "version": "v1.13.0",
        "name": "os-ubuntu",
    },
    {
        "package": "gardener/gardener-extension-provider-alicloud",
        "version": "v1.32.0",
        "name": "provider-alicloud",
    },
    {
        "package": "gardener/gardener-extension-provider-aws",
        "version": "v1.33.0",
        "name": "provider-aws",
    },
    {
        "package": "gardener/gardener-extension-provider-azure",
        "version": "v1.24.1",
        "name": "provider-azure",
    },
    {
        "package": "gardener/gardener-extension-provider-gcp",
        "version": "v1.20.0",
        "name": "provider-gcp",
    },
    {
        "package": "23technologies/gardener-extension-provider-hcloud",
        "version": "v0.4.8",
        "name": "provider-hcloud",
    },
    {
        "package": "gardener/gardener-extension-provider-openstack",
        "version": "v1.23.1",
        "name": "provider-openstack",
    },
    {
        "package": "gardener/gardener-extension-shoot-cert-service",
        "version": "v1.18.0",
        "name": "shoot-cert-service",
    },
    {
        "package": "gardener/gardener-extension-shoot-dns-service",
        "version": "v1.14.0",
        "name": "shoot-dns-service",
    },
]


def import_charts(cfg, target_dir):

    # Potentially, the controller-registration.yaml can be found at several places in github repos.
    # Therefore, we define a list with urls to try
    urls = [
        "https://raw.githubusercontent.com/"
        + cfg["package"]
        + "/"
        + cfg["version"]
        + "/examples/controller-registration.yaml",
        "https://raw.githubusercontent.com/"
        + cfg["package"]
        + "/"
        + cfg["version"]
        + "/example/controller-registration.yaml",
        "https://github.com/"
        + cfg["package"]
        + "/releases/download/"
        + cfg["version"]
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
    

    # setup the path for our target chart
    Path(target_dir + "templates/").mkdir(parents=True, exist_ok=True)
    outf = Path(target_dir + "templates/" + cfg["name"] + ".yaml")
    try:
        outf.unlink()
    except:
        pass

    # write the target chart including templating
    yaml.explicit_start = True
    with outf.open("a") as ofp:
        ofp.write("{{- if (index .Values " + '"' + cfg["name"] + '"' + ").enabled }}\n")
        yaml.dump(content[0], ofp)
        ofp.write("{{- if (index .Values " + '"' + cfg["name"] + '"' + ").values }}\n")
        ofp.write("{{- toYaml (index .Values " + '"' + cfg["name"] + '"' + ").values | nindent 4 }}\n")
        ofp.write("{{- end }}\n")

        yaml.dump(content[1], ofp)
        ofp.write("{{- if (index .Values " + '"' + cfg["name"] + '"' + ").resources}}\n")
        ofp.write("{{- toYaml (index .Values " + '"' + cfg["name"] + '"' + ").resources | nindent 2 }}\n")
        ofp.write("{{- end }}\n")
        ofp.write("{{- end }}\n")

def write_values_yaml(config, target_dir):

    outf = Path(target_dir + "values.yaml")
    try:
        outf.unlink()
    except:
        pass

    for cfg in config:
        # write a basic values.yaml
        content = {cfg["name"]: {"enabled": False, "values": {}, "resources": []}}
        yaml.explicit_start = False
        with outf.open("a") as ofp:
            yaml.dump(content, ofp)
            ofp.write("\n")

                  
# call the import function for all elements in the config list
for cfg in config:
    import_charts(cfg, target_dir)

# and write a starting point values.yaml
write_values_yaml(config,target_dir)

# lastly, increment the version number of the chart
chartf = Path(target_dir + "Chart.yaml")
chart = yaml.load(chartf)
current_version = semantic_version.Version(chart["version"])
current_version.patch += 1
chart["version"] = str(current_version)
yaml.dump(chart, chartf)
