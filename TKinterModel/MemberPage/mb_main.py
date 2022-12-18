import tkinter as tk
import tkinter.font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.MemberPage.mb_view as mv
import TKinterModel.MemberPage.mb_add as ma
import TKinterModel.MemberPage.mb_edit as me
import TKinterModel.MemberPage.mb_remove as mr


class MemberMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        btn = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        btn.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 3: Member page")
        label.pack(padx=10, pady=20)

        mv_button = tk.Button(self, text='View all members', font=def_font,
                              command=lambda: sf.show_frame(mv.MemberViewPage), height=2, width=20)
        mv_button.pack(padx=10, pady=20)

        ma_button = tk.Button(self, text='Register a new member', font=def_font,
                              command=lambda: sf.show_frame(ma.MemberAddPage), height=2, width=20)
        ma_button.pack(padx=10, pady=20)

        me_button = tk.Button(self, text='Edit member information', font=def_font,
                              command=lambda: sf.show_frame(me.MemberEditPage), height=2, width=20)
        me_button.pack(padx=10, pady=20)

        mr_button = tk.Button(self, text='Delete a member', font=def_font,
                              command=lambda: sf.show_frame(mr.MemberRemovePage), height=2, width=20)
        mr_button.pack(padx=10, pady=20)
