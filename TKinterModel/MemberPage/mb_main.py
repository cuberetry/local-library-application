import tkinter as tk
import tkinter.font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_view as mv
import TKinterModel.MemberPage.mb_add as ma


class MemberMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        btn = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        btn.pack(padx=10, pady=20)

        label = tk.Label(self, text="Welcome to Main Member Page!")
        label.pack(padx=10, pady=20)

        mv_button = tk.Button(self, text='View or Edit Members', font=def_font,
                              command=lambda: sf.show_frame(mv.MemberViewPage), height=2, width=20)
        mv_button.pack(padx=10, pady=20)

        ma_button = tk.Button(self, text='Register a New Member', font=def_font,
                              command=lambda: sf.show_frame(ma.MemberAddPage), height=2, width=20)
        ma_button.pack(padx=10, pady=20)
