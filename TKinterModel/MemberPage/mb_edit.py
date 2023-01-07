import tkinter as tk
from tkcalendar import DateEntry
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_view as mv
import datetime as d
import __main__ as m


class MemberEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.mb_birthday = None
        self.home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.member_button = tk.Button(self, text='Member View Page', command=lambda: sf.show_frame(mv.MemberViewPage))
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

        # Edit member age
        self.mb_age_label = tk.Label(self, text="Edit Member Age")
        self.mb_age_label.pack(padx=10, pady=2)

        self.mb_age = tk.StringVar()
        self.mb_age_entry = tk.Entry(self, textvariable=self.mb_age)
        self.mb_age_entry.pack(padx=10, pady=2)

        # Edit member birthday
        self.mb_bd_label = tk.Label(self, text="Edit Member Birthday")
        self.mb_bd_label.pack(padx=10, pady=2)

        self.mb_birthday_entry = DateEntry(self, locale='en_US', date_pattern='yyyy/mm/dd')
        self.mb_birthday_entry.pack(padx=10, pady=2)

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
        self.mb_national_id_label = tk.Label(self, text="Edit Member National ID")
        self.mb_national_id_label.pack(padx=10, pady=2)

        self.mb_national_id = tk.StringVar()
        self.mb_national_id_entry = tk.Entry(self, textvariable=self.mb_national_id)
        self.mb_national_id_entry.pack(padx=10, pady=2)

        # Edit member passport id
        self.p_id_label = tk.Label(self, text="Edit Member passport ID")
        self.p_id_label.pack(padx=10, pady=2)

        self.mb_passport_id = tk.StringVar()
        self.mb_passport_id_entry = tk.Entry(self, textvariable=self.mb_passport_id)
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
        edit_dict = dict()
        self.mb_birthday = self.mb_birthday_entry.get_date()
        if self.mb_fname_entry.get() != '':
            edit_dict["mb_fname"] = self.mb_fname_entry.get()
            if len(self.mb_fname_entry.get()) > 50:
                self.error_label.config(text="Text exceeded 50 characters")
                return
            else:
                self.error_label.config(text="")
        if self.mb_lname_entry.get() != '':
            edit_dict["mb_lname"] = self.mb_lname_entry.get()
            if len(self.mb_lname_entry.get()) > 50:
                self.error_label.config(text="Text exceeded 50 characters")
                return
            else:
                self.error_label.config(text="")
        if self.mb_age_entry.get() != '':
            edit_dict["mb_age"] = self.mb_age_entry.get()
            if len(self.mb_age_entry.get()) > 3:
                self.error_label.config(text="Please enter a valid age")
                return
            elif self.mb_age_entry.get().isnumeric() is False:
                self.error_label.config(text="Please enter a valid age")
                return
            else:
                self.error_label.config(text="")

        if self.mb_birthday != '':
            if self.mb_birthday > d.date.today():
                self.error_label.config(text="Please enter a valid birthday")
                return
            if not isinstance(self.mb_birthday, d.date):
                self.error_label.config(text="Please enter a valid birthday")
                return
            else:
                self.error_label.config(text="")
            self.mb_birthday = self.mb_birthday.strftime('%Y-%m-%d')
            edit_dict["mb_birthday"] = self.mb_birthday

        if self.mb_phone_entry.get() != '':
            edit_dict["mb_phone"] = self.mb_phone_entry.get()
            if len(self.mb_phone_entry.get()) > 13:
                self.error_label.config(text="phone number exceeded 13 digits")
                return
            else:
                self.error_label.config(text="")
        if self.mb_email_entry.get() != '':
            edit_dict["mb_email"] = self.mb_email_entry.get()
            if len(self.mb_email_entry.get()) > 50:
                self.error_label.config(text="Text exceeded 50 characters")
                return
            else:
                self.error_label.config(text="")
        if self.mb_national_id_entry.get() != '':
            edit_dict["mb_national_id"] = self.mb_national_id_entry.get()
            if len(self.mb_national_id_entry.get()) > 13:
                self.error_label.config(text="Text exceeded 13 characters")
                return
            else:
                self.error_label.config(text="")
        if self.mb_passport_id_entry.get() != '':
            edit_dict["mb_passport_id"] = self.mb_passport_id_entry.get()
            if len(self.mb_passport_id_entry.get()) > 8:
                self.error_label.config(text="Text exceeded 8 characters")
                return
            else:
                self.error_label.config(text="")
        if self.mb_address_entry.get() != '':
            edit_dict["mb_address"] = self.mb_address_entry.get()
            if len(self.mb_address_entry.get()) > 100:
                self.error_label.config(text="Text exceeded 100 characters")
                return
            else:
                self.error_label.config(text="")
        m.sql_connection.sql_update("MEMBERS", self.target['values'][0], edit_dict)
        # Empty input field
        self.mb_fname_entry.delete(0, "end")
        self.mb_lname_entry.delete(0, "end")
        self.mb_age_entry.delete(0, "end")
        self.mb_birthday_entry.delete(0, "end")
        self.mb_phone_entry.delete(0, "end")
        self.mb_email_entry.delete(0, "end")
        self.mb_national_id_entry.delete(0, "end")
        self.mb_passport_id_entry.delete(0, "end")
        self.mb_address_entry.delete(0, "end")

        # Return user to publisher page
        sf.frames[mv.MemberViewPage].refresh()
        sf.show_frame(mv.MemberViewPage)
