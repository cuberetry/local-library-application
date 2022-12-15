import os
import mysql.connector
from TKinterModel.main_scene import *
import SQLScript.sql_execute

if __name__ == "__main__":
    # Establish connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root"
    )
    cursor = connection.cursor()
    SQLScript.sql_execute.sql_execute("./SQLScript/sql_init.sql", cursor)

    # Remove logs in later version
    # print(connection)
    # cursor.execute("SHOW TABLES")
    # for table in cursor:
    #     print(table)

    app = App()
    app.mainloop()
