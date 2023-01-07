import tkinter as tk
from tkinter import font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.BookPage.b_main as b_main
import TKinterModel.AuthorPublisherPage.ap_main as ap_main
import TKinterModel.MemberPage.mb_main as mb_main
import TKinterModel.LendingPage.l_main as l_main


class Homepage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        label = tk.Label(self, text="Welcome to the Homepage!")
        label.pack(padx=10, pady=20)

        # btn
        b_button = tk.Button(self, text='Book', font=def_font,
                             command=lambda: sf.show_frame(b_main.BookMainPage), height=2, width=20)
        b_button.pack(padx=10, pady=20)

        ap_button = tk.Button(self, text='Author and Publisher', font=def_font,
                              command=lambda: sf.show_frame(ap_main.AuthorPublisherMainPage), height=2, width=20)
        ap_button.pack(padx=10, pady=20)

        mb_button = tk.Button(self, text='Member', font=def_font,
                              command=lambda: sf.show_frame(mb_main.MemberMainPage), height=2, width=20)
        mb_button.pack(padx=10, pady=20)

        l_button = tk.Button(self, text='Lending', font=def_font,
                             command=lambda: sf.show_frame(l_main.LendingMainPage), height=2, width=20)
        l_button.pack(padx=10, pady=20)
