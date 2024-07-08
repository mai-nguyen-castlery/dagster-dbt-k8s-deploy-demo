import os
import time

import pandas as pd
from sqlalchemy import create_engine


def get_env_var(variable_name):
    if not os.getenv(variable_name):
        raise KeyError(f"{variable_name} environment variable is not set")
    return os.getenv(variable_name)


postgres_user = get_env_var("JAFFLE_POSTGRES_USER")
postgres_password = get_env_var("JAFFLE_POSTGRES_PASSWORD")
postgres_host = get_env_var("JAFFLE_POSTGRES_HOST")
postgres_port = get_env_var("JAFFLE_POSTGRES_PORT")
postgres_db = get_env_var("JAFFLE_POSTGRES_DB")

data = pd.read_csv("https://docs.dagster.io/assets/customers.csv")
data.to_csv("data", index=False, header=False)
# conn = psycopg2.connect(
#     dbname=postgres_db,
#     user=postgres_user,
#     password=postgres_password,
#     host=postgres_host,
#     port=postgres_port,
# )
# with conn.cursor() as c:
#     c.execute("create schema if not exists jaffle_shop")
#     create_table_sql = """
#         create table if not exists jaffle_shop.raw_customers (
#         id int4,
#         first_name text,
#         last_name text
#         )
#     """
#     c.execute(create_table_sql)
#     c.execute('TRUNCATE TABLE jaffle_shop.raw_customers') #Truncate the table in case you've already run the script before
#     copy_sql = '''
#         COPY jaffle_shop.raw_customers
#         FROM 'data.csv' --input full file path here. see line 46
#         DELIMITER ',' CSV;
#     '''
#     start_time = time.time()
#     c.execute(copy_sql)
#     conn.commit()
#     conn.close()
#     print("COPY duration: {} seconds".format(time.time() - start_time))

# import_sql = """
#     COPY jaffle_shop.raw_customers(id, first_name, last_name)
#     FROM 'data.csv'
#     DELIMITER ','
#     CSV HEADER
# """
