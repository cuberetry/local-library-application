import tkinter as tk
from tkinter import ttk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_main as mm
import TKinterModel.MemberPage.mb_edit as me
import __main__ as m


class MemberViewPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.cur_page = 0

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        member_button = tk.Button(self, text='Member Page', command=lambda: sf.show_frame(mm.MemberMainPage))
        member_button.pack(padx=10, pady=20)

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
        self.member_list = m.sql_connection.sql_select("MEMBERS")
        self.columns = ["mb_id", "mb_fname", "mb_lname", "mb_age", "mb_birthday", "mb_phone", "mb_email",
                        "mb_national_id", "mb_passport_id", "mb_address"]
        self.table = ttk.Treeview(self, columns=self.columns, show="headings", height=27)
        for col in self.columns:
            self.table.heading(col, text=col.title())
        self.update_table()

    def update_table(self):
        self.member_list = m.sql_connection.sql_select("MEMBERS")
        self.table.delete(*self.table.get_children())
        for i in range(self.cur_page * 25, (self.cur_page * 25) + 25):
            if i > len(self.member_list) - 1:
                break
            self.table.insert("", 'end', values=self.member_list[i])
        self.table.pack(fill="both", expand=True)

    def refresh(self):
        self.cur_page = 0
        self.update_table()

    def next_page(self):
        if self.cur_page < len(self.member_list) // 25:
            self.cur_page += 1
        self.update_table()

    def prev_page(self):
        if self.cur_page > 0:
            self.cur_page -= 1
        self.update_table()

    def edit_item(self):
        cur_item = self.table.item(self.table.focus())
        if cur_item['values'] != "":
            sf.frames[me.MemberEditPage].target = cur_item
            sf.show_frame(me.MemberEditPage)

    def delete_item(self):
        cur_item = self.table.item(self.table.focus())
        m.sql_connection.sql_delete("MEMBERS", cur_item['values'][0])
        self.refresh()
