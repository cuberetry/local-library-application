import tkinter as tk
import TKinterModel.SystemPage.sys_frame as sf
import TKinterModel.SystemPage.sys_home_page as sh
import TKinterModel.AuthorPublisherPage.ap_main as apm
import __main__ as m


class PublisherEditPage(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.home_button = tk.Button(self, text='Homepage', command=lambda: sf.show_frame(sh.Homepage))
        self.home_button.pack(padx=10, pady=20)
        self.publisher_button = tk.Button(self, text='Publisher Page', command=lambda: sf.show_frame(apm.AuthorPublisherMainPage))
        self.publisher_button.pack(padx=10, pady=20)

        # Edit name
        self.p_name_label = tk.Label(self, text="Edit Publisher Name")
        self.p_name_label.pack(padx=10, pady=2)

        self.p_name = tk.StringVar()
        self.p_name_entry = tk.Entry(self, textvariable=self.p_name)
        self.p_name_entry.pack(padx=10, pady=2)

        self.submit_button = tk.Button(self, text='Submit',
                                       command=lambda: self.edit_publisher())
        self.submit_button.pack(padx=10, pady=20)

        self.target = None

    def edit_publisher(self):
        edit_dict = dict()
        if self.p_name_entry.get() != '':
            edit_dict["p_name"] = self.p_name_entry.get()
        m.sql_connection.sql_update("PUBLISHER", self.target['values'][0], edit_dict)
