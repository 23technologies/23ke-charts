package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"

	getter "github.com/hashicorp/go-getter"
	"gopkg.in/yaml.v3"
	"helm.sh/helm/v3/pkg/chart"
	"helm.sh/helm/v3/pkg/chart/loader"
	"helm.sh/helm/v3/pkg/chartutil"
)

type configuration struct {
	Name       string   `yaml:"name"`
	Version    string   `yaml:"version"`
	Repo       string   `yaml:"repo"`
	Add_charts []string `yaml:"additionalCharts"`
}

func import_additional_charts(cfg configuration) []*chart.Chart {

	var result []*chart.Chart
	for _, path := range cfg.Add_charts {
		os.RemoveAll("tmp")
		getter.Get("tmp", "github.com/"+cfg.Repo+"?ref="+cfg.Version+"//"+path)

		add_chart, err := loader.Load("tmp")
		if err != nil {
			fmt.Println(err)
		}
		result = append(result, add_chart)
	}
	return result
}

func ensure_chart(c *chart.Chart) {

	c.Metadata.APIVersion = "v2"
	if len(c.Dependencies()) == 0 {
		return
	}

	for _, dep := range c.Dependencies() {
		cur_dep := chart.Dependency{
			Name:      dep.Name(),
			Version:   dep.Metadata.Version,
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
		
		ensure_chart( dep )
	}

}

func generate_controller_chart(cfg configuration) chart.Chart {

	urls := [3]string{
		"https://raw.githubusercontent." + cfg.Repo + "/" + cfg.Version + "/examples/controller-registration.yaml",
		"https://raw.githubusercontent.com/" + cfg.Repo + "/" + cfg.Version + "/example/controller-registration.yaml",
		"https://github.com/" + cfg.Repo + "/releases/download/" + cfg.Version + "/controller-registration.yaml",
	}

	// download flux install.yaml
	client := http.Client{
		CheckRedirect: func(r *http.Request, via []*http.Request) error {
			r.URL.Opaque = r.URL.Path
			return nil
		},
	}

	var controller_registration []byte
	for _, url := range urls {
		resp, err := client.Get(url)
		if err != nil {
			continue
		}

		controller_registration, err = ioutil.ReadAll(resp.Body)
		defer resp.Body.Close()
		break
	}

	// add a helm template for values in the ControllerDeployment part of the chart
	controller_registration_as_string := string(controller_registration)
	controller_registration_split := strings.Split(controller_registration_as_string, "---")
	for i := range controller_registration_split {
		if strings.Contains(controller_registration_split[i], "ControllerDeployment") {
			controller_registration_split[i] +=  `{{- if .Values.values }}
{{- toYaml .Values.values | nindent 4 }}
{{- end }}
`
		}
	}
	
	controller_registration = []byte(strings.Join(controller_registration_split, "---"))

	var values = make(map[string]interface{})
	values["values"] = map[string]interface{}{}
	values_serialized, _ := yaml.Marshal(values)

	controller_chart := chart.Chart{
		Metadata: &chart.Metadata{
			Name:        "controller",
			Version:     "v0.0.1", // make this static here, versioning is handeled on the upper level
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

func generate_chart(cfg configuration) chart.Chart {
	cur_chart := chart.Chart{
		Metadata: &chart.Metadata{
			Name:        cfg.Name,
			Version:     cfg.Version,
			Description: "A helmchart for" + cfg.Name,
			APIVersion:  "v2",
		},
	}
	return cur_chart
}

func main() {

	// parse the configuration
	data, err := ioutil.ReadFile("config.yaml")
	if err != nil {
		fmt.Println(err)
	}
	var config []configuration
	err = yaml.Unmarshal(data, &config)

	// define the main extension chart
	extension_chart := chart.Chart{
		Metadata: &chart.Metadata{
			Name:        "extensions",
			Version:     "v0.0.1",
			Description: "A helmchart for Gardener extensions",
			APIVersion:  "v2",
		},
	}

	for _, cfg := range config {
		// First, we generate the current chart
		cur_chart := generate_chart(cfg)

		// now let's generate the chart containing the controller-registration
		// and set it as dependency
		controller_chart := generate_controller_chart(cfg)
		cur_chart.AddDependency(&controller_chart)
		
		// import additional charts.
		// most probably, these are the charts containing the admission controllers for provider extensions
		add_charts := import_additional_charts(cfg)
		for _, add_chart := range(add_charts){
			cur_chart.AddDependency(add_chart)
		}
		
		// set the current sub-chart as dependency for the entire extensions chart
		extension_chart.AddDependency(&cur_chart)
	}

	// make sure that all charts are set to APIversion=v2
	// and every subchart is disabled by default
	ensure_chart(&extension_chart)
	chartutil.SaveDir(&extension_chart, ".")

}
