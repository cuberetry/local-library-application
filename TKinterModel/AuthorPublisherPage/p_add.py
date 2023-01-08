import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import TKinterModel.AuthorPublisherPage.p_view as pv
import __main__ as m


class PublisherAddPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.error_msg = ''
        self.home_button = tk.Button(self, text='Homepage',
                                     command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.book_button = tk.Button(self, text='Author/Publisher Page',
                                     command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        self.book_button.pack(padx=10, pady=20)

        self.p_name_l = tk.Label(self, text='Enter Publisher Name')
        self.p_name_l.pack(padx=10, pady=2)

        self.p_name_e = tk.Entry(self)
        self.p_name_e.pack(padx=10, pady=2)

        self.p_submit = tk.Button(
            self, text='Submit', command=lambda: self.p_add())
        self.p_submit.pack(padx=10, pady=20)

        self.error_label = tk.Label(self, text="", fg="IndianRed1")
        self.error_label.pack(padx=10, pady=2)

    def p_add(self):
        p_name = self.p_name_e.get()

        # Handling input fields
        if p_name == '':
            self.error_msg = "Please fill all the required field(s)!"
            self.error_label.config(text=self.error_msg)
            return
        elif len(p_name) > 100:
            self.error_msg = "Name exceeded 100 characters"
            self.error_label.config(text=self.error_msg)
            return
        else:
            self.error_label.config(text="")

        # Empty input field
        self.p_name_e.delete(0, "end")

        # Insert to SQL
        m.sql_connection.sql_insert("PUBLISHER", {"p_name": p_name})

        # Return user to publisher page
        sf.frames[pv.PublisherViewPage].refresh()
        sf.show_frame(pv.PublisherViewPage)
