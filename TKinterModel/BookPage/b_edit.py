import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as bm
import __main__ as m


class BookEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Book Page', command=lambda: sf.show_frame(bm.BookMainPage))
        self.book_button.pack(padx=10, pady=20)

        # Edit name
        self.b_name_label = tk.Label(self, text="Edit Book Name")
        self.b_name_label.pack(padx=10, pady=2)

        self.b_name = tk.StringVar()
        self.b_name_entry = tk.Entry(self, textvariable=self.b_name)
        self.b_name_entry.pack(padx=10, pady=2)

        # Edit description
        self.b_desc_label = tk.Label(self, text="Edit Book Description")
        self.b_desc_label.pack(padx=10, pady=2)

        self.b_desc = tk.StringVar()
        self.b_desc_entry = tk.Entry(self, textvariable=self.b_desc)
        self.b_desc_entry.pack(padx=10, pady=2)

        # Edit author ID
        self.a_id_label = tk.Label(self, text="Edit Author ID")
        self.a_id_label.pack(padx=10, pady=2)

        self.a_id = tk.StringVar()
        self.a_id_entry = tk.Entry(self, textvariable=self.a_id)
        self.a_id_entry.pack(padx=10, pady=2)

        # Edit publisher ID
        self.p_id_label = tk.Label(self, text="Edit Publisher ID")
        self.p_id_label.pack(padx=10, pady=2)

        self.p_id = tk.StringVar()
        self.p_id_entry = tk.Entry(self, textvariable=self.p_id)
        self.p_id_entry.pack(padx=10, pady=2)

        self.submit_button = tk.Button(self, text='Submit',
                                       command=lambda: self.edit_book())
        self.submit_button.pack(padx=10, pady=20)

        self.target = None

    def edit_book(self):
        edit_dict = dict()
        if self.b_name_entry.get() != '':
            edit_dict["b_name"] = self.b_name_entry.get()
        if self.b_desc_entry.get() != '':
            edit_dict["b_desc"] = self.b_desc_entry.get()
        if self.a_id_entry.get() != '':
            edit_dict["a_id"] = self.a_id_entry.get()
        if self.p_id_entry.get() != '':
            edit_dict["p_id"] = self.p_id_entry.get()
        m.sql_connection.sql_update("BOOKS", self.target['values'][0], edit_dict)
