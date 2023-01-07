import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import TKinterModel.AuthorPublisherPage.p_edit as pe
import __main__ as m


class PublisherViewPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.cur_page = 0

        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Author/Publisher Page',
                                command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        book_button.pack(padx=10, pady=20)

        refresh_button = tk.Button(
            self, text='Refresh', command=lambda: self.refresh())
        refresh_button.pack(padx=10, pady=20)
        next_button = tk.Button(
            self, text='Next', command=lambda: self.next_page())
        next_button.pack(padx=5, pady=20, side=tk.RIGHT)
        prev_button = tk.Button(
            self, text='Prev', command=lambda: self.prev_page())
        prev_button.pack(padx=5, pady=20, side=tk.LEFT)

        delete_button = tk.Button(
            self, text='Delete', command=lambda: self.delete_item())
        delete_button.pack(padx=0, pady=0, side=tk.BOTTOM)
        edit_button = tk.Button(
            self, text='Edit', command=lambda: self.edit_item())
        edit_button.pack(padx=0, pady=0, side=tk.BOTTOM)

        # Init DB connection and table
        self.publisher_list = m.sql_connection.sql_select("PUBLISHER")
        self.columns = ["ID", "Name"]
        self.table = ttk.Treeview(
            self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.update_table()
        self.error_label.pack(padx=10, pady=2)

    def update_table(self):
        self.publisher_list = m.sql_connection.sql_select("PUBLISHER")
        self.table.delete(*self.table.get_children())
        for i in range(self.cur_page * 25, (self.cur_page * 25) + 25):
            if i > len(self.publisher_list) - 1:
                break
            self.table.insert("", 'end', values=self.publisher_list[i])
        self.table.pack(fill="both", expand=True, padx=10)
        self.error_label.config(text='')

    def refresh(self):
        self.cur_page = 0
        self.update_table()

    def next_page(self):
        if self.cur_page < len(self.publisher_list) // 25:
            self.cur_page += 1
        self.update_table()

    def prev_page(self):
        if self.cur_page > 0:
            self.cur_page -= 1
        self.update_table()

    def edit_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] != "":
            sf.frames[pe.PublisherEditPage].target = cur_item
            sf.show_frame(pe.PublisherEditPage)
        self.error_label.config(text='ERROR: Please select a publisher!')

    def delete_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] == '':
            self.error_label.config(text='ERROR: Please select a publisher!')
            return
        if not m.sql_connection.sql_delete("PUBLISHER", cur_item['values'][0]):
            self.error_label.config(
                text="ERROR: Cannot delete a publisher with existing book!")
            return
        self.refresh()
