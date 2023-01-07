import tkinter as tk
from tkinter import font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_view as bv
import TKinterModel.BookPage.b_add as ba


class BookMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="Welcome to Main Book Page!")
        label.pack(padx=10, pady=20)

        bv_button = tk.Button(self, text='View or Edit Books', font=def_font,
                              command=lambda: sf.show_frame(bv.BookViewPage), height=2, width=20)
        bv_button.pack(padx=10, pady=20)

        ba_button = tk.Button(self, text='Add a New Book', font=def_font,
                              command=lambda: sf.show_frame(ba.BookAddPage), height=2, width=20)
        ba_button.pack(padx=10, pady=20)
