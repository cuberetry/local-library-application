import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as bm


class BookEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Book Page', command=lambda: sf.show_frame(bm.BookMainPage))
        book_button.pack(padx=10, pady=20)

        # Edit name
        b_name_label = tk.Label(self, text="Edit Book Name")
        b_name_label.pack(padx=10, pady=2)

        b_name = tk.StringVar()
        b_name_entry = tk.Entry(self, textvariable=b_name)
        b_name_entry.pack(padx=10, pady=2)

        # Edit description
        b_desc_label = tk.Label(self, text="Edit Book Description")
        b_desc_label.pack(padx=10, pady=2)

        b_desc = tk.StringVar()
        b_desc_entry = tk.Entry(self, textvariable=b_desc)
        b_desc_entry.pack(padx=10, pady=2)

        # Edit author ID
        a_id_label = tk.Label(self, text="Edit Author ID")
        a_id_label.pack(padx=10, pady=2)

        a_id = tk.StringVar()
        a_id_entry = tk.Entry(self, textvariable=a_id)
        a_id_entry.pack(padx=10, pady=2)

        # Edit publisher ID
        p_id_label = tk.Label(self, text="Edit Publisher ID")
        p_id_label.pack(padx=10, pady=2)

        p_id = tk.StringVar()
        p_id_entry = tk.Entry(self, textvariable=p_id)
        p_id_entry.pack(padx=10, pady=2)

        submit_button = tk.Button(self, text='Submit',
                                  command=lambda: self.edit_book())
        submit_button.pack(padx=10, pady=20)

        self.target = None

    def edit_book(self):
        print(self.target)
