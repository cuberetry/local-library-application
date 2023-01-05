import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.LendingPage.l_main as lm
import TKinterModel.LendingPage.l_view as lv
import datetime as d
import __main__ as m


class LendingAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ""
        self.home_button = tk.Button(self, text='Homepage',
                                     command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Lending Page',
                                     command=lambda: sf.show_frame(lm.LendingMainPage))
        self.book_button.pack(padx=10, pady=20)

        # Book field
        self.book_id_label = tk.Label(self, text="Select a book*")
        self.book_id_label.pack(padx=10, pady=2)
        self.book_id_entry = tk.Entry(self)
        self.book_id_entry.pack(padx=10, pady=2)

        # Member field
        self.member_id_label = tk.Label(self, text="Select a member*")
        self.member_id_label.pack(padx=10, pady=2)
        self.member_id_entry = tk.Entry(self)
        self.member_id_entry.pack(padx=10, pady=2)

        # Duration field
        self.d_label = tk.Label(self, text="Enter optional day duration")
        self.d_label.pack(padx=10, pady=2)
        self.d_entry = tk.Entry(self)
        self.d_entry.pack(padx=10, pady=2)

        # Submit button
        self.submit_button = tk.Button(self, text='Submit', command=lambda: self.add_to_sql())
        self.submit_button.pack(padx=10, pady=20)

        # Error message
        self.error_label = tk.Label(self, text=self.error_msg, fg='IndianRed1')
        self.error_label.pack(padx=10, pady=20)

    def add_to_sql(self):
        b_id = self.book_id_entry.get()
        mb_id = self.member_id_entry.get()
        duration = self.d_entry.get()
        now = d.datetime.now()

        # Handling input fields
        if b_id == '' or mb_id == '':
            self.error_msg = "Please fill all the required field(s)!"
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

        # Empty input field
        self.book_id_entry.delete(0, "end")
        self.member_id_entry.delete(0, "end")

        # Return user to lending page
        sf.show_frame(lv.LendingViewPage)
