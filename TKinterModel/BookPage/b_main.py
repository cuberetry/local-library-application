import tkinter as tk
from tkinter import font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_view as bv
import TKinterModel.BookPage.b_add as ba
import TKinterModel.BookPage.b_edit as be
import TKinterModel.BookPage.b_remove as br


class BookMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 1: book page")
        label.pack(padx=10, pady=20)

        bv_button = tk.Button(self, text='View all books', font=def_font,
                              command=lambda: sf.show_frame(bv.BookViewPage), height=2, width=20)
        bv_button.pack(padx=10, pady=20)

        ba_button = tk.Button(self, text='Add a new book', font=def_font,
                              command=lambda: sf.show_frame(ba.BookAddPage), height=2, width=20)
        ba_button.pack(padx=10, pady=20)

        be_button = tk.Button(self, text='Edit a book', font=def_font,
                              command=lambda: sf.show_frame(be.BookEditPage), height=2, width=20)
        be_button.pack(padx=10, pady=20)

        br_button = tk.Button(self, text='Remove a book', font=def_font,
                              command=lambda: sf.show_frame(br.BookRemovePage), height=2, width=20)
        br_button.pack(padx=10, pady=20)

