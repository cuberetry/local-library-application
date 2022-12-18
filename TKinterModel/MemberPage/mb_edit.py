import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_main as mm


class MemberEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Member Page', command=lambda: sf.show_frame(mm.MemberMainPage))
        book_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is member edit page")
        label.pack(padx=10, pady=20)
