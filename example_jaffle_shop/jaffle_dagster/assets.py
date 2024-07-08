import os

import pandas as pd
from dagster import OpExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from sqlalchemy import create_engine

from example_jaffle_shop.jaffle_dagster.constants import dbt_manifest_path


@dbt_assets(manifest=dbt_manifest_path)
def jaffle_shop_dbt_assets(context: OpExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
