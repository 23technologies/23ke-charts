import glob
import re
import sys


def update_chart_version(filename, version):
    """ Rewrite the chart version"""
    with open(filename, "r") as f:
        content = f.read()
        content = re.sub("version:.*", "version: " + version, content, flags=re.M)

    with open(filename, "w") as f:
        f.write(content)


def update_charts(dir, fix_version):
    """search for all Chart.yaml files and invoke the update function"""
    charts = glob.glob(dir + "/**/Chart.yaml", recursive=True)
    for chart in charts:
        update_chart_version(chart, fix_version)


if __name__ == "__main__":
    try:
        update_charts(sys.argv[1], sys.argv[2])
    except:
        print(
            "Please specify a chart directory and a new version for the controlplane charts as commandline argument to this script\nExample usage:\n\tpython hack/helmchart-import/introduce-fix-version.py charts/gardener-controlplane* 1.41.2-fix.1"
        )
