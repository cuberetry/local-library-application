import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.LendingPage.l_main as lm
import TKinterModel.LendingPage.l_edit as le
import __main__ as m


class LendingViewPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.cur_page = 0

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Lending Page', command=lambda: sf.show_frame(lm.LendingMainPage))
        book_button.pack(padx=10, pady=20)

        refresh_button = tk.Button(self, text='Refresh', command=lambda: self.refresh())
        refresh_button.pack(padx=10, pady=20)
        next_button = tk.Button(self, text='Next', command=lambda: self.next_page())
        next_button.pack(padx=0, pady=20, side=tk.RIGHT)
        prev_button = tk.Button(self, text='Prev', command=lambda: self.prev_page())
        prev_button.pack(padx=0, pady=20, side=tk.LEFT)

        delete_button = tk.Button(self, text='Delete', command=lambda: self.delete_item())
        delete_button.pack(padx=0, pady=0, side=tk.BOTTOM)
        edit_button = tk.Button(self, text='Return', command=lambda: self.return_item())
        edit_button.pack(padx=0, pady=0, side=tk.BOTTOM)

        # Init DB connection and table
        self.lending_list = m.sql_connection.sql_select_joint_fk("LENDING")
        self.columns = ["ID", "Start Date", "Due Date", "Return Date", "Member", "Book"]
        self.table = ttk.Treeview(self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.update_table()
        self.error_label.pack(padx=10, pady=2)

    def update_table(self):
        self.lending_list = m.sql_connection.sql_select_joint_fk("LENDING")
        self.table.delete(*self.table.get_children())
        for i in range(self.cur_page*25, (self.cur_page*25)+25):
            if i > len(self.lending_list)-1:
                break
            self.table.insert("", 'end', values=self.lending_list[i])
        self.table.pack(fill="both", expand=True)
        self.error_label.config(text='')

    def refresh(self):
        self.cur_page = 0
        self.update_table()

    def next_page(self):
        if self.cur_page < len(self.lending_list)//25:
            self.cur_page += 1
        self.update_table()

    def prev_page(self):
        if self.cur_page > 0:
            self.cur_page -= 1
        self.update_table()

    def return_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] == "":
            self.error_label.config(text='Please select a lending!')
            return
        sf.frames[le.LendingEditPage].target = cur_item
        sf.show_frame(le.LendingEditPage)
        self.error_label.config(text='')

    def delete_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] == '':
            self.error_label.config(text='Please select a lending!')
            return
        m.sql_connection.sql_delete("LENDING", cur_item['values'][0])
        self.error_label.config(text='')
        self.refresh()
