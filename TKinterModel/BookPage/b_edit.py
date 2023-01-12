import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.SystemPage.sys_select as ss
import TKinterModel.BookPage.b_main as bm
import TKinterModel.BookPage.b_view as bv
import __main__ as m


class BookEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.tg_author = None
        self.tg_publisher = None

        self.home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Book Page', command=lambda: sf.show_frame(bm.BookMainPage))
        self.book_button.pack(padx=10, pady=20)

        # Edit name
        self.b_name_label = tk.Label(self, text="Edit Book Name")
        self.b_name_label.pack(padx=10, pady=2)

        self.b_name = tk.StringVar()
        self.b_name_entry = tk.Entry(self, textvariable=self.b_name)
        self.b_name_entry.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        # Edit description
        self.b_desc_label = tk.Label(self, text="Edit Book Description")
        self.b_desc_label.pack(padx=10, pady=2)

        self.b_desc = tk.StringVar()
        self.b_desc_entry = tk.Text(self, width=60, height=4)
        self.b_desc_entry.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        # Edit author ID
        self.author_label = tk.Label(self, text="No author selected")
        self.author_button = tk.Button(self, text="Select author",
                                       command=lambda: sf.frames[ss.SelectionPage].show_page(
                                              "AUTHOR", BookEditPage, self.author_label)
                                       )
        self.author_button.pack(padx=10, pady=2)
        self.author_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        # Edit publisher ID
        self.publisher_label = tk.Label(self, text="No author selected")
        self.publisher_button = tk.Button(self, text="Select publisher",
                                          command=lambda: sf.frames[ss.SelectionPage].show_page(
                                              "PUBLISHER", BookEditPage, self.publisher_label)
                                          )
        self.publisher_button.pack(padx=10, pady=2)
        self.publisher_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        self.submit_button = tk.Button(self, text='Submit',
                                       command=lambda: self.edit_book())
        self.submit_button.pack(padx=10, pady=20)

        self.error_label = tk.Label(self, text='', fg='IndianRed1')
        self.error_label.pack(padx=10, pady=5)

        self.target = None

    def edit_book(self):
        edit_dict = dict()
        if len(self.b_name_entry.get()) > 50:
            self.error_label.config(text="Name exceeded 50 characters")
            return
        if len(self.b_desc_entry.get("1.0", "end")) > 200:
            self.error_label.config(text="Description exceeded 50 characters")
            return

        if self.b_name_entry.get() != '':
            edit_dict["b_name"] = self.b_name_entry.get()
        if self.b_desc_entry.get("1.0", "end") != '\n':
            edit_dict["b_desc"] = self.b_desc_entry.get("1.0", "end")
        if self.tg_author is not None:
            edit_dict["a_id"] = self.tg_author['values'][0]
        if self.tg_publisher is not None:
            edit_dict["p_id"] = self.tg_publisher['values'][0]
        m.sql_connection.sql_update("BOOKS", self.target['values'][0], edit_dict)

        # Clear the fields
        self.b_name_entry.delete(0, "end")
        self.b_desc_entry.delete('1.0', "end")
        self.tg_author = None
        self.tg_publisher = None
        self.author_label.config(text="Not selected")
        self.publisher_label.config(text="Not selected")

        sf.frames[bv.BookViewPage].refresh()
        sf.show_frame(bv.BookViewPage)
    