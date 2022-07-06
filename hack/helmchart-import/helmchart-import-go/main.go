package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
    "sync"

	"github.com/sirupsen/logrus"
	flag "github.com/spf13/pflag"
	"gopkg.in/yaml.v3"
	"helm.sh/helm/v3/pkg/chart"
	"helm.sh/helm/v3/pkg/chartutil"
)

type configuration struct {
	Name       string   `yaml:"name"`
	Version    string   `yaml:"version"`
	Repo       string   `yaml:"repo"`
	Add_charts []string `yaml:"additionalCharts"`
}

func fetchChart(cfg configuration) ([]byte, error) {
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

func getChart(cfg configuration) chart.Chart {
	controller_registration, err := fetchChart(cfg)
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
			Name:        cfg.Name,
			Version:     cfg.Version,
			Description: "A helm chart for the controllerRegistration of " + cfg.Name,
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
    wg sync.WaitGroup
)

func init() {
	flag.StringVar(&configFile, "config", "conf.yml", "")
	flag.StringVar(&targetDir, "target", "charts", "")
}

func getAndSave(cfg configuration) {
  	    defer wg.Done()
		chart := getChart(cfg)
		chartutil.SaveDir(&chart, targetDir)
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
    wg.Add(len(config))
    fmt.Println("wg length: ",  len(config))

	for _, cfg := range config {
        go getAndSave(cfg)
	}
    wg.Wait()
}
