#/usr/bin/env bash

git checkout latest-3
git checkout latest-2 hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit "Shift latest-2 version to latest-3"
git push

git checkout latest-2
git checkout latest-1 hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit "Shift latest-1 version to latest-2"
git push

git checkout latest-1
git checkout main hack/helmchart-import/import-gardener-charts.py
git add hack/helmchart-import/import-gardener-charts.py
git commit "Shift main version to latest-1"
git push
