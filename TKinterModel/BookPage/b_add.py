import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.SystemPage.sys_select as ss
import TKinterModel.BookPage.b_main as bm
import TKinterModel.BookPage.b_view as bv
import __main__ as m


class BookAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
        self.tg_author = None
        self.tg_publisher = None
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Book Page',
                                command=lambda: sf.show_frame(bm.BookMainPage))
        book_button.pack(padx=10, pady=20)

        # Book name field
        self.book_name_label = tk.Label(self, text="Enter Book Name*")
        self.book_name_label.pack(padx=10, pady=2)

        self.book_name_entry = tk.Entry(self)
        self.book_name_entry.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=2)

        # Book description field
        self.book_des_label = tk.Label(
            self, text="Enter Book Description")
        self.book_des_label.pack(padx=10, pady=2)

        self.book_des_entry = tk.Text(self, width=60, height=4)
        self.book_des_entry.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=2)

        # Author field
        self.author_label = tk.Label(self, text="No author selected")
        self.author_id_button = tk.Button(self, text="Select a author*",
                                        command=lambda: self.select_item("AUTHOR", self.author_label))
        self.author_id_button.pack(padx=10, pady=2)
        self.author_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=2)

        # Publisher field
        self.publisher_label = tk.Label(self, text="No publisher selected")
        self.publisher_id_button = tk.Button(self, text="Select a publisher*",
                                        command=lambda: self.select_item("PUBLISHER", self.publisher_label))
        self.publisher_id_button.pack(padx=10, pady=2)
        self.publisher_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=2)

        # Submit button
        self.submit_button = tk.Button(
            self, text='Submit', command=lambda: self.add_to_sql())
        self.submit_button.pack(padx=10, pady=20)

        # Error message
        self.error_label = tk.Label(self, text=self.error_msg, fg='IndianRed1')
        self.error_label.pack(padx=10, pady=5)

    def add_to_sql(self):
        bk_name = self.book_name_entry.get()
        bk_des = self.book_des_entry.get("1.0", "end")

        # Check if Book Name is empty
        if bk_name == '' or self.tg_author is None or self.tg_publisher is None:
            self.error_msg = "Please fill all the required field(s)!"
            self.error_label.config(text=self.error_msg)
            return
        # Limit Book Description input characters
        elif len(bk_des) > 200:
            self.error_msg = "Text exceeded 200 characters"
            self.error_label.config(text=self.error_msg)
            return

        auth_id = self.tg_author['values'][0]
        pub_id = self.tg_publisher['values'][0]

        # Empty input field
        self.book_name_entry.delete(0, "end")
        self.book_des_entry.delete('1.0', "end")
        self.tg_author = None
        self.tg_publisher = None
        self.author_label.config(text="No author selected")
        self.publisher_label.config(text="No publisher selected")
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)

        # Insert to SQL
        m.sql_connection.sql_insert(
            'BOOKS', {'b_name': bk_name, 'b_desc': bk_des, 'a_id': auth_id, 'p_id': pub_id})

        # Return user to book page
        sf.frames[bv.BookViewPage].refresh()
        sf.show_frame(bv.BookViewPage)

    @staticmethod
    def select_item(table, label):
        sf.frames[ss.SelectionPage].db_table = table
        sf.frames[ss.SelectionPage].prev_page = BookAddPage
        sf.frames[ss.SelectionPage].label = label
        sf.frames[ss.SelectionPage].cur_page = 0
        sf.frames[ss.SelectionPage].refresh()
        sf.show_frame(ss.SelectionPage)