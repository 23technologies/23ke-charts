package main

import (
	"context"
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"sort"
	"strings"

	semver "github.com/Masterminds/semver/v3"
	"github.com/akrennmair/slice"
	git "github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
	"github.com/google/go-github/v45/github"
	"github.com/sirupsen/logrus"
	flag "github.com/spf13/pflag"
	"gopkg.in/yaml.v3"
	"helm.sh/helm/v3/pkg/chart"
	"helm.sh/helm/v3/pkg/chart/loader"
	"helm.sh/helm/v3/pkg/chartutil"
)

type configuration struct {
	Name       string   `yaml:"name"`
	Version    string   `yaml:"version"`
	Repo       string   `yaml:"repo"`
	Charts []string `yaml:"charts"`
}


func getReleasesToTrack(cfg configuration) error {
	client := github.NewClient(nil)
	owner := strings.Split(cfg.Repo, "/")[0]
	repo := strings.Split(cfg.Repo, "/")[1]

	// most probably the last 20 upstreamReleases will contain everything we need
	upstreamReleases, _, _ := client.Repositories.ListReleases(context.Background(),
		owner,
		repo,
		&github.ListOptions{
			Page:    0,
			PerPage: 20,
	})

	// get and sort upstream release versions
	upstreamReleaseVersions := make([]*semver.Version, len(upstreamReleases))
	for i, r := range upstreamReleases {
		v, err := semver.NewVersion(r.GetTagName())
		if err != nil {
			return err
		}
		upstreamReleaseVersions[i] = v
	}
	sort.Sort(semver.Collection(upstreamReleaseVersions))


	maxMinor := upstreamReleaseVersions[len(upstreamReleaseVersions) - 1].Minor()
	maxMinorMinus3 := maxMinor - 3

	upstreamReleaseVersions = slice.Filter(upstreamReleaseVersions, (func(v *semver.Version) bool { return v.Minor() >= maxMinorMinus3 }))

	// As we release all charts in the 23ke-charts repo, we need to list way more releases.
	// Let's take the last 300 for now
	ourReleases := make([]*github.RepositoryRelease, 300)
	for i:=1; i<=3; i++ {
		pageReleases, _, _ := client.Repositories.ListReleases(context.Background(),
			"23technologies",
			"23ke-charts",
			&github.ListOptions{
				Page:    i,
				PerPage: 100,
			})
		ourReleases = append(ourReleases, pageReleases...)
	}

	ourReleases = slice.Filter(ourReleases, (func(r *github.RepositoryRelease) bool {
		return strings.Contains(r.GetName(), cfg.Name)
	}))


	ourReleaseVersions := slice.Map(ourReleases, func(r *github.RepositoryRelease) *semver.Version {
		vAsStringSlice := strings.Split(r.GetTagName(), "-")
		v, _ := semver.NewVersion(vAsStringSlice[len(vAsStringSlice) - 1])
		return v
	})


	// Now, filter out all version we have on our side.
	// If upstreamReleaseVersions is not empty afterwards,
	// we need to generate releases for these versions
	for _, ver := range(ourReleaseVersions) {
		upstreamReleaseVersions = slice.Filter(upstreamReleaseVersions, (func(v *semver.Version) bool {
			return !v.Equal(ver)
		}))
	}

	return nil

}


func fetchControllerRegistration(cfg configuration) ([]byte, error) {
	var controller_registration []byte
	urls := [3]string{
		"https://raw.githubusercontent.com/" + cfg.Repo + "/" + cfg.Version + "/examples/controller-registration.yaml",
		"https://raw.githubusercontent.com/" + cfg.Repo + "/" + cfg.Version + "/example/controller-registration.yaml",
		"https://github.com/" + cfg.Repo + "/releases/download/" + cfg.Version + "/controller-registration.yaml",
	}

	for _, url := range urls {
		resp, err := http.Get(url)
		if err == nil {
			if resp.StatusCode == 200 {
				defer resp.Body.Close()
				controller_registration, err = ioutil.ReadAll(resp.Body)
				if err == nil {
					// Download was sucessful, return content
					logrus.Info("Successfully fetched chart for ", cfg.Name, " URL: ", url)
					return controller_registration, nil
				}
			}
		}
	}
	return nil, errors.New("Was not able to fetch chart for " + cfg.Name)
}


func writeReleaseNotes(cfg configuration, targetDir string) {
	client := github.NewClient(nil)
	rr, _, _ := client.Repositories.GetReleaseByTag(context.Background(), strings.Split(cfg.Repo, "/")[0], strings.Split(cfg.Repo, "/")[1], cfg.Version)

	file, err := os.Create(targetDir + "/" + cfg.Name + "/RELEASE.md")
	if err != nil {
		logrus.Error("Error while writing Release notes to" + file.Name())
	}
	file.WriteString(*rr.Body)

}

