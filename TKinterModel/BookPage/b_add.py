import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.BookPage.b_main as bm
import __main__ as m


class BookAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        home_button = tk.Button(self, text='Homepage',
                                command=lambda: sf.show_frame(sh.Homepage))
        home_button.pack(padx=10, pady=20)
        book_button = tk.Button(self, text='Book Page',
                                command=lambda: sf.show_frame(bm.BookMainPage))
        book_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is book add page")
        label.pack(padx=10, pady=20)

        self.book_name_label = tk.Label(self, text="Add Book Name*")
        self.book_name_label.pack(padx=10, pady=2)

        self.book_name_entry = tk.Entry(self)
        self.book_name_entry.pack(padx=10, pady=2)

        self.book_des_label = tk.Label(
            self, text="Add Book Description (Max 200 Chatacters)")
        self.book_des_label.pack(padx=10, pady=2)

        self.book_des_entry = tk.Text(self, width=60, height=4)
        self.book_des_entry.pack(padx=10, pady=2)

        self.author_id_label = tk.Label(self, text="Author ID*")
        self.author_id_label.pack(padx=10, pady=2)

        self.author_id_entry = tk.Entry(self)
        self.author_id_entry.pack(padx=10, pady=2)

        self.publisher_id_label = tk.Label(self, text="Publisher ID*")
        self.publisher_id_label.pack(padx=10, pady=2)

        self.publisher_id_entry = tk.Entry(self)
        self.publisher_id_entry.pack(padx=10, pady=2)

        self.submit_button = tk.Button(
            self, text='Submit', command=lambda: self.add_to_SQL())
        self.submit_button.pack(padx=10, pady=20)

        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.error_label.pack(padx=10, pady=2)

    def add_to_SQL(self):
        bk_name = self.book_name_entry.get()
        bk_des = self.book_des_entry.get("1.0", "end")
        auth_id = self.author_id_entry.get()
        pub_id = self.publisher_id_entry.get()

        # Check if Book Name is empty
        if len(bk_name) <= 0 or len(auth_id) <= 0 or len(pub_id) <= 0:
            self.error_label.config(
                text="Please fill the all the required field(s)")
            return
        # Limit Book Description input characters
        elif len(bk_des) > 201:
            self.error_label.config(text="Text exceeded 200 characters")
            return
        # Clear error msg
        else:
            self.error_label.config(text="")

        # Empty input field
        self.book_name_entry.delete(0, "end")
        self.book_des_entry.delete('1.0', "end")
        self.author_id_entry.delete(0, "end")
        self.publisher_id_entry.delete(0, "end")

        # Insert to SQL
        m.sql_connection.sql_insert(
            'BOOKS', {'b_name': bk_name, 'b_desc': bk_des, 'a_id': auth_id, 'p_id': pub_id})
