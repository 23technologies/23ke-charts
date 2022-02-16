import shutil
import tempfile
import git
import glob
import re

# here go our importet helmcharts
target_dir = "charts/"
shutil.rmtree(target_dir, ignore_errors=True)

# configure the charts you want to import here
# you need to define the package consiting of github-org/repo,
# the corresponding version, and src and dst directories
config = [
    {
        "package": "gardener/gardener",
        "version": "v1.38.2",
        "dirs": [
            {"src": "charts/gardener/controlplane", "dst": "gardener-controlplane"},
            {"src": "charts/gardener/gardenlet", "dst": "gardenlet"},
        ],
    },
    {
        "package": "gardener/garden-setup",
        "version": "3.19.0",
        "dirs": [
            {"src": "components/etcd/cluster/chart", "dst": "garden-etcd"},
            {"src": "components/kube-apiserver/chart", "dst": "kube-apiserver"},
        ],
    },
    {
        "package": "gardener/dashboard",
        "version": "1.52.3",
        "dirs": [
            {"src": "charts/gardener-dashboard", "dst": "gardener-dashboard"},
            {"src": "charts/identity", "dst": "identity"},
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
        shutil.copytree(repo_dir + dir["src"], target_dir + dir["dst"])
        charts = glob.glob(target_dir + dir["dst"] + "/**/Chart.yaml", recursive=True)
        for chart in charts:
            update_chart_version(chart, config["version"])

    # delete the temporary directory
    shutil.rmtree(repo_dir)


# call the import function for all elements in the config list
for cfg in config:
    import_charts(cfg, target_dir)
