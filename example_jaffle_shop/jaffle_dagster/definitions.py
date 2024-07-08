import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from example_jaffle_shop.jaffle_dagster.assets import jaffle_shop_dbt_assets
from example_jaffle_shop.jaffle_dagster.constants import dbt_project_dir
from example_jaffle_shop.jaffle_dagster.schedules import schedules

defs = Definitions(
    assets=[jaffle_shop_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)
