import tkinter as tk
from tkinter import font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh


class BookMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 1: book page")
        label.pack(padx=10, pady=20)
