import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh


class MemberMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        btn = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        btn.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 3: Member page")
        label.pack(padx=10, pady=20)
