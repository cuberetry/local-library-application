import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as b_main
import TKinterModel.BookPage.b_view as b_view
import TKinterModel.BookPage.b_add as b_add
import TKinterModel.BookPage.b_edit as b_edit
import TKinterModel.AuthorPublisherPage.ap_main as ap_main
import TKinterModel.AuthorPublisherPage.a_view as a_view
import TKinterModel.AuthorPublisherPage.a_add as a_add
import TKinterModel.AuthorPublisherPage.a_edit as a_edit
import TKinterModel.AuthorPublisherPage.a_remove as a_remove
import TKinterModel.AuthorPublisherPage.p_view as p_view
import TKinterModel.AuthorPublisherPage.p_edit as p_edit
import TKinterModel.AuthorPublisherPage.p_add as p_add
import TKinterModel.AuthorPublisherPage.p_remove as p_remove
import TKinterModel.MemberPage.mb_main as mb_main
import TKinterModel.MemberPage.mb_view as mb_view
import TKinterModel.MemberPage.mb_add as mb_add
import TKinterModel.MemberPage.mb_edit as mb_edit
import TKinterModel.MemberPage.mb_remove as mb_remove
import TKinterModel.LendingPage.l_main as l_main
import TKinterModel.LendingPage.l_view as l_view
import TKinterModel.LendingPage.l_add as l_add
import TKinterModel.LendingPage.l_edit as l_edit


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # configure the root window
        self.title('Local Library Application')
        self.geometry('650x550')
        self.attributes('-fullscreen', True)

        # label Title
        self.label = tk.Label(text="Local Library", font=(
            'Times New Roman bold', 20), background="#34A2FE")
        self.label.pack(padx=10, pady=20)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for f in (sh.Homepage, b_main.BookMainPage, b_view.BookViewPage, b_add.BookAddPage, b_edit.BookEditPage,
                  ap_main.AuthorPublisherMainPage, a_view.AuthorViewPage, a_add.AuthorAddPage, a_edit.AuthorEditPage,
                  a_remove.AuthorRemovePage, p_view.PublisherViewPage, p_edit.PublisherEditPage, p_add.PublisherAddPage,
                  p_remove.PublisherRemovePage, mb_main.MemberMainPage, mb_view.MemberViewPage,
                  mb_add.MemberAddPage, mb_edit.MemberEditPage, mb_remove.MemberRemovePage,
                  l_main.LendingMainPage, l_view.LendingViewPage, l_add.LendingAddPage,
                  l_edit.LendingEditPage):
            frame = f(container)
            sf.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        sf.show_frame(sh.Homepage)

        # Create a Button
        self.btn_exit = tk.Button(self, text='exit', bd='15')
        self.btn_exit['command'] = self.button_clicked
        self.btn_exit.pack(side='top')

    def button_clicked(self):
        self.destroy()
