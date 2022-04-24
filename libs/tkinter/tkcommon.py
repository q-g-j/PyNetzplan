# -*- coding: utf-8 -*-


class TkCommon:
    @staticmethod
    def center(window):
        window.update_idletasks()
        width = window.winfo_width()
        frm_width = window.winfo_rootx() - window.winfo_x()
        win_width = width + 2 * frm_width
        height = window.winfo_height()
        titlebar_height = window.winfo_rooty() - window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = window.winfo_screenwidth() // 2 - win_width // 2
        y = window.winfo_screenheight() // 2 - win_height // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

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
