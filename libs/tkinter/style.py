# -*- coding: utf-8 -*-

from tkinter import ttk

from libs.common import Common
from libs.tkinter.fonts import Fonts


class Style:
    def __init__(self):
        pass

    @staticmethod
    def set_theme(root):
        root.tk.call("source", Common.script_path + "/themes/sun-valley/sun-valley.tcl")
        root.tk.call("set_theme", "dark")

    @staticmethod
    def set_styles():
        fonts = Fonts()
        style = ttk.Style()
        style.configure(
            "Header.Treeview",
            font=fonts.font_table
        )
        style.configure(
            "Header.Treeview.Heading",
            font=fonts.font_header
        )
        style.configure(
            "Normal.TButton",
            font=fonts.font_main
        )
        style.configure(
            "Accent.TButton",
            font=fonts.font_main
        )
        style.configure(
            "TCheckbutton",
            font=fonts.font_main
        )
        style.configure(
            'Treeview',
            rowheight=26
        )
