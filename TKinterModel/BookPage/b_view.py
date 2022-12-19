import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as bm
import __main__ as m


class BookViewPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Book Page', command=lambda: sf.show_frame(bm.BookMainPage))
        book_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is book view page")
        label.pack(padx=10, pady=20)

        # Init DB connection and table
        self.book_list = m.sql_connection.sql_select("BOOKS")
        self.columns = ["ID", "Name", "Description", "Book Status", "Author ID", "Publisher ID"]
        self.table = ttk.Treeview(self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.update_table(0)

    def update_table(self, page=0):
        for i in range(page*25, (page*25)+25):
            if i > len(self.book_list)-1:
                break
            self.table.insert("", 'end', values=self.book_list[i])
        self.table.place(x=200, y=270)
