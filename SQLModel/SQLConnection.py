import mysql.connector


class SQLConnection:
    def __init__(self, host=str, port=str, user=str, schema_name=str, reset=False):
        self.connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user
        )
        self.cursor = self.connection.cursor()
        self.schema_name = schema_name
        if reset:
            self.sql_execute("./SQLScript/sql_init.sql")
        self.cursor.execute(f"USE {self.schema_name}")

    def sql_get_pk(self, table_name):
        self.cursor.execute("SELECT COLUMN_NAME "
                            "FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
                            f"WHERE TABLE_SCHEMA = '{self.schema_name}' "
                            "AND CONSTRAINT_NAME = 'PRIMARY' "
                            f"AND TABLE_NAME = '{table_name}';")
        return self.cursor.fetchone()[0]

    def sql_execute(self, filename):
        fd = open(filename, 'r')
        sql_file = fd.read()
        fd.close()
        sql_commands = sql_file.split(';')

        for command in sql_commands:
            try:
                if command.strip() != '':
                    self.cursor.execute(command)
            except IOError as msg:
                print("Command skipped: ", msg)

    def sql_select(self, table_name=str, fields=None):
        try:
            if fields:
                if isinstance(fields, tuple) or isinstance(fields, set) or isinstance(fields, list):
                    fields = ", ".join(fields)
                self.cursor.execute(f"SELECT {fields} FROM {table_name}")
            else:
                self.cursor.execute(f"SELECT * FROM {table_name}")
            return self.cursor.fetchall()
        except (mysql.connector.errors.ProgrammingError, TypeError) as msg:
            print("ERROR", msg)
            return False

    def sql_insert(self, table_name=str, data_dict=dict):
        try:
            key_list = []
            value_list = []
            for col in data_dict:
                key_list.append(col)
                value_list.append(data_dict[col])
            key_list = ", ".join(key_list)
            self.cursor.execute(f"INSERT INTO {table_name} ({key_list}) VALUES {tuple(value_list)}")
            self.connection.commit()
            return True
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.IntegrityError, TypeError) as msg:
            print("ERROR", msg)
            return False

    def sql_update(self, table_name=str, primary_key=int, data_dict=dict):
        try:
            pk_col = self.sql_get_pk(table_name)
            for col in data_dict:
                self.cursor.execute(f"UPDATE {table_name} SET {col} = '{data_dict[col]}' WHERE {pk_col} = '{primary_key}'")
            self.connection.commit()
            return True
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.IntegrityError, TypeError) as msg:
            print("ERROR", msg)
            return False

    def sql_delete(self, table_name=str, primary_key=int):
        try:
            pk_col = self.sql_get_pk(table_name)
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {pk_col} = {primary_key}")
            self.connection.commit()
            return True
        except mysql.connector.errors.ProgrammingError as msg:
            print("ERROR", msg)
            return False
