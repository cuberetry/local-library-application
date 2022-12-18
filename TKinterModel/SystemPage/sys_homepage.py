import tkinter as tk
from tkinter import font as tkf
import TKinterModel.SystemPage.sys_page as p
import TKinterModel.BookPage.b_main as pg1
import TKinterModel.AuthorPublisherPage.ap_main as pg2
import TKinterModel.MemberPage.m_main as pg3
import TKinterModel.LendingPage.l_main as pg4


class Homepage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        label = tk.Label(self, text="This is Home Page")
        label.pack(padx=10, pady=20)

        # btn
        btn1 = tk.Button(self, text='Book', font=def_font, command=lambda: p.show_frame(pg1.Page1), height=2, width=20)
        btn1.pack(padx=10, pady=20)

        btn2 = tk.Button(self, text='Author and Publisher', font=def_font, command=lambda: p.show_frame(pg2.Page2), height=2, width=20)
        btn2.pack(padx=10, pady=20)

        btn3 = tk.Button(self, text='Member', font=def_font, command=lambda: p.show_frame(pg3.Page3), height=2, width=20)
        btn3.pack(padx=10, pady=20)

        btn4 = tk.Button(self, text='Lending', font=def_font, command=lambda: p.show_frame(pg4.Page4), height=2, width=20)
        btn4.pack(padx=10, pady=20)
