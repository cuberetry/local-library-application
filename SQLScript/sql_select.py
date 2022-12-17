from mysql.connector import errors


def sql_select(cursor, table_name=str, fields=None):
    try:
        if fields:
            if isinstance(fields, tuple) or isinstance(fields, set) or isinstance(fields, list):
                fields = ", ".join(fields)
            cursor.execute(f"SELECT {fields} FROM {table_name}")
        else:
            cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    except (errors.ProgrammingError, TypeError) as msg:
        print("ERROR", msg)
        return None
