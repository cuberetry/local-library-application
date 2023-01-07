import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import __main__ as m


class SelectionPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.target = None
        self.prev_page = None
        self.db_table = None
        self.list = None
        self.cur_page = 0
        self.label = None

        # Prev page button
        self.home_button = tk.Button(
            self, text='Previous Page', command=lambda: sf.show_frame(self.prev_page))
        self.home_button.pack(padx=10, pady=20)

        # Confirm button
        self.select_button = tk.Button(
            self, text='Confirm', command=lambda: self.select_item())
        self.select_button.pack(padx=0, pady=0, side=tk.BOTTOM)

        # Navigation
        self.next_button = tk.Button(
            self, text='Next', command=lambda: self.goto_next_page())
        self.next_button.pack(padx=0, pady=20, side=tk.RIGHT)
        self.prev_button = tk.Button(
            self, text='Prev', command=lambda: self.goto_prev_page())
        self.prev_button.pack(padx=0, pady=20, side=tk.LEFT)

        # Init DB connection and table
        self.columns = None
        self.table = None

    def update_table(self):
        self.cur_page = 0
        self.refresh()

    def refresh(self):
        self.columns = None
        if self.table is not None:
            self.table.destroy()
        if self.db_table == 'BOOKS':
            self.columns = ["ID", "Name", "Description",
                            "Book Status", "Author ID", "Publisher ID"]
            self.list = m.sql_connection.sql_select(self.db_table)
        elif self.db_table == 'MEMBERS':
            self.columns = ["ID", "Name", "Surname", "Age", "Phone", "E-mail"]
            self.list = m.sql_connection.sql_select(self.db_table, ('mb_id', 'mb_fname', 'mb_lname',
                                                                    'mb_age', 'mb_phone', 'mb_email'))
        elif self.db_table == 'AUTHOR':
            self.columns = ["ID", "Name", "Surname"]
            self.list = m.sql_connection.sql_select(self.db_table)
        elif self.db_table == 'PUBLISHER':
            self.columns = ["ID", "Name"]
            self.list = m.sql_connection.sql_select(self.db_table)
        self.table = ttk.Treeview(
            self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.table.delete(*self.table.get_children())
        for i in range(self.cur_page * 25, (self.cur_page * 25) + 25):
            if i > len(self.list) - 1:
                break
            self.table.insert("", 'end', values=self.list[i])
        self.table.pack(fill="both", padx=10)

    def goto_next_page(self):
        if self.cur_page < len(self.list) // 25:
            self.cur_page += 1
        self.refresh()

    def goto_prev_page(self):
        if self.cur_page > 0:
            self.cur_page -= 1
        self.refresh()

    def select_item(self):
        if self.db_table == 'BOOKS':
            sf.frames[self.prev_page].tg_book = self.table.item(
                self.table.focus())
            self.label.config(
                text=sf.frames[self.prev_page].tg_book['values'][1])
        if self.db_table == 'MEMBERS':
            sf.frames[self.prev_page].tg_member = self.table.item(
                self.table.focus())
            self.label.config(text=sf.frames[self.prev_page].tg_member['values']
                              [1] + " " + sf.frames[self.prev_page].tg_member['values'][2])
        if self.db_table == 'AUTHOR':
            sf.frames[self.prev_page].tg_author = self.table.item(
                self.table.focus())
            self.label.config(text=sf.frames[self.prev_page].tg_author['values']
                              [1] + " " + sf.frames[self.prev_page].tg_author['values'][2])
        if self.db_table == 'PUBLISHER':
            sf.frames[self.prev_page].tg_publisher = self.table.item(
                self.table.focus())
            self.label.config(
                text=sf.frames[self.prev_page].tg_publisher['values'][1])
        sf.show_frame(self.prev_page)
        self.target = None
        self.prev_page = None
        self.db_table = None
        self.list = None
        self.cur_page = 0
        # self.table = None
        self.label = None

    def show_page(self, table_name=str, prev_page=tk.Frame, label=tk.Label):
        self.db_table = table_name
        self.prev_page = prev_page
        self.label = label
        self.update_table()
        sf.show_frame(SelectionPage)
