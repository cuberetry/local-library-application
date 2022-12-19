import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m


def p_add(p_name_e):
    p_name = p_name_e.get()
    print(p_name, type(p_name))
    m.sql_connection.sql_insert("BOOKS", {"b_name": 'tryy'})


class PublisherAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Author/Publisher Page',
                                command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        book_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is publisher add page")
        label.pack(padx=10, pady=20)

        p_name_l = tk.Label(self, text='Publisher Name: ')
        p_name_l.pack(padx=10, pady=10)
        p_name_e = tk.Entry(self)
        p_name_e.pack(padx=10, pady=10)

        p_submit = tk.Button(self, text='submit', command=lambda: p_add(p_name_e))
        p_submit.pack(padx=10, pady=20)
