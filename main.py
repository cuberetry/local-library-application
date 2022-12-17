import mysql.connector
from TKinterModel.main_scene import *
from SQLModel.SQLConnection import *

if __name__ == "__main__":
    # Establish connection to the database
    sql_connection = SQLConnection("localhost", "3306", "root", "Local_Library_Schema", False)
    
    # Tkinter mainloop
    app = App()
    app.mainloop()
