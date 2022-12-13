import tkinter as tk
import TKinterModel.page as pg


class Page3(pg.Page):
    def __init__(self, *args, **kwargs):
        pg.Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3: Member page")
        label.pack(side="top", fill="both", expand=True)
