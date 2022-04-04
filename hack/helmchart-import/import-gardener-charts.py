import shutil
import tempfile
import git
import glob
import re

# here go our importet helmcharts
target_dir = "charts/"

# configure the charts you want to import here
# you need to define the package consiting of github-org/repo,
# the corresponding version, and src and dst directories
config = [
    {
        "package": "gardener/gardener",
        "version": "v1.43.2",
        "dirs": [
            {
                "src": "charts/gardener/controlplane",
                "chart_name": "gardener-controlplane",
            },
            {"src": "charts/gardener/gardenlet", "chart_name": "gardenlet"},
            {"src": "charts/gardener/controlplane/charts/runtime", "chart_name": "gardener-controlplane-runtime"},
            {"src": "charts/gardener/controlplane/charts/application", "chart_name": "gardener-controlplane-application"},
        ],
    },
    {
        "package": "gardener/garden-setup",
        "version": "3.21.0",
        "dirs": [
            {"src": "components/etcd/cluster/chart", "chart_name": "garden-etcd"},
            {
                "src": "components/kube-apiserver/chart",
                "chart_name": "garden-kube-apiserver",
            },
        ],
    },
    {
        "package": "gardener/dashboard",
        "version": "1.55.0",
        "dirs": [
            {"src": "charts/gardener-dashboard", "chart_name": "gardener-dashboard"},
            {"src": "charts/identity", "chart_name": "identity"},
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
        charts = glob.glob(target_dir + dir["chart_name"] + "/Chart.yaml")
        for chart in charts:
            update_chart_name(chart, dir["chart_name"])

    # delete the temporary directory
    shutil.rmtree(repo_dir)


# call the import function for all elements in the config list
for cfg in config:
    import_charts(cfg, target_dir)
