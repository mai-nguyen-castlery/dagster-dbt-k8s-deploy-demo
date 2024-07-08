"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""

from dagster_dbt import build_schedule_from_dbt_selection

from example_jaffle_shop.jaffle_dagster.assets import jaffle_shop_dbt_assets

schedules = [
    build_schedule_from_dbt_selection(
        [jaffle_shop_dbt_assets],
        job_name="materialize_dbt_models",
        cron_schedule="0 10 * * *",
        dbt_select="fqn:*",
    ),
]
