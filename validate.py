#!/usr/bin/env python
import sqlalchemy as sql
#get credentials
engine = sql.create_engine =(
    'snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}?warehouse=WAREHOUSE_NAME&role=ROLENAME'.format(
        user='<username>',
        password='<password>',
        role_name='<ROLE_NAME>',
        account_identifier='<account_identifier>',
        warehouse_name='<WAREHOUSE_NAME>',
        database_name='<DATABASE_NAME>',
        schema_name='<SCHEMA_NAME>'
    )
)
#connect engine
try:
    connection = engine.connect()
    results = engine.connect().execute('select current_version()').fetchone()
    print(results[0])
finally:
    connection.close()
    engine.dispose()
