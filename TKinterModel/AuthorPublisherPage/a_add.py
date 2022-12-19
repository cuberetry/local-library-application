import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m

def set_text_by_button(fn_entry, ln_entry):
    a_fname = fn_entry.get()
    a_lname = ln_entry.get()

    # Insert to SQL
    m.sql_connection.sql_insert('AUTHOR', {'a_fname':a_fname,'a_lname':a_lname})

    # Empty input field
    fn_entry.delete(0,"end")
    ln_entry.delete(0,"end")
    
class AuthorAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Author/Publisher Page',
                                command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        book_button.pack(padx=10, pady=20)

        author_fn_label = tk.Label(self, text="Add Author First Name")
        author_fn_label.pack(padx=10, pady=2)

        author_fn_entry = tk.Entry(self)
        author_fn_entry.pack(padx=10, pady=2)

        author_ln_label = tk.Label(self, text="Add Author Last Name")
        author_ln_label.pack(padx=10, pady=2)

        author_ln_entry = tk.Entry(self)
        author_ln_entry.pack(padx=10, pady=2)

        submit_button=tk.Button(self ,text = 'Submit', command=lambda:set_text_by_button(author_fn_entry, author_ln_entry))
        submit_button.pack(padx=10, pady=20)
