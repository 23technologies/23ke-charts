import glob
import os
import re
import urllib
from urllib import request
from pathlib import Path
import semantic_version

import ruamel.yaml

yaml = ruamel.yaml.YAML()


# here go our importet helmcharts
target_dir = "charts/extensions/"

# make sure to rewrite the default values.yaml each time
outf = Path(target_dir + "values.yaml")
try:
    outf.unlink()
except:
    pass

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
        "version": "v1.11.0",
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
        "version": "v1.34.0",
        "name": "provider-alicloud",
    },
    {
        "package": "gardener/gardener-extension-provider-aws",
        "version": "v1.34.3",
        "name": "provider-aws",
    },
    {
        "package": "gardener/gardener-extension-provider-azure",
        "version": "v1.26.2",
        "name": "provider-azure",
    },
    {
        "package": "gardener/gardener-extension-provider-gcp",
        "version": "v1.21.3",
        "name": "provider-gcp",
    },
    {
        "package": "23technologies/gardener-extension-provider-hcloud",
        "version": "v0.4.16",
        "name": "provider-hcloud",
    },
    {
        "package": "gardener/gardener-extension-provider-openstack",
        "version": "v1.24.2",
        "name": "provider-openstack",
    },
    {
        "package": "gardener/gardener-extension-shoot-cert-service",
        "version": "v1.20.0",
        "name": "shoot-cert-service",
    },
    {
        "package": "gardener/gardener-extension-shoot-dns-service",
        "version": "v1.18.3",
        "name": "shoot-dns-service",
    },
]

def save_old_versions():
    versions = []
    for pkg in config:
        text_file = open("charts/extensions/templates/" + pkg["name"] + ".yaml", "r")
        text = text_file.read()
        x = re.search(r"\ \ \ \ \ \ tag:\ (.*)", text)
        pkg["old_version"] = x.group(1)

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

    # define a dictionary for writing the default values.yaml file
    default_values = {cfg["name"]: {"enabled": False, "values": {}}}

    # write the target chart including templating
    yaml.explicit_start = True
    with outf.open("a") as ofp:
        ofp.write("{{- if (index .Values " + '"' + cfg["name"] + '"' + ").enabled }}\n")
        yaml.dump(content[0], ofp)
        ofp.write("{{- if (index .Values " + '"' + cfg["name"] + '"' + ").values }}\n")
        ofp.write(
            "{{- toYaml (index .Values "
            + '"'
            + cfg["name"]
            + '"'
            + ").values | nindent 4 }}\n"
        )
        ofp.write("{{- end }}\n")

        # if we have a kind: Extension in our resources, we want to be able to set this
        # resource to globallyEnabled: true by helm templating
        # Therefore, Add a helm template for this option
        for resource in content[1]["spec"]["resources"]:
            for k, v in dict(resource).items():
                if (k, v) == ("kind", "Extension"):
                    resource["globallyEnabled"] = "HereOurHelmTemplateGoes"
                    default_values[cfg["name"]]["globallyEnabled"] = False
        yaml.dump(content[1], ofp)
        ofp.write("{{- end }}\n")

    # As we cannot write the helmtemplate with ruamel.yaml, we need to replace our previously
    # inserted string "HereOurHelmTemplateGoes" with the actual template
    with outf.open("r") as ofp:
        content = ofp.read()
        content = re.sub(
            "HereOurHelmTemplateGoes",
            "{{ (index .Values " + '"' + cfg["name"] + '"' + ").globallyEnabled }}",
            content,
            flags=re.M,
        )

    with outf.open("w") as ofp:
        ofp.write(content)

    # write the default values file
    outf = Path(target_dir + "values.yaml")
    yaml.explicit_start = False
    with outf.open("a") as ofp:
        yaml.dump(default_values, ofp)
        ofp.write("\n")


save_old_versions()
# call the import function for all elements in the config list
extensions_versions = "| Extension      |  Version | \n| ----------- | ----------- |\n"
for cfg in config:
    import_charts(cfg, target_dir)
    if cfg["old_version"] != cfg["version"]:
        version = "```" + cfg["old_version"] + " -> " + cfg["version"] + "```"
    else:
        version = "```" + cfg["version"] + "```"
    extensions_versions = extensions_versions + "|" + cfg["name"] + "|" + version + "|\n"

# lastly, increment the version number of the chart and list bundled versions
chartf = Path(target_dir + "Chart.yaml")
chart = yaml.load(chartf)
current_version = semantic_version.Version(chart["version"])
current_version.patch += 1
chart["version"] = str(current_version)
yaml.dump(chart, chartf)

versionsf = Path(target_dir + "VERSIONS.md")
text_file = open(versionsf, "w")
text_file.write(extensions_versions)
text_file.close()

