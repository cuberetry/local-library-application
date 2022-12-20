import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as bm
import TKinterModel.BookPage.b_edit as be
import __main__ as m


class BookViewPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.cur_page = 0

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Book Page', command=lambda: sf.show_frame(bm.BookMainPage))
        book_button.pack(padx=10, pady=20)

        refresh_button = tk.Button(self, text='Refresh', command=lambda: self.refresh())
        refresh_button.pack(padx=10, pady=20)
        next_button = tk.Button(self, text='Next', command=lambda: self.next_page())
        next_button.pack(padx=0, pady=20, side=tk.RIGHT)
        prev_button = tk.Button(self, text='Prev', command=lambda: self.prev_page())
        prev_button.pack(padx=0, pady=20, side=tk.LEFT)

        delete_button = tk.Button(self, text='Delete', command=lambda: self.delete_item())
        delete_button.pack(padx=0, pady=0, side=tk.BOTTOM)
        edit_button = tk.Button(self, text='Edit', command=lambda: self.edit_item())
        edit_button.pack(padx=0, pady=0, side=tk.BOTTOM)

        # Init DB connection and table
        self.book_list = m.sql_connection.sql_select("BOOKS")
        self.columns = ["ID", "Name", "Description", "Book Status", "Author ID", "Publisher ID"]
        self.table = ttk.Treeview(self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.update_table()

    def update_table(self):
        self.book_list = m.sql_connection.sql_select("BOOKS")
        self.table.delete(*self.table.get_children())
        for i in range(self.cur_page*25, (self.cur_page*25)+25):
            if i > len(self.book_list)-1:
                break
            self.table.insert("", 'end', values=self.book_list[i])
        self.table.place(x=125, y=200)

    def refresh(self):
        self.cur_page = 0
        self.update_table()

    def next_page(self):
        if self.cur_page < len(self.book_list)//25:
            self.cur_page += 1
        self.update_table()

    def prev_page(self):
        if self.cur_page > 0:
            self.cur_page -= 1
        self.update_table()

    def edit_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] != "":
            sf.frames[be.BookEditPage].target = cur_item
            sf.show_frame(be.BookEditPage)

    def delete_item(self):
        cur_item = self.table.item(self.table.focus())
        m.sql_connection.sql_delete("BOOKS", cur_item['values'][0])
        self.refresh()
