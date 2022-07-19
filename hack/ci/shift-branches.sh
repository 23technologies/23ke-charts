#/usr/bin/env bash

pip install -r hack/helmchart-import/requirements.txt

git config --global user.email "renovate@23technologies.cloud"
git config --global user.name "Renovate Bot"
# check whether a minor upgrade took place:
git checkout renovate/main-gardener
NEW_MINOR=$(python hack/helmchart-import/import-gardener-charts.py show_gardener_version | cut -d '.' -f 2)
git checkout main
OLD_MINOR=$(python hack/helmchart-import/import-gardener-charts.py show_gardener_version | cut -d '.' -f 2)
if [[ $OLD_MINOR == $NEW_MINOR ]]
then
    echo "Only patch-upgrade skipping this script..."
    exit 0
fi


## Adjust renovate config:
# attention: this script assumes that no major release is created.
git checkout renovate/main-gardener
LATEST_MINOR=$(python hack/helmchart-import/import-gardener-charts.py show_gardener_version | cut -d '.' -f 2)
LATEST_1_MINOR=$(( $LATEST_MINOR - 1 ))
export LATEST_1_REGEX="/^v1\.$LATEST_1_MINOR\..*$/"
LATEST_2_MINOR=$(( $LATEST_MINOR - 2 ))
export LATEST_2_REGEX="/^v1\.$LATEST_2_MINOR\..*$/"
LATEST_3_MINOR=$(( $LATEST_MINOR - 3 ))
export LATEST_3_REGEX="/^v1\.$LATEST_3_MINOR\..*$/"
yq eval -o=json -i '.packageRules[3].allowedVersions = env(LATEST_1_REGEX)' .github/renovate.json
yq eval -o=json -i '.packageRules[4].allowedVersions = env(LATEST_2_REGEX)' .github/renovate.json
yq eval -o=json -i '.packageRules[5].allowedVersions = env(LATEST_3_REGEX)' .github/renovate.json
git add .github/renovate.json
git commit -s -m "Update renovate.json to track Gardener 1.$LATEST_MINOR and its three predecessors"
git push

git checkout latest-3
git pull
git checkout latest-2
git pull
git checkout latest-1
git pull
git checkout main
git pull

## Update branches:
git checkout latest-3
git pull
#git checkout latest-2 hack/helmchart-import/import-gardener-charts.py
sed "18s/\"version\": \"v[0-9]*\.[0-9]*\.[0-9]*\",/\"version\": \"v1.$LATEST_3_MINOR.0\",/" hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit -s -m "Shift latest-2 version to latest-3"
git push

git checkout latest-2
git pull
#git checkout latest-1 hack/helmchart-import/import-gardener-charts.py
sed "18s/\"version\": \"v[0-9]*\.[0-9]*\.[0-9]*\",/\"version\": \"v1.$LATEST_2_MINOR.0\",/" hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit -s -m "Shift latest-1 version to latest-2"
git push

git checkout latest-1
git pull
#git checkout main hack/helmchart-import/import-gardener-charts.py
sed "18s/\"version\": \"v[0-9]*\.[0-9]*\.[0-9]*\",/\"version\": \"v1.$LATEST_1_MINOR.0\",/" hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit -s -m "Shift main version to latest-1"
git push
