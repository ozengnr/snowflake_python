#!/usr/bin/env python
import sqlalchemy as sql
#get credentials
engine = sql.create_engine =(
    'snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}?warehouse=FIVETRAN_WAREHOUSE&role=ACCOUNTADMIN'.format(
        user='oguner',
        password='c2QbecJwfsKzYPGL',
        role_name='ACCOUNTADMIN',
        account_identifier='ms77939.us-east-2.aws',
        warehouse_name='FIVETRAN_WAREHOUSE',
        database_name='PI_ENGAGEMENT_DB',
        schema_name='PENDO'
    )
)

try:
    connection = engine.connect()
    results = engine.connect().execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()