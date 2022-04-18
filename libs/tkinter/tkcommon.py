# -*- coding: utf-8 -*-

from tkinter import ttk

from libs.common import Common
from libs.tkinter.fonts import Fonts


class TkCommon:

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
            font=fonts.font_main
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

    @staticmethod
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()

    @staticmethod
    def tab_pressed(event):
        event.widget.tk_focusNext().focus()
        return "break"

    @staticmethod
    def hover_button(event, button):
        if event:
            button.configure(style="Accent.TButton")
        return "break"

    @staticmethod
    def leave_button(event, button):
        if event:
            button.configure(style="Normal.TButton")
        return "break"
