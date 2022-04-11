import glob
import re
import argparse
import sys


def update_chart_version(filename, version):

    with open(filename, "r") as f:
        content = f.read()
        content = re.sub("version:.*", "version: " + version, content, flags=re.M)

    with open(filename, "w") as f:
        f.write(content)


def update_charts(fix_version):
    for dir in [
        "charts/gardener-controlplane",
        "charts/gardener-controlpane-application",
        "charts/gardener-controlplane-runtime",
    ]:
        charts = glob.glob(dir + "/**/Chart.yaml", recursive=True)
        for chart in charts:
            update_chart_version(chart, fix_version)


if __name__ == "__main__":
    try:
        update_charts(sys.argv[1])
    except:
        print(
            "Please specify a new version for the controlplane charts as commandline argument to this script"
        )
