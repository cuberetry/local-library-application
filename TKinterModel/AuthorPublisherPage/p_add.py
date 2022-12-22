import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m


class PublisherAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.home_button = tk.Button(self, text='Homepage',
                                     command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Author/Publisher Page',
                                     command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        self.book_button.pack(padx=10, pady=20)

        self.p_name_l = tk.Label(self, text='Add Publisher Name:')
        self.p_name_l.pack(padx=10, pady=2)
        self.p_name_e = tk.Entry(self)
        self.p_name_e.pack(padx=10, pady=2)

        self.p_submit = tk.Button(self, text='submit', command=lambda: self.p_add())
        self.p_submit.pack(padx=10, pady=20)

    def p_add(self):
        p_name = self.p_name_e.get()
        m.sql_connection.sql_insert("PUBLISHER", {"p_name": p_name})

        # Empty input field
        self.p_name_e.delete(0, "end")
