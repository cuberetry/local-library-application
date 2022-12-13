import tkinter as tk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('Local Library Application')
        self.geometry('650x550')
        self.attributes('-fullscreen', True)

        # label Title
        self.label = tk.Label(text="Local Library", font=('Times New Roman bold', 20), background="#34A2FE")
        self.label.pack(padx=10, pady=10)

        # Create a Button
        self.btn = tk.Button(self, text='Click me !', bd='5')
        self.btn['command'] = self.buttton_clicked
        self.btn.pack(side='top')

    def buttton_clicked(self):
        showinfo(showinfo='information', message='hello')


if __name__ == "__main__":
  app = App()
  app.mainloop()
