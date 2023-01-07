import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_main as mm
import __main__ as m
import datetime as d
from datetime import date
from tkcalendar import DateEntry




class MemberAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
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

        self.member_fn_label = tk.Label(self, text="Enter member First Name*")
        self.member_fn_label.pack(padx=10, pady=2)

        self.member_fn_entry = tk.Entry(self)
        self.member_fn_entry.pack(padx=10, pady=2)

        self.member_ln_label = tk.Label(self, text="Enter member Last Name*")
        self.member_ln_label.pack(padx=10, pady=2)

        self.member_ln_entry = tk.Entry(self)
        self.member_ln_entry.pack(padx=10, pady=2)

        self.member_age_label = tk.Label(self, text="Enter member Age")
        self.member_age_label.pack(padx=10, pady=2)

        self.member_age_entry = tk.Entry(self)
        self.member_age_entry.pack(padx=10, pady=2)

        self.member_bd_label = tk.Label(self, text="Enter member Birthday")
        self.member_bd_label.pack(padx=10, pady=2)

        self.member_bd_entry = DateEntry(self)
        self.member_bd_entry.pack(padx=10, pady=2)

        self.member_phone_label = tk.Label(self, text="Enter member Phone number")
        self.member_phone_label.pack(padx=10, pady=2)

        self.member_phone_entry = tk.Entry(self)
        self.member_phone_entry.pack(padx=10, pady=2)

        self.member_email_label = tk.Label(self, text="Enter member Email")
        self.member_email_label.pack(padx=10, pady=2)

        self.member_email_entry = tk.Entry(self)
        self.member_email_entry.pack(padx=10, pady=2)

        self.member_national_id_label = tk.Label(self, text="Enter member National ID")
        self.member_national_id_label.pack(padx=10, pady=2)
 
        self.member_national_id_entry = tk.Entry(self)
        self.member_national_id_entry.pack(padx=10, pady=2)

        self.member_passport_id_label = tk.Label(self, text="Enter member Passport ID")
        self.member_passport_id_label.pack(padx=10, pady=2)

        self.member_passport_id_entry = tk.Entry(self)
        self.member_passport_id_entry.pack(padx=10, pady=2)

        self.member_address_label = tk.Label(self, text="Enter member Address")
        self.member_address_label.pack(padx=10, pady=2)

        self.member_address_entry = tk.Entry(self)
        self.member_address_entry.pack(padx=10, pady=2)

        self.submit_button=tk.Button(self ,text = 'Submit', command=lambda:self.add_to_SQL())
        self.submit_button.pack(padx=10, pady=2)

        # Error message
        self.error_label = tk.Label(self, text=self.error_msg, fg='IndianRed1')
        self.error_label.pack(padx=10, pady=2)

    def add_to_SQL(self):
        mb_fname = self.member_fn_entry.get()
        mb_lname = self.member_ln_entry.get()
        mb_age = self.member_age_entry.get()
        mb_birthday = self.member_bd_entry.get_date()
        mb_phone = self.member_phone_entry.get()
        mb_email = self.member_email_entry.get()
        mb_national_id = self.member_national_id_entry.get()
        mb_passport_id = self.member_passport_id_entry.get()
        mb_address = self.member_address_entry.get()

        if mb_fname == '' or mb_lname == '':
            self.error_msg = "Please fill the all the required field(s)"
            self.error_label.config(text=self.error_msg)
            return
        elif len(mb_fname) > 50:
            self.error_msg = "Text exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_lname) > 50:
            self.error_msg = "Text exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_age) > 3:
            self.error_msg = "Age exceeded 3 digits"
            self.error_label.config(text=self.error_msg)
            return
        
        elif mb_age != '' and mb_age.isnumeric() is False:
            self.error_msg = "Please enter a valid age"
            self.error_label.config(text=self.error_msg)
            return

        elif mb_birthday > d.date.today():
            self.error_msg = "Please enter a valid birthday"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_phone) > 13:
            self.error_msg = "Phone number exceeded 13 digits"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_email) > 50:
            self.error_msg = "Text exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_national_id) > 13:
            self.error_msg = "Phone number exceeded 13 digits"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_passport_id) > 8:
            self.error_msg = "Text exceeded 8 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_address) > 100:
            self.error_msg = "Text exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return


        # Insert to SQL
        m.sql_connection.sql_insert('MEMBERSß', {'mb_fname':mb_fname,'mb_lname':mb_lname, 'mb_age':mb_age, 'mb_birthday':mb_birthday, 'mb_phone':mb_phone, 'mb_email':mb_email, 'mb_national_id':mb_national_id, 'mb_passport_id':mb_passport_id, 'mb_address':mb_address})

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
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)    

class RegisterWindow(tk.Toplevel): 
    def __init__(self, parent): 
        super().__init__(parent)  

      
