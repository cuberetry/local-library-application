import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m

    
class AuthorAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Author/Publisher Page',
                                command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        self.book_button.pack(padx=10, pady=20)

        self.author_fn_label = tk.Label(self, text="Add Author First Name")
        self.author_fn_label.pack(padx=10, pady=2)

        self.author_fn_entry = tk.Entry(self)
        self.author_fn_entry.pack(padx=10, pady=2)

        self.author_ln_label = tk.Label(self, text="Add Author Last Name")
        self.author_ln_label.pack(padx=10, pady=2)

        self.author_ln_entry = tk.Entry(self)
        self.author_ln_entry.pack(padx=10, pady=2)

        self.submit_button=tk.Button(self ,text = 'Submit', command=lambda:self.add_to_SQL())
        self.submit_button.pack(padx=10, pady=20)

    def add_to_SQL(self):
        a_fname = self.author_fn_entry.get()
        a_lname = self.author_ln_entry.get()

        # Insert to SQL
        m.sql_connection.sql_insert('AUTHOR', {'a_fname':a_fname,'a_lname':a_lname})

        # Empty input field
        self.author_fn_entry.delete(0,"end")
        self.author_ln_entry.delete(0,"end")
