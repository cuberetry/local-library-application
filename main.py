import mysql.connector
from TKinterModel.main_scene import *
import SQLScript.sql_execute as sql_execute
import SQLScript.sql_update as sql_update

if __name__ == "__main__":
    # Establish connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root"
    )
    cursor = connection.cursor()
    # sql_execute.sql_execute(cursor, "./SQLScript/sql_init.sql")
    cursor.execute("USE Local_Library_Schema")
    
    # Tkinter mainloop
    app = App()
    app.mainloop()
