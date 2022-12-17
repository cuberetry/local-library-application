from mysql.connector import errors
import SQLScript.sql_get_pk as sql_get_pk


def sql_update(cursor, connection, table_name=str, primary_key=int, data_dict=dict):
    try:
        pk_col = sql_get_pk.sql_get_pk(cursor, table_name)
        for col in data_dict:
            cursor.execute(f"UPDATE {table_name} SET {col} = '{data_dict[col]}' WHERE {pk_col} = '{primary_key}'")
        connection.commit()
        return True
    except (errors.ProgrammingError, errors.IntegrityError, TypeError) as msg:
        print("ERROR", msg)
        return False
