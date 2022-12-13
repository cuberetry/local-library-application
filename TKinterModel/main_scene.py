import tkinter as tk
import TKinterModel.page1_book as pg1
import TKinterModel.page2_author_publisher as pg2
import TKinterModel.page3_member as pg3
import TKinterModel.page4_lending as pg4


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Local Library Application')
        self.geometry('650x550')
        self.attributes('-fullscreen', True)

        # label Title
        self.label = tk.Label(text="Local Library", font=('Times New Roman bold', 20), background="#34A2FE")
        self.label.pack(padx=10, pady=20)

        self.main = MainView(self)
        self.main.pack(side="top", fill="both", expand=True)

        # Create a Button
        self.btn_exit = tk.Button(self, text='exit', bd='5')
        self.btn_exit['command'] = self.button_clicked
        self.btn_exit.pack(side='top')

    def button_clicked(self):
        self.destroy()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = pg1.Page1(self)
        p2 = pg2.Page2(self)
        p3 = pg3.Page3(self)
        p4 = pg4.Page4(self)

        btn_frame = tk.Frame(self)
        container = tk.Frame(self)
        btn_frame.pack(side="top", pady='5')
        container.pack(side="top", fill="both", expand=True)

        b1 = tk.Button(btn_frame, text="Page 1", command=p1.show)
        b2 = tk.Button(btn_frame, text="Page 2", command=p2.show)
        b3 = tk.Button(btn_frame, text="Page 3", command=p3.show)
        b4 = tk.Button(btn_frame, text="Page 4", command=p4.show)

        b1.pack(side='left')
        b2.pack(side='left')
        b3.pack(side='left')
        b4.pack(side='left')

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        p1.show()
