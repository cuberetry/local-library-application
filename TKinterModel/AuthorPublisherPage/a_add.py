import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m

def set_text_by_button(fn, ln, fn_entry, ln_entry, finish_label):
    # insert to SQL
    m.sql_connection.sql_insert('AUTHOR', {'a_fname':fn.get(),'a_lname':ln.get()})

    #Empty input field
    fn_entry.delete(0,"end")
    ln_entry.delete(0,"end")

    #Indicate successfull insert
    finish_label.config(text="Added successfully")
    
class AuthorAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Author/Publisher Page',
                                command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        book_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is author add page")
        label.pack(padx=10, pady=20)

        # Edit
        author_fn_label = tk.Label(self, text="Add Firstname")
        author_fn_label.pack(padx=10, pady=2)

        author_fn = tk.StringVar()
        author_fn_entry = tk.Entry(self, textvariable=author_fn)
        author_fn_entry.pack(padx=10, pady=2)

        author_ln_label = tk.Label(self, text="Add Lastname")
        author_ln_label.pack(padx=10, pady=2)

        author_ln = tk.StringVar()
        author_ln_entry = tk.Entry(self, textvariable=author_ln)
        author_ln_entry.pack(padx=10, pady=2)

        success_label = tk.Label(self, text="")
        success_label.pack(padx=20, pady=20)

        submit_button=tk.Button(self ,text = 'Submit', command=lambda:set_text_by_button(author_fn, author_ln, author_fn_entry, author_ln_entry, success_label))
        submit_button.pack(padx=10, pady=20)



    
        