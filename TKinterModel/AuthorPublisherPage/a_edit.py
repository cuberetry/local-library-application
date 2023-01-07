import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.a_view as av
import __main__ as m


class AuthorEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.home_button = tk.Button(
            self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(
            self, text='Author Page', command=lambda: sf.show_frame(av.AuthorViewPage))
        self.book_button.pack(padx=10, pady=20)

        # Edit firstname
        self.a_fname_label = tk.Label(self, text="Edit Author Firstname")
        self.a_fname_label.pack(padx=10, pady=2)

        self.a_fname = tk.StringVar()
        self.a_fname_entry = tk.Entry(self, textvariable=self.a_fname)
        self.a_fname_entry.pack(padx=10, pady=2)

        # Edit lastname
        self.a_lname_label = tk.Label(self, text="Edit Author Lastname")
        self.a_lname_label.pack(padx=10, pady=2)

        self.a_lname = tk.StringVar()
        self.a_lname_entry = tk.Entry(self, textvariable=self.a_lname)
        self.a_lname_entry.pack(padx=10, pady=2)

        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.error_label.pack(padx=10, pady=2)

        self.submit_button = tk.Button(self, text='Submit',
                                       command=lambda: self.edit_author())
        self.submit_button.pack(padx=10, pady=20)

        self.target = None

    def edit_author(self):
        edit_dict = dict()
        if self.a_fname_entry.get() != '':
            edit_dict["a_fname"] = self.a_fname_entry.get()
            if len(self.a_fname_entry.get()) > 50:
                self.error_label.config(text="Text exceeded 50 characters")
                return
            else:
                self.error_label.config(text="")
        if self.a_lname_entry.get() != '':
            edit_dict["a_lname"] = self.a_lname_entry.get()
            if len(self.a_lname_entry.get()) > 50:
                self.error_label.config(text="Text exceeded 50 characters")
                return
            else:
                self.error_label.config(text="")
        m.sql_connection.sql_update(
            "AUTHOR", self.target['values'][0], edit_dict)
        # Empty input field
        self.a_fname_entry.delete(0, "end")
        self.a_lname_entry.delete(0, "end")

        # Return user to publisher page
        sf.frames[av.AuthorViewPage].refresh()
        sf.show_frame(av.AuthorViewPage)
