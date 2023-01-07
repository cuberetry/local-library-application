import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.SystemPage.sys_select as ss
import TKinterModel.LendingPage.l_main as lm
import TKinterModel.LendingPage.l_view as lv
import datetime as d
import __main__ as m


class LendingAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
        self.tg_book = None
        self.tg_member = None

        self.home_button = tk.Button(self, text='Homepage',
                                     command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Lending Page',
                                     command=lambda: sf.show_frame(lm.LendingMainPage))
        self.book_button.pack(padx=10, pady=20)

        self.space = tk.Label(self)
        self.space.pack(pady=10)

        # Book field
        self.book_label = tk.Label(self, text="No book selected")
        self.book_id_button = tk.Button(self, text="Select a book*",
                                        command=lambda: sf.frames[ss.SelectionPage].show_page(
                                            "BOOKS", LendingAddPage, self.book_label)
                                        )
        self.book_id_button.pack(padx=10, pady=2)
        self.book_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        # Member field
        self.member_label = tk.Label(self, text="No member selected")
        self.member_id_button = tk.Button(self, text="Select a member*",
                                          command=lambda: sf.frames[ss.SelectionPage].show_page(
                                            "MEMBERS", LendingAddPage, self.member_label)
                                          )
        self.member_id_button.pack(padx=10, pady=2)
        self.member_label.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=5)

        # Duration field
        self.d_label = tk.Label(self, text="Enter day(s) duration")
        self.d_label.pack(padx=10, pady=2)
        self.d_entry = tk.Entry(self)
        self.d_entry.pack(padx=10, pady=2)

        self.space = tk.Label(self)
        self.space.pack(pady=10)

        # Submit button
        self.submit_button = tk.Button(self, text='Submit', command=lambda: self.add_to_sql())
        self.submit_button.pack(padx=10, pady=20)

        # Error message
        self.error_label = tk.Label(self, text=self.error_msg, fg='IndianRed1')
        self.error_label.pack(padx=10, pady=20)

    def add_to_sql(self):
        # Handling input fields
        if self.tg_book is None or self.tg_member is None:
            self.error_msg = "Please fill all the required field(s)!"
            self.error_label.config(text=self.error_msg)
            return

        b_id = self.tg_book['values'][0]
        mb_id = self.tg_member['values'][0]
        duration = self.d_entry.get()
        now = d.datetime.now()

        if self.tg_book['values'][3] == False:
            self.error_msg == "Book not available for lending!"
            self.error_label.config(text=self.error_msg)
            return
            

        try:
            if duration == '':
                duration = 14
            duration = int(duration)
            if duration <= 0:
                self.error_msg = "Please enter a valid duration!"
                self.error_label.config(text=self.error_msg)
                return
        except ValueError:
            self.error_msg = "Please enter a valid duration!"
            self.error_label.config(text=self.error_msg)
            return

        # Handling date
        lsd = now
        ldd = now + d.timedelta(days=duration)

        lsd = lsd.strftime('%Y-%m-%d %H:%M:%S')
        ldd = ldd.strftime('%Y-%m-%d')

        # Insert to SQL
        m.sql_connection.sql_insert('LENDING',
                                    {'l_start_date': lsd, 'l_due_date': ldd,
                                     'mb_id': mb_id, 'b_id': b_id})
        # Update book status
        m.sql_connection.sql_update("BOOKS", self.tg_book['values'][0], {'b_status': False})


        # Empty input field
        self.tg_book = None
        self.tg_member = None
        self.book_label.config(text="Not selected")
        self.member_label.config(text="Not selected")
        self.error_msg = ""
        self.error_label.config(text=self.error_msg)

        # Return user to lending page
        sf.frames[lv.LendingViewPage].refresh()
        sf.show_frame(lv.LendingViewPage)
