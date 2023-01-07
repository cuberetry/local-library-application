import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_main as mm
import __main__ as m
from tkcalendar import Calendar, DateEntry




class MemberAddPage(tk.Frame):
    def __init__(self, parent):
        


        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Member Page', command=lambda: sf.show_frame(mm.MemberMainPage))
        book_button.pack(padx=10, pady=10)


        # self.author_fn_label = tk.Label(self, text="Add Author First Name",width=10,font=("bold", 11))
        # self.author_fn_label.pack(padx=10, pady=2)
        # self.author_fn_label.place(x=90,y=53)  

        # self.author_fn_entry = tk.Entry(self)
        # self.author_fn_entry.pack(padx=10, pady=2)
        # self.author_fn_entry.place(x=200, y=120)

        self.member_fn_label = tk.Label(self, text="Add member First Name")
        self.member_fn_label.pack(padx=10, pady=2)

        self.member_fn_entry = tk.Entry(self)
        self.member_fn_entry.pack(padx=10, pady=2)

        self.member_ln_label = tk.Label(self, text="Add member Last Name")
        self.member_ln_label.pack(padx=10, pady=2)

        self.member_ln_entry = tk.Entry(self)
        self.member_ln_entry.pack(padx=10, pady=2)

        self.member_age_label = tk.Label(self, text="Add member Age")
        self.member_age_label.pack(padx=10, pady=2)

        self.member_age_entry = tk.Entry(self)
        self.member_age_entry.pack(padx=10, pady=2)

        self.member_bd_label = tk.Label(self, text="Add member Birthday")
        self.member_bd_label.pack(padx=10, pady=2)

        self.member_bd_entry = DateEntry(self)
        self.member_bd_entry.pack(padx=10, pady=2)

        self.member_phone_label = tk.Label(self, text="Add member Phone number")
        self.member_phone_label.pack(padx=10, pady=2)

        self.member_phone_entry = tk.Entry(self)
        self.member_phone_entry.pack(padx=10, pady=2)

        self.member_email_label = tk.Label(self, text="Add member Email")
        self.member_email_label.pack(padx=10, pady=2)

        self.member_email_entry = tk.Entry(self)
        self.member_email_entry.pack(padx=10, pady=2)

        self.member_national_id_label = tk.Label(self, text="Add member National ID")
        self.member_national_id_label.pack(padx=10, pady=2)
 
        self.member_national_id_entry = tk.Entry(self)
        self.member_national_id_entry.pack(padx=10, pady=2)

        self.member_passport_id_label = tk.Label(self, text="Add member Passport ID")
        self.member_passport_id_label.pack(padx=10, pady=2)

        self.member_passport_id_entry = tk.Entry(self)
        self.member_passport_id_entry.pack(padx=10, pady=2)

        self.member_address_label = tk.Label(self, text="Add member Address")
        self.member_address_label.pack(padx=10, pady=2)

        self.member_address_entry = tk.Entry(self)
        self.member_address_entry.pack(padx=10, pady=2)

        self.submit_button=tk.Button(self ,text = 'Submit', command=lambda:self.add_to_SQL())
        self.submit_button.pack(padx=10, pady=10)

    def add_to_SQL(self):
        mb_fname = self.member_fn_entry.get()
        mb_lname = self.member_ln_entry.get()
        mb_age = self.member_fn_entry.get()
        mb_birthday = self.member_ln_entry.get()
        mb_phone = self.member_fn_entry.get()
        mb_email = self.member_ln_entry.get()
        mb_national_id = self.member_ln_entry.get()
        mb_passport_id = self.member_fn_entry.get()
        mb_address = self.member_ln_entry.get()

        if len(mb_fname) > 51:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_lname) > 51:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_age) > 4:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_birthday) > 51:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_phone) > 14:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_email) > 51:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_national_id) > 14:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_passport_id) > 9:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        elif len(mb_address) > 101:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return

        # Limit Book Description input characters
        elif len(mb_des) > 201:
            self.error_label.config(text="Text exceeded 200 characters")
            return
        # Clear error msg
        else:
            self.error_label.config(text="")

        # Handling date
        mbsd = now
        mbdd = now + d.timedelta(days=duration)

        lsd = lsd.strftime('%Y-%m-%d %H:%M:%S')
        ldd = ldd.strftime('%Y-%m-%d')

        # Insert to SQL
        m.sql_connection.sql_insert('MEMBER', {'mb_fname':mb_fname,'mb_lname':mb_lname, 'mb_age':mb_age, 'mb_birthday':mb_birthday, 'mb_phone':mb_phone, 'mb_email':mb_email, 'mb_national_id':mb_national_id, 'mb_passport_id':mb_passport_id, 'mb_address':mb_address})

        # Empty input field
        self.member_fn_entry.delete(0,"end")
        self.member_ln_entry.delete(0,"end")
        self.member_age_entry.delete(0,"end")
        self.member_bd_entry.delete(0,"end")
        self.member_phone_entry.delete(0,"end")
        self.member_email_entry.delete(0,"end")
        self.member_national_id_entry.delete(0,"end")
        self.member_passport_id_entry.delete(0,"end")
        self.member_address_entry.delete(0,"end")

    # def member_bd_entry():
    #     #Import tkinter library

    #     #Create an instance of tkinter frame
    #     win= Tk()
    #     #Set the Geometry
    #     win.geometry("750x250")
    #     win.title("Date Picker")
    #     #Create a Label
    #     Label(win, text= "Choose a Date", background= 'gray61', foreground="white").pack(padx=20,pady=20)
    #     #Create a Calendar using DateEntry
    #     cal = DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
    #     cal.pack(pady=20)
    #     win.mainloop()
    
    
    

class RegisterWindow(tk.Toplevel): 
    def __init__(self, parent): 
        super().__init__(parent)  

      
