import tkinter
import mysql.connector
from TKinterModel.main_scene import *

if __name__ == "__main__":
    # Establish connection to the database
    connection = mysql.connector.connect(
        host="localhost",
        port="3306",
        user='root',
        database="Local_Library_Schema"
    )
    cursor = connection.cursor()
    # Remove logs in later version
    print(connection)
    cursor.execute("SHOW TABLES")
    for table in cursor:
        print(table)

    app = App()
    app.mainloop()
