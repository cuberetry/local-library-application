import tkinter as tk
import TKinterModel.SystemPage.sys_frame as p
import TKinterModel.SystemPage.sys_homepage as pg0


class Page3(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        btn = tk.Button(self, text='Homepage', command=lambda: p.show_frame(pg0.Homepage))
        btn.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 3: Member page")
        label.pack(padx=10, pady=20)
