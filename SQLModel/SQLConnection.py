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

    def sql_get_table(self):
        self.cursor.execute("SELECT DISTINCT TABLE_NAME FROM"
                            " information_schema.TABLE_CONSTRAINTS"
                            " WHERE CONSTRAINT_SCHEMA = 'Local_Library_Schema'")
        tables = []
        for table in self.cursor.fetchall():
            tables.append(table[0])
        return tables

    def sql_get_pk(self, table_name):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            self.cursor.execute("SELECT COLUMN_NAME "
                                "FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE "
                                f"WHERE TABLE_SCHEMA = '{self.schema_name}' "
                                "AND CONSTRAINT_NAME = 'PRIMARY' "
                                f"AND TABLE_NAME = '{table_name}';")
            return self.cursor.fetchone()[0]
        except Exception as msg:
            print("ERROR", msg)
            return False

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

    def sql_select(self, table_name=str, fields=None, conditions=dict):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            if fields:
                if isinstance(fields, tuple) or isinstance(fields, set) or isinstance(fields, list):
                    fields = ", ".join(fields)
                if conditions == dict:
                    self.cursor.execute(f"SELECT {fields} FROM {table_name}")
                else:
                    condition = list()
                    for c in conditions:
                        condition.append(f"{c} = {conditions[c]}")
                    condition = " AND ".join(condition)
                    self.cursor.execute(f"SELECT {fields} FROM {table_name} WHERE {condition}")
            else:
                self.cursor.execute(f"SELECT * FROM {table_name}")
            return self.cursor.fetchall()
        except (mysql.connector.errors.ProgrammingError, TypeError, Exception) as msg:
            print("ERROR", msg)
            return False

    def sql_select_joint_fk(self, table_name=str):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            if table_name == 'BOOKS':
                self.cursor.execute("SELECT b_id, b_name, b_desc, b_status, "
                                    "CONCAT(AUTHOR.a_fname, ' ', AUTHOR.a_lname) AS a_fullname, "
                                    "PUBLISHER.p_name FROM BOOKS "
                                    "LEFT JOIN AUTHOR ON BOOKS.a_id = AUTHOR.a_id "
                                    "LEFT JOIN PUBLISHER ON BOOKS.p_id = PUBLISHER.p_id")
            elif table_name == 'LENDING':
                self.cursor.execute("SELECT l_id, l_start_date, l_due_date, l_return_date, "
                                    "CONCAT(MEMBERS.mb_fname, ' ', MEMBERS.mb_lname) AS mb_fullname, "
                                    "BOOKS.b_name FROM LENDING "
                                    "LEFT JOIN MEMBERS ON LENDING.mb_id = LENDING.mb_id "
                                    "LEFT JOIN BOOKS ON LENDING.b_id = BOOKS.b_id")
            else:
                raise Exception("table does not have existing select joint format")
            return self.cursor.fetchall()
        except (mysql.connector.errors.ProgrammingError, TypeError, Exception) as msg:
            print("ERROR", msg)
            return False

    def sql_insert(self, table_name=str, data_dict=dict):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            key_list = []
            value_list = []
            for col in data_dict:
                key_list.append(col)
                value_list.append(data_dict[col])
            key_list = ", ".join(key_list)
            if len(value_list) == 1:
                self.cursor.execute(f"INSERT INTO {table_name} ({key_list}) VALUES ('{value_list[0]}')")
            else:
                self.cursor.execute(f"INSERT INTO {table_name} ({key_list}) VALUES {tuple(value_list)}")
            self.connection.commit()
            return True
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.IntegrityError,
                Exception, TypeError) as msg:
            print("ERROR", msg)
            return False

    def sql_update(self, table_name=str, primary_key=int, data_dict=dict):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            pk_col = self.sql_get_pk(table_name)
            for col in data_dict:
                self.cursor.execute(f"UPDATE {table_name} SET {col} = '{data_dict[col]}' WHERE {pk_col} = '{primary_key}'")
            self.connection.commit()
            return True
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.IntegrityError,
                Exception, TypeError) as msg:
            print("ERROR", msg)
            return False

    def sql_delete(self, table_name=str, primary_key=int):
        try:
            if table_name not in self.sql_get_table():
                raise Exception("table name does not match any existing tables")
            pk_col = self.sql_get_pk(table_name)
            self.cursor.execute(f"DELETE FROM {table_name} WHERE {pk_col} = {primary_key}")
            self.connection.commit()
            return True
        except (mysql.connector.errors.ProgrammingError, mysql.connector.errors.IntegrityError, Exception) as msg:
            print("ERROR", msg)
            return False

    def close(self):
        self.connection.close()
