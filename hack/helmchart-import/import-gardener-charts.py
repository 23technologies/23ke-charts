import shutil
import tempfile
import git
import glob
import re
import os
import sys

# this is the target directory for our imported helmcharts
target_dir = "charts/"

# configure the charts you want to import here
# you need to define the package consiting of github-org/repo,
# the corresponding version, and src and dst directories
config = [
    {
        "package": "gardener/gardener",
        "version": "v1.48.2",
        "dirs": [
            {
                "src": "charts/gardener/controlplane",
                "chart_name": "gardener-controlplane",
                "update_tag": True
            },
            {
                "src": "charts/gardener/gardenlet",
                "chart_name": "gardenlet",
                "update_tag": True 
            },
            {
                "src": "charts/gardener/controlplane/charts/runtime",
                "chart_name": "gardener-controlplane-runtime",
                "update_tag": True
            },
            {
                "src": "charts/gardener/controlplane/charts/application",
                "chart_name": "gardener-controlplane-application",
                "update_tag": True
            }
        ],
    },
    {
        "package": "gardener/garden-setup",
        "version": "3.26.0",
        "dirs": [
            {
                "src": "components/etcd/cluster/chart",
                "chart_name": "garden-etcd",
                "update_tag": False
            },
            {
                "src": "components/kube-apiserver/chart",
                "chart_name": "garden-kube-apiserver",
                "update_tag": False
            },
        ],
    },
    {
        "package": "gardener/dashboard",
        "version": "1.58.0",
        "dirs": [
            {
                "src": "charts/gardener-dashboard",
                "chart_name": "gardener-dashboard",
                "update_tag": True
            },
            {
                "src": "charts/identity",
                "chart_name": "identity",
                "update_tag": False
            }
        ],
    },
]


def update_chart_version(filename, version):
    """Update the chart version so that it matches the upstream versioning, i.e. the versioning of the repository, where the charts come from. Do not confuse with the upstream chart version, as this is not maintained at this point in time."""
    # in case our version contains a character like e.g. v1.0.3
    version = re.sub("[a-zA-Z]", "", version)
    with open(filename, "r") as f:
        content = f.read()
        content = re.sub("version:.*", "version: " + version, content, flags=re.M)

    with open(filename, "w") as f:
        f.write(content)

def update_image_tag(filename, version):
    """Update the chart version so that it matches the upstream versioning, i.e. the versioning of the repository, where the charts come from. Do not confuse with the upstream chart version, as this is not maintained at this point in time."""
    # in case our version contains a character like e.g. v1.0.3
    with open(filename, "r") as f:
        content = f.read()
        content = re.sub("tag:.*", "tag: " + version, content, flags=re.M)

    with open(filename, "w") as f:
        f.write(content)


def update_chart_name(filename, name):
    """Update the chart name so that it matches our naming convention, i.e. we define the names in this import script."""
    # in case our version contains a character like e.g. v1.0.3
    with open(filename, "r") as f:
        content = f.read()
        content = re.sub("name:.*", "name: " + name, content, flags=re.M)

    with open(filename, "w") as f:
        f.write(content)


def import_charts(config, target_dir):
    """Import the charts. I.e. Clone the repo. Loop over the defined directories. Move the files into the target_dir. Update the version."""

    # define some options for cloning and set the correct version
    multi_options = ["--depth 1", "--branch " + config["version"]]

    # construct the remote url and create a local temporary directory
    git_url = "https://github.com/" + config["package"]
    repo_dir = tempfile.mkdtemp("/")

    # clone the repo to the temp dir and copy the specified directories to the target directory
    git.Repo.clone_from(git_url, repo_dir, multi_options=multi_options)
    for dir in config["dirs"]:
        shutil.rmtree(target_dir + dir["chart_name"], ignore_errors=True)
        shutil.copytree(repo_dir + dir["src"], target_dir + dir["chart_name"])
        charts = glob.glob(
            target_dir + dir["chart_name"] + "/**/Chart.yaml", recursive=True
        )
        for chart in charts:
            update_chart_version(chart, config["version"])
        # the gardener-dashboard image tag needs to be set here. since we have a versioned release
        # we do not want to have a latest tag in the values.yaml
            if dir["update_tag"]:
                chart = chart.replace("Chart.yaml", "values.yaml")
                if os.path.exists(chart):
                    update_image_tag(chart, config["version"])
        charts = glob.glob(target_dir + dir["chart_name"] + "/Chart.yaml")
        for chart in charts:
            update_chart_name(chart, dir["chart_name"])

    # delete the temporary directory
    shutil.rmtree(repo_dir)


# call the import function for all elements in the config list
if len(sys.argv) == 2:
  if sys.argv[1] == "show_gardener_version":
    print(config[0]["version"])
else:
  for cfg in config:
        import_charts(cfg, target_dir)
