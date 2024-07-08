# Define default values for variables
PYTHON_VERSION ?= 3.11
DAGSTER_VERSION ?= 1.7
DBT_CORE_VERSION ?= 1.8
EXAMPLE_IMAGE_NAME ?= dagster-example-jaffle-shop
PLATFORM ?= linux/amd64

create-env:
	mamba env create --file environment.yml

update-env:
	mamba env update --file environment.yml --prune

dagster-dev: 
	dagster dev -w workspace.local.yaml

example-dbt:
	dbt debug --project-dir ./example_jaffle_shop/jaffle_dbt --profiles-dir ./example_jaffle_shop/jaffle_dbt
	dbt deps --project-dir ./example_jaffle_shop/jaffle_dbt --profiles-dir ./example_jaffle_shop/jaffle_dbt
	dbt parse --project-dir ./example_jaffle_shop/jaffle_dbt --profiles-dir ./example_jaffle_shop/jaffle_dbt	

example-build:
	docker build -t ${EXAMPLE_IMAGE_NAME}:latest \
		--build-arg BASE_IMAGE=python:${PYTHON_VERSION}-slim \
		--build-arg DAGSTER_VERSION=${DAGSTER_VERSION} \
		--build-arg DBT_CORE_VERSION=${DBT_CORE_VERSION} \
		--platform ${PLATFORM} \
		-f ./example_jaffle_shop/Dockerfile ./example_jaffle_shop
	docker tag ${EXAMPLE_IMAGE_NAME}:latest janetvn/${EXAMPLE_IMAGE_NAME}:latest
	docker push janetvn/${EXAMPLE_IMAGE_NAME}:latest

example: example-dbt example-build

deploy-minikube: 
	helm upgrade --install dagster dagster/dagster -f dagster_helm_values.yaml --namespace dagster
	export DAGSTER_WEBSERVER_POD_NAME=$(kubectl get pods --namespace dagster -l "app.kubernetes.io/name=dagster,app.kubernetes.io/instance=dagster,component=dagster-webserver" -o jsonpath="{.items[0].metadata.name}")
	echo "Visit http://127.0.0.1:8080 to open the Dagster UI"
	kubectl --namespace dagster port-forward $${DAGSTER_WEBSERVER_POD_NAME} 8080:80
	