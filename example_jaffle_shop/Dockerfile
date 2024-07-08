ARG BASE_IMAGE

# Use a slim Python image as the base
FROM ${BASE_IMAGE}

ARG DAGSTER_VERSION
ARG DBT_CORE_VERSION

# Install git
RUN apt-get update && apt-get install -y git && apt-get clean
# Upgrade pip
RUN pip install --upgrade pip

# Install Dagster dependencies
# All packages are hard-pinned to `dagster`, so setting the version on just `dagster` will ensure
# compatible versions.
RUN pip install \
    dagster==${DAGSTER_VERSION} \
    dbt-core==${DBT_CORE_VERSION} \
    dagster-dbt \
    dagster-postgres \
    dagster-k8s \
    dagster-celery[flower,redis,kubernetes] \
    dagster-celery-k8s

# Set working directory
ENV WORK_DIR=/opt/dagster/app
WORKDIR ${WORK_DIR}

# Copy user-code 
COPY jaffle_dagster ${WORK_DIR}/example_jaffle_shop/jaffle_dagster
COPY jaffle_dagster_tests ${WORK_DIR}/example_jaffle_shop/jaffle_dagster_tests
COPY jaffle_dbt ${WORK_DIR}/example_jaffle_shop/jaffle_dbt
COPY requirements.txt ${WORK_DIR}/example_jaffle_shop/requirements.txt

# Set environment variable for dbt project directory
ENV DBT_PROJECT_DIR=${WORK_DIR}/example_jaffle_shop/jaffle_dbt

# Install required dependencies to run the user code
RUN pip install -r ${WORK_DIR}/example_jaffle_shop/requirements.txt

# Parse dbt project 
RUN dbt deps --project-dir ${DBT_PROJECT_DIR} --profiles-dir ${DBT_PROJECT_DIR}
RUN dbt clean --project-dir ${DBT_PROJECT_DIR} --profiles-dir ${DBT_PROJECT_DIR}
# RUN dbt parse --project-dir ${DBT_PROJECT_DIR} --profiles-dir ${DBT_PROJECT_DIR}
