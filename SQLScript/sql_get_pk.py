def sql_get_pk(cursor, table_name, schema_name='Local_Library_Schema'):
    cursor.execute("SELECT COLUMN_NAME "
                   "FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
                   f"WHERE TABLE_SCHEMA = '{schema_name}' "
                   "AND CONSTRAINT_NAME = 'PRIMARY' "
                   f"AND TABLE_NAME = '{table_name}';")
    return cursor.fetchone()[0]
