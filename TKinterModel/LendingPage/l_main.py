import tkinter as tk
import tkinter.font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.LendingPage.l_view as lv
import TKinterModel.LendingPage.l_add as la
import TKinterModel.LendingPage.l_edit as le


class LendingMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is page 4: Lending page")
        label.pack(padx=10, pady=20)

        lv_button = tk.Button(self, text='View all lending', font=def_font,
                              command=lambda: sf.show_frame(lv.LendingViewPage), height=2, width=20)
        lv_button.pack(padx=10, pady=20)

        la_button = tk.Button(self, text='Add a new lending', font=def_font,
                              command=lambda: sf.show_frame(la.LendingAddPage), height=2, width=20)
        la_button.pack(padx=10, pady=20)

        le_button = tk.Button(self, text='Update a lending', font=def_font,
                              command=lambda: sf.show_frame(le.LendingEditPage), height=2, width=20)
        le_button.pack(padx=10, pady=20)
