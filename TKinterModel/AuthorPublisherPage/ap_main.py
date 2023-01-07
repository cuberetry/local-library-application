import tkinter as tk
import tkinter.font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.a_view as av
import TKinterModel.AuthorPublisherPage.a_add as aa
import TKinterModel.AuthorPublisherPage.p_view as pv
import TKinterModel.AuthorPublisherPage.p_add as pa


class AuthorPublisherMainPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')

        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="Welcome to Main Author/Publisher Page!")
        label.pack(padx=10, pady=20)

        # Choice buttons
        av_button = tk.Button(self, text='View or Edit Authors', font=def_font,
                              command=lambda: sf.show_frame(av.AuthorViewPage), height=2, width=20)
        av_button.pack(padx=10, pady=20)

        aa_button = tk.Button(self, text='Add a New Author', font=def_font,
                              command=lambda: sf.show_frame(aa.AuthorAddPage), height=2, width=20)
        aa_button.pack(padx=10, pady=20)

        pv_button = tk.Button(self, text='View or Edit Publishers', font=def_font,
                              command=lambda: sf.show_frame(pv.PublisherViewPage), height=2, width=20)
        pv_button.pack(padx=10, pady=20)

        pa_button = tk.Button(self, text='Add a New Publisher', font=def_font,
                              command=lambda: sf.show_frame(pa.PublisherAddPage), height=2, width=20)
        pa_button.pack(padx=10, pady=20)
