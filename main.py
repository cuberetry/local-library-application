from TKinterModel.SystemPage.sys_main_scene import *
from SQLModel.SQLConnection import *
import user_setting

if __name__ == "__main__":
    # Establish connection to the database
    sql_connection = SQLConnection("localhost", "3306", "root", "Local_Library_Schema", user_setting.first_time)

    # Update first time file
    f = open("user_setting.py", "w")
    f.write("first_time = False\n")
    f.close()

    # Update birthday
    sql_connection.sql_select("MEMBER")

    # Tkinter mainloop
    app = App()
    app.mainloop()

    # Close connection to the database
    sql_connection.close()
