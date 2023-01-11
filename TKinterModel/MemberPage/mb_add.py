import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_main as mm
import TKinterModel.MemberPage.mb_view as mv
import __main__ as m
import datetime as d
from tkcalendar import DateEntry


class MemberAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Member Page',
                                command=lambda: sf.show_frame(mm.MemberMainPage))
        book_button.pack(padx=10, pady=10)

        self.member_fn_label = tk.Label(self, text="Enter member First Name*")
        self.member_fn_label.pack(padx=10, pady=2)

        self.member_fn_entry = tk.Entry(self)
        self.member_fn_entry.pack(padx=10, pady=2)

        self.member_ln_label = tk.Label(self, text="Enter member Last Name*")
        self.member_ln_label.pack(padx=10, pady=2)

        self.member_ln_entry = tk.Entry(self)
        self.member_ln_entry.pack(padx=10, pady=2)

        self.member_bd_label = tk.Label(self, text="Enter member Birthday")
        self.member_bd_label.pack(padx=10, pady=2)

        self.mbd = tk.StringVar()
        self.member_bd_entry = DateEntry(self, textvariable=self.mbd, locale='en_US', date_pattern='yyyy-mm-dd')
        self.member_bd_entry.configure(validate='none')
        self.mbd.set('')
        self.member_bd_entry.delete(0, "end")
        self.member_bd_entry.pack(padx=10, pady=2)

        self.member_phone_label = tk.Label(self, text="Enter member Phone number")
        self.member_phone_label.pack(padx=10, pady=2)

        self.member_phone_entry = tk.Entry(self)
        self.member_phone_entry.pack(padx=10, pady=2)

        self.member_email_label = tk.Label(self, text="Enter member Email")
        self.member_email_label.pack(padx=10, pady=2)

        self.member_email_entry = tk.Entry(self)
        self.member_email_entry.pack(padx=10, pady=2)

        self.member_national_id_label = tk.Label(
            self, text="Enter member National ID")
        self.member_national_id_label.pack(padx=10, pady=2)

        self.member_national_id_entry = tk.Entry(self)
        self.member_national_id_entry.pack(padx=10, pady=2)

        self.member_passport_id_label = tk.Label(
            self, text="Enter member Passport ID")
        self.member_passport_id_label.pack(padx=10, pady=2)

        self.member_passport_id_entry = tk.Entry(self)
        self.member_passport_id_entry.pack(padx=10, pady=2)

        self.member_address_label = tk.Label(self, text="Enter member Address")
        self.member_address_label.pack(padx=10, pady=2)

        self.member_address_entry = tk.Entry(self)
        self.member_address_entry.pack(padx=10, pady=2)

        self.submit_button = tk.Button(
            self, text='Submit', command=lambda: self.add_to_sql())
        self.submit_button.pack(padx=10, pady=2)

        # Error message
        self.error_label = tk.Label(self, text=self.error_msg, fg='IndianRed1')
        self.error_label.pack(padx=10, pady=2)

    def add_to_sql(self):
        mb_fname = self.member_fn_entry.get()
        mb_lname = self.member_ln_entry.get()
        mb_birthday = self.mbd.get()
        mb_phone = self.member_phone_entry.get()
        mb_email = self.member_email_entry.get()
        mb_national_id = self.member_national_id_entry.get()
        mb_passport_id = self.member_passport_id_entry.get()
        mb_address = self.member_address_entry.get()
        age = 'NULL'

        if mb_fname == '' or mb_lname == '':
            self.error_msg = "Please fill the all the required field(s)"
            self.error_label.config(text=self.error_msg)
            return
        elif len(mb_fname) > 50:
            self.error_msg = "First name exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_lname) > 50:
            self.error_msg = "Last name exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_phone) > 13:
            self.error_msg = "Phone number exceeded 13 digits"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_email) > 50:
            self.error_msg = "Email exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_national_id) > 13:
            self.error_msg = "National ID number exceeded 13 digits"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_passport_id) > 8:
            self.error_msg = "Passport ID exceeded 8 characters"
            self.error_label.config(text=self.error_msg)
            return

        elif len(mb_address) > 100:
            self.error_msg = "Address exceeded 100 characters"
            self.error_label.config(text=self.error_msg)
            return
        if mb_birthday != '':
            try:
                mb_birthday = d.datetime.strptime(mb_birthday, '%Y-%m-%d').date()
            except ValueError:
                self.error_msg = "Please enter a valid birthday"
                self.error_label.config(text=self.error_msg)
                return
            if mb_birthday > d.date.today():
                self.error_msg = "Please enter a valid birthday"
                self.error_label.config(text=self.error_msg)
                return
            today = d.date.today()
            age = today.year - mb_birthday.year - ((today.month, today.day) < (mb_birthday.month, mb_birthday.day))
            mb_birthday = mb_birthday.strftime('%Y-%m-%d')
            mb_birthday = mb_birthday
        else:
            mb_birthday = 'NULL'
            age = 'NULL'

        # Insert to SQL
        m.sql_connection.sql_insert('MEMBERS', {'mb_fname': mb_fname, 'mb_lname': mb_lname, 'mb_birthday': mb_birthday,
                                                'mb_age': age, 'mb_phone': mb_phone, 'mb_email': mb_email,
                                                'mb_national_id': mb_national_id, 'mb_passport_id': mb_passport_id,
                                                'mb_address': mb_address})

        # Empty input field
        self.member_fn_entry.delete(0, "end")
        self.member_ln_entry.delete(0, "end")
        self.member_bd_entry.delete(0, "end")
        self.member_phone_entry.delete(0, "end")
        self.member_email_entry.delete(0, "end")
        self.member_national_id_entry.delete(0, "end")
        self.member_passport_id_entry.delete(0, "end")
        self.member_address_entry.delete(0, "end")
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)

        # Return user to author page
        sf.frames[mv.MemberViewPage].refresh()
        sf.show_frame(mv.MemberViewPage)


class RegisterWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
