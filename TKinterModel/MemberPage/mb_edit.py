import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_view as mv
import __main__ as m
import datetime as d
from tkcalendar import DateEntry


class MemberEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
        self.home_button = tk.Button(
            self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.member_button = tk.Button(self, text='Member View Page')
        self.member_button['command'] = self.button_clicked
        self.member_button.pack(padx=10, pady=20)

        # Edit first name
        self.mb_fname_label = tk.Label(self, text="Edit First Member Name")
        self.mb_fname_label.pack(padx=10, pady=2)

        self.mb_fname = tk.StringVar()
        self.mb_fname_entry = tk.Entry(self, textvariable=self.mb_fname)
        self.mb_fname_entry.pack(padx=10, pady=2)

        # Edit first name
        self.mb_lname_label = tk.Label(self, text="Edit Last Member Name")
        self.mb_lname_label.pack(padx=10, pady=2)

        self.mb_lname = tk.StringVar()
        self.mb_lname_entry = tk.Entry(self, textvariable=self.mb_lname)
        self.mb_lname_entry.pack(padx=10, pady=2)

        # Edit member birthday
        self.member_bd_label = tk.Label(self, text="Edit member Birthday")
        self.member_bd_label.pack(padx=10, pady=2)

        self.member_bd_entry = DateEntry(self, locale='en_US', date_pattern='yyyy-mm-dd')
        self.member_bd_entry.delete(0, "end")
        self.member_bd_entry.pack(padx=10, pady=2)

        # Edit member phone
        self.mb_phone_label = tk.Label(self, text="Edit Member Phone")
        self.mb_phone_label.pack(padx=10, pady=2)

        self.mb_phone = tk.StringVar()
        self.mb_phone_entry = tk.Entry(self, textvariable=self.mb_phone)
        self.mb_phone_entry.pack(padx=10, pady=2)

        # Edit member email
        self.mb_email_label = tk.Label(self, text="Edit Member email")
        self.mb_email_label.pack(padx=10, pady=2)

        self.mb_email = tk.StringVar()
        self.mb_email_entry = tk.Entry(self, textvariable=self.mb_email)
        self.mb_email_entry.pack(padx=10, pady=2)

        # Edit member national id
        self.mb_national_id_label = tk.Label(
            self, text="Edit Member National ID")
        self.mb_national_id_label.pack(padx=10, pady=2)

        self.mb_national_id = tk.StringVar()
        self.mb_national_id_entry = tk.Entry(
            self, textvariable=self.mb_national_id)
        self.mb_national_id_entry.pack(padx=10, pady=2)

        # Edit member passport id
        self.p_id_label = tk.Label(self, text="Edit Member passport ID")
        self.p_id_label.pack(padx=10, pady=2)

        self.mb_passport_id = tk.StringVar()
        self.mb_passport_id_entry = tk.Entry(
            self, textvariable=self.mb_passport_id)
        self.mb_passport_id_entry.pack(padx=10, pady=2)

        # Edit member address
        self.mb_passport_id_label = tk.Label(self, text="Edit Member Address")
        self.mb_passport_id_label.pack(padx=10, pady=2)

        self.mb_address = tk.StringVar()
        self.mb_address_entry = tk.Entry(self, textvariable=self.mb_address)
        self.mb_address_entry.pack(padx=10, pady=2)

        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.error_label.pack(padx=10, pady=2)

        self.submit_button = tk.Button(self, text='Submit',
                                       command=lambda: self.edit_book())
        self.submit_button.pack(padx=10, pady=20)

        self.target = None

    def edit_book(self):
        self.member_bd_entry.delete(0, "end")
        edit_dict = dict()
        mb_fname = self.mb_fname_entry.get()
        mb_lname = self.mb_lname_entry.get()
        mb_birthday = self.member_bd_entry.get()
        mb_phone = self.mb_phone_entry.get()
        mb_email = self.mb_email_entry.get()
        mb_national_id = self.mb_national_id_entry.get()
        mb_passport_id = self.mb_passport_id_entry.get()
        mb_address = self.mb_address_entry.get()
        if mb_fname != '':
            if len(mb_fname) > 50:
                self.error_msg = "First name exceeded 50 characters"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_fname"] = mb_fname
        if mb_lname != '':
            if len(mb_lname) > 50:
                self.error_msg = "Last name exceeded 50 characters"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_lname"] = mb_lname
        if mb_birthday != '':
            mb_birthday = d.datetime.strptime(mb_birthday, '%Y-%m-%d').date()
            if mb_birthday > d.date.today():
                self.error_msg = "Please enter a valid birthday"
                self.error_label.config(text=self.error_msg)
                return
            today = d.date.today()
            age = today.year - mb_birthday.year - ((today.month, today.day) < (mb_birthday.month, mb_birthday.day))
            mb_birthday = mb_birthday.strftime('%Y-%m-%d')
            edit_dict["mb_age"] = age
            edit_dict["mb_birthday"] = mb_birthday
        if mb_phone != '':
            if len(mb_phone) > 13:
                self.error_msg = "Phone number exceeded 13 digits"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_phone"] = mb_phone
        if mb_email != '':
            if len(mb_email) > 50:
                self.error_msg = "Email exceeded 50 characters"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_email"] = mb_email
        if mb_national_id != '':
            if len(mb_national_id) > 13:
                self.error_msg = "National ID exceeded 13 digits"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_national_id"] = mb_national_id
        if mb_passport_id != '':
            if len(mb_passport_id) > 8:
                self.error_msg = "Passport ID exceeded 8 characters"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_passport_id"] = mb_passport_id
        if mb_address != '':
            if len(mb_address) > 100:
                self.error_msg = "Address exceeded 100 characters"
                self.error_label.config(text=self.error_msg)
                return
            edit_dict["mb_address"] = mb_address
        m.sql_connection.sql_update(
            "MEMBERS", self.target['values'][0], edit_dict)
        # Empty input field
        self.mb_fname_entry.delete(0, "end")
        self.mb_lname_entry.delete(0, "end")
        self.member_bd_entry.delete(0, "end")
        self.mb_phone_entry.delete(0, "end")
        self.mb_email_entry.delete(0, "end")
        self.mb_national_id_entry.delete(0, "end")
        self.mb_passport_id_entry.delete(0, "end")
        self.mb_address_entry.delete(0, "end")
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)
        print(edit_dict)

        # Return user to lending page
        sf.frames[mv.MemberViewPage].refresh()
        sf.show_frame(mv.MemberViewPage)

    def button_clicked(self):
        # Empty input field
        self.mb_fname_entry.delete(0, "end")
        self.mb_lname_entry.delete(0, "end")
        self.member_bd_entry.delete(0, "end")
        self.mb_phone_entry.delete(0, "end")
        self.mb_email_entry.delete(0, "end")
        self.mb_national_id_entry.delete(0, "end")
        self.mb_passport_id_entry.delete(0, "end")
        self.mb_address_entry.delete(0, "end")
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)
        sf.show_frame(mv.MemberViewPage)
