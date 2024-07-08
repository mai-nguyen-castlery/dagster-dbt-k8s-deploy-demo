
# Demo: Deploy Dagster and dbt on Kubernetes with Helm

## Repository structure

### `dagster_home`

The `dagster_home` directory is a central location for Dagster's configuration, logs, and metadata.

**Key Components**

1. Configuration Files: Contains the `dagster.yaml` file and other configuration files.

2. Logs: Stores logs related to pipeline runs and events.

3. Metadata: Includes information about pipeline runs and instance-level settings.

**`dagster.yaml` file**

The `dagster.yaml` file [configures various aspects of Dagster's behavior](https://docs.dagster.io/deployment/dagster-instance) for its local instance. 

### example_jaffle_shop

`example_jaffle_shop` contains example codes for a Dagster code location and its corresponding dbt project. It is loaded into the Dagster UI and instance via the `workspace.local.yaml` file.
It also has a `Dockerfile` for building the Dagster docker image, which will be deployed to a Kubernetes cluster for the development and production environment.
The `requirements.txt` file in this folder includes the required Python dependencies. 

### env.example 

Example of .env file. This `.env` file is used to load the environment variables into local Dagster and VSCode.

Change the value of the environment variable `DAGSTER_HOME` to the absolute path to the `dagster_home` directory 

### dagster_helm_values.yaml

`dagster_helm_values.yaml` is used to configure the deployment of Dagster on Kubernetes using Helm, a package manager for Kubernetes. This file contains customizable values that Helm uses to generate the necessary Kubernetes resource configurations.

### environment.yml

The environment.yml file is used by Conda to define the environment configuration for this project. This file specifies the dependencies, Python version, and other packages that should be installed in the Conda environment.

### Makefile

The `Makefile` includes commands for creating, updating, and managing this project, such as creating / updating conda environment, launch Dagster local instance, publishing Docker images, etc. 

### workspace.local.yaml

The `workspace.local.yaml`  is used to define the code locations and repositories that Dagster should load when running locally.

## How to get Dagster running locally 

### Create a conda environment 

Full command:
```
mamba env create --file environment.yml
```
Makefile shortcut command:
```
make create-env 
```
This will create a conda environment with the name `dagster`. Set this environment as the Python interpreter for VSCode.

### Create .env file 

Copy the `.env.example` file and change its name to `.env`. Replace the value of `DAGSTER_HOME` key to the the absolute path to the `dagster_home` folder in your local machine. Change the values of the following credential keys, which is provided in the chat: 
```
JAFFLE_POSTGRES_HOST=HOST
JAFFLE_POSTGRES_USER=USER
JAFFLE_POSTGRES_PASSWORD=PASSWORD
JAFFLE_POSTGRES_PORT=5432
JAFFLE_POSTGRES_DB=DATABASE
```
### Run local Dagster 
Run the full command:
```
dagster dev -w workspace.local.yaml
```
Makefile shortcut:
```
make dagster-dev
```
