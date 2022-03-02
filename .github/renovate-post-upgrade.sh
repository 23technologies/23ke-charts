#!/usr/bin/env bash

# First, find out which file has been changed:

CHANGED_FILE=$(git status -s)

if echo "$CHANGED_FILE" | grep "import-gardener-charts.py"
then
    # looks like gardener-core has been updated, import charts:
    echo 'cd /tmp/renovate/repos/github/23technologies/23ke-charts' > /tmp/tmpscript
    echo 'git status -s' >> /tmp/tmpscript
    echo 'pip install -r hack/helmchart-import/requirements.txt' >> /tmp/tmpscript
    echo 'python3 hack/helmchart-import/import-gardener-charts.py' >> /tmp/tmpscript
    echo 'git apply hack/helmchart-import/patches/*.patch' >> /tmp/tmpscript
    echo "chmod -R 777 /tmp/renovate/repos/github/23technologies/23ke-charts" >> /tmp/tmpscript
    mv /tmp/tmpscript /tmp/scripts/renovate-post-upgrade-script
fi
until test ! -f /tmp/scripts/renovate-post-upgrade-script
do
    echo "Importing gardener charts..."
    sleep 1
done
if echo "$CHANGED_FILE" | grep "import-gardener-extension-charts.py"
then
    # looks like gardener-extensions has been updated, import charts:
    echo 'cd /tmp/renovate/repos/github/23technologies/23ke-charts' > /tmp/tmpscript
    echo 'git status -s' >> /tmp/tmpscript
    echo 'pip install -r hack/helmchart-import/requirements.txt' >> /tmp/tmpscript
    echo 'python3 hack/helmchart-import/import-gardener-extension-charts.py' >> /tmp/tmpscript
    echo 'git apply hack/helmchart-import/patches/*.patch' >> /tmp/tmpscript
    echo "chmod -R 777 /tmp/renovate/repos/github/23technologies/23ke-charts" >> /tmp/tmpscript
    mv /tmp/tmpscript /tmp/scripts/renovate-post-upgrade-script
fi
until test ! -f /tmp/scripts/renovate-post-upgrade-script
do
    echo "Importing gardener exetensionexetension  charts..."
    sleep 1
done
exit 0

