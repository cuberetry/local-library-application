import tkinter as tk
import tkinter.font as tkf
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.LendingPage.l_view as lv
import TKinterModel.BookPage.b_view as bv
import datetime as d
import __main__ as m


class LendingEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        def_font = tkf.Font(family='Courier', size=20, weight='bold')
        self.target = None

        home_button = tk.Button(self, text='Lending view page', command=lambda: sf.show_frame(lv.LendingViewPage))
        home_button.pack(padx=10, pady=20)

        label = tk.Label(self, text="This is lending edit page")
        label.pack(padx=10, pady=20)

        confirm_button = tk.Button(self, text='Confirm', font=def_font, command=lambda: self.add_return_date(),
                                   height=2, width=20)
        confirm_button.pack(padx=10, pady=20)

        cancel_button = tk.Button(self, text='Cancel', font=def_font, command=lambda: sf.show_frame(lv.LendingViewPage),
                                  height=2, width=20)
        cancel_button.pack(padx=10, pady=20)

    def add_return_date(self):
        now = d.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')

        # Insert to SQL
        m.sql_connection.sql_update('LENDING', self.target['values'][0], {'l_return_date': now})
        # Update book status
        book_id = m.sql_connection.sql_select('LENDING', 'b_id', {'l_id': self.target['values'][0]})[0][0]
        m.sql_connection.sql_update('BOOKS', book_id, {'b_status': 1})

        # Return user to lending page
        sf.frames[bv.BookViewPage].refresh()
        sf.frames[lv.LendingViewPage].refresh()
        sf.show_frame(lv.LendingViewPage)
