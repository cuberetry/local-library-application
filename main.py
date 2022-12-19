from TKinterModel.SystemPage.sys_main_scene import *
from SQLModel.SQLConnection import *

if __name__ == "__main__":
    # Establish connection to the database
    sql_connection = SQLConnection("localhost", "3306", "root", "Local_Library_Schema", True)

    # Tkinter mainloop
    app = App()
    app.mainloop()

    # Close connection to the database
    sql_connection.close()
