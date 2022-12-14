from datetime import date
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
    today = date.today()
    members = sql_connection.sql_select("MEMBERS")
    for member in members:
        try:
            age = today.year - member[4].year - ((today.month, today.day) < (member[4].month, member[4].day))
        except AttributeError:
            age = 'NULL'
        sql_connection.sql_update("MEMBERS", member[0], {'mb_age': age})

    # Tkinter mainloop
    app = App()
    app.mainloop()

    # Close connection to the database
    sql_connection.close()
