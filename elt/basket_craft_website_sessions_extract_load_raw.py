"""
1. Import necessary libraries.
2. Load source MySQL and destination Postgres connection details.
3. Build connection strings and create database engines.
4. Read website_sessions for Dec 2023 from MySQL into a DataFrame.
5. Write DataFrame to website_sessions table in Postgres (raw schema).
"""

# %%
# Import necessary libraries
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# %%
# Load environment variables from .env file
load_dotenv()

# %%
# MySQL database connection details
mysql_user     = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_host     = os.environ['MYSQL_HOST']
mysql_db       = os.environ['MYSQL_DB']

# Postgres database connection details
pg_user     = os.environ['PG_USER']
pg_password = os.environ['PG_PASSWORD']
pg_host     = os.environ['PG_HOST']
pg_db       = os.environ['PG_DB']

# %%
# Build connection strings
mysql_conn_str = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}'
pg_conn_str    = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}/{pg_db}'

# %%
# Create database engines
mysql_engine = create_engine(mysql_conn_str)
pg_engine    = create_engine(pg_conn_str)

# %%
# Read only December 2023 sessions from MySQL
query = """
SELECT *
FROM website_sessions
WHERE created_at >= '2023-12-01'
  AND created_at <  '2024-01-01'
"""
df = pd.read_sql(query, mysql_engine)

# %%
# Write DataFrame to website_sessions table in Postgres (raw schema)
df.to_sql(
    'website_sessions',
    pg_engine,
    schema='raw',
    if_exists='replace',
    index=False
)

print(f'{len(df)} records loaded into raw.website_sessions.')

# %%
df
# %%
