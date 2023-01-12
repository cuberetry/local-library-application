import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import TKinterModel.AuthorPublisherPage.a_view as av
import TKinterModel.BookPage.b_view as bv
import TKinterModel.LendingPage.l_view as lv
import __main__ as m


class AuthorAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ''
        self.home_button = tk.Button(self, text='Homepage',
                                     command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Author/Publisher Page',
                                     command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        self.book_button.pack(padx=10, pady=20)

        self.author_fn_label = tk.Label(self, text="Enter Author First Name*")
        self.author_fn_label.pack(padx=10, pady=2)

        self.author_fn_entry = tk.Entry(self)
        self.author_fn_entry.pack(padx=10, pady=2)

        self.author_ln_label = tk.Label(self, text="Enter Author Last Name")
        self.author_ln_label.pack(padx=10, pady=2)

        self.author_ln_entry = tk.Entry(self)
        self.author_ln_entry.pack(padx=10, pady=2)

        self.submit_button = tk.Button(
            self, text='Submit', command=lambda: self.add_to_sql())
        self.submit_button.pack(padx=10, pady=20)

        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.error_label.pack(padx=10, pady=2)

    def add_to_sql(self):
        a_fname = self.author_fn_entry.get()
        a_lname = self.author_ln_entry.get()

        # Handling input fields
        if a_fname == '':
            self.error_msg = "Please fill all the required field(s)!"
            self.error_label.config(text=self.error_msg)
            return
        elif len(a_fname) > 50:
            self.error_msg = "First name exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return
        elif len(a_lname) > 50:
            self.error_msg = "Last name exceeded 50 characters"
            self.error_label.config(text=self.error_msg)
            return
        else:
            self.error_label.config(text="")

        # Empty input field
        self.author_fn_entry.delete(0, "end")
        self.author_ln_entry.delete(0, "end")

        # Insert to SQL
        m.sql_connection.sql_insert(
            'AUTHOR', {'a_fname': a_fname, 'a_lname': a_lname})

        # Return user to author page
        sf.frames[bv.BookViewPage].refresh()
        sf.frames[lv.LendingViewPage].refresh()
        sf.frames[av.AuthorViewPage].refresh()
        sf.show_frame(av.AuthorViewPage)
