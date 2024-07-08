import os
from pathlib import Path

from dagster_dbt import DbtCliResource

dbt_project_dir = Path(__file__).joinpath("..", "..").resolve().joinpath("jaffle_dbt")

dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    # # Check dbt configuration with dbt debug
    # dbt.cli(["--quiet", "debug"]).wait()

    # # Update dbt package configuration
    # dbt.cli(["--quiet", "deps"]).wait()

    # Parse dbt project
    dbt_manifest_path = (
        dbt.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        )
        .wait()
        .target_path.joinpath("manifest.json")
    )
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")
    if os.path.exists(dbt_manifest_path) is False:
        dbt.cli(
            ["--quiet", "parse"],
            target_path=Path("target"),
        ).wait()
