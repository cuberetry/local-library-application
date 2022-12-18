import tkinter as tk
import TKinterModel.SystemPage.sys_frame as p
import TKinterModel.SystemPage.sys_home_page as pg0
import TKinterModel.BookPage.b_main as pg1
import TKinterModel.AuthorPublisherPage.ap_main as pg2
import TKinterModel.MemberPage.m_main as pg3
import TKinterModel.LendingPage.l_main as pg4


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # configure the root window
        self.title('Local Library Application')
        self.geometry('650x550')
        self.attributes('-fullscreen', True)

        # label Title
        self.label = tk.Label(text="Local Library", font=('Times New Roman bold', 20), background="#34A2FE")
        self.label.pack(padx=10, pady=20)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        for f in (pg0.Homepage, pg1.Page1, pg2.Page2, pg3.Page3, pg4.Page4):
            frame = f(container)
            p.frames[f] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        p.show_frame(pg0.Homepage)

        # Create a Button
        self.btn_exit = tk.Button(self, text='exit', bd='5')
        self.btn_exit['command'] = self.button_clicked
        self.btn_exit.pack(side='top')

    def button_clicked(self):
        self.destroy()