func generateExtensionChart(cfg configuration) chart.Chart {
	controller_registration, err := fetchControllerRegistration(cfg)
	if err != nil {
		logrus.Warn(err.Error())
	}
	// add a helm template for values in the ControllerDeployment part of the chart
	controller_registration_as_string := string(controller_registration)
	controller_registration_split := strings.Split(controller_registration_as_string, "---")
	for i := range controller_registration_split {
		if strings.Contains(controller_registration_split[i], "ControllerDeployment") {
			controller_registration_split[i] += `{{- if .Values.values }}
{{- toYaml .Values.values | nindent 4 }}
{{- end }}
`
		}
	}

	controller_registration = []byte(strings.Join(controller_registration_split, "---"))

	// to create an empty values file:
	var values = make(map[string]interface{})
	values["values"] = map[string]interface{}{}
	values_serialized, _ := yaml.Marshal(values)

	controller_chart := chart.Chart{
		Metadata: &chart.Metadata{
			Name:        "controller",
			Version:     cfg.Version,
			Description: "Helmchart for controllerregistration of " + cfg.Name,
			APIVersion:  "v2",
		},
		Values: values,
		Raw: []*chart.File{{
			Name: "values.yaml",
			Data: values_serialized,
		}},
		Templates: []*chart.File{{
			Name: "templates/controller-registration.yaml",
			Data: controller_registration,
		}},
	}

	return controller_chart

}

var (
	configFile string
	targetDir  string
)

func init() {
	flag.StringVar(&configFile, "config", "conf.yml", "")
	flag.StringVar(&targetDir, "target", "charts", "")
}


func importChart(cfg configuration, src string) chart.Chart {

	logrus.Info("Starting Chart import from ", cfg.Repo, " Version: ", cfg.Version)
	tempRepoDir := "/tmp/" + cfg.Repo + "/"
	_, err := git.PlainClone(tempRepoDir, false, &git.CloneOptions{
		URL:               "https://github.com/" + cfg.Repo,
		ReferenceName:     plumbing.NewTagReferenceName(cfg.Version),
		SingleBranch:      true,
		Depth:             1,
		Progress:          os.Stdout,
	})
	if err != nil {
		fmt.Println(err)
	}


	// I did not find any package handling the symlinks to directories,
	// so that the directories are copied over
	// Therefore, just use a system command here
	tempDir := "tmp"
	
	_, err = exec.Command("cp", "-Lr", tempRepoDir + src, tempDir).Output()
	if err != nil {
		fmt.Println(err)
	}

	resultChart, err := loader.Load(tempDir)
	if err != nil {
		fmt.Println(err)
	}
	os.RemoveAll(tempDir)
	resultChart.Metadata.Version = cfg.Version

	return *resultChart
}


func ensureChart(c *chart.Chart) {

	c.Metadata.APIVersion = "v2"
	if len(c.Dependencies()) == 0 {
		return
	}

	for _, dep := range c.Dependencies() {
		cur_dep := chart.Dependency{
			Name:      dep.Name(),
			Condition: dep.Name() + ".enabled",
			Enabled:   false,
		}
		c.Metadata.Dependencies = append(c.Metadata.Dependencies, &cur_dep)

		if c.Values == nil {
			c.Values = make(map[string]interface{})
		} 
		c.Values[dep.Name()] = map[string]bool{"enabled": false}

		values_serialized, _ := yaml.Marshal(c.Values)
		c.Raw = []*chart.File{{
			Name: "values.yaml",
			Data: values_serialized,
		}}
		
		ensureChart( dep )
	}

}


func getAndSaveCharts(cfg configuration) {

	var mainChart chart.Chart

	// We need to generate a new Chart, when controller-registrations are involved, as extension
	// controllers are not packaged as charts by upstream
	generateNewChart := false
	for _, src := range(cfg.Charts) {
		if src == "controller-registration" {
			generateNewChart = true
		}
		break
	}
	
	if generateNewChart {
		mainChart = chart.Chart{
			Metadata: &chart.Metadata{
				Name:        cfg.Name, 
				Version:     cfg.Version,
				Description: "A helmchart for " + cfg.Name,
				APIVersion:  "v2",
			},
		}
		
		// if src equals "controller-registration", we need to generate the Chart for
		// the controller of an extension
		for _, src := range cfg.Charts {
			subChart := new(chart.Chart)
			if src == "controller-registration" {
				*subChart = generateExtensionChart(cfg)
			} else {
				*subChart = importChart(cfg, src)
			}
			mainChart.AddDependency(subChart)
		}
		
	} else {
		// here we assume that the chart is already packaged appropriately by upstream
		mainChart = importChart(cfg, cfg.Charts[0])
	}

	// ensureChart makes sure that the chart dependencies are set correctly
	mainChart.Metadata.Name = cfg.Name
	ensureChart(&mainChart)	
	chartutil.SaveDir(&mainChart, targetDir)
	writeReleaseNotes(cfg, targetDir)
}

func main() {
	logrus.Info("Helmchart importer started")

	flag.Parse()
	if _, err := os.Stat(configFile); err == os.ErrNotExist {
		logrus.Fatal("Config file not found")
		flag.PrintDefaults()
		return
	}
	// parse the configuration
	data, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		fmt.Println(err)
	}
	var config []configuration
	err = yaml.Unmarshal(data, &config)
	if err != nil {
		panic(err)
	}

	for _, cfg := range config {
		getAndSaveCharts(cfg)
	}

}
