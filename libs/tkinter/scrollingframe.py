# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


class ScrollingFrame(tk.Frame):
    def __init__(self, _parent):
        tk.Frame.__init__(self, _parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, background='white')
        self.frame = ttk.Frame(self.canvas, style='Scrolling.TFrame')

        self.__scrollbar_y = tk.Scrollbar(self, orient="vertical", command=self.__scroll_y_action)
        self.canvas.configure(yscrollcommand=self.__scrollbar_y.set)
        self.__scrollbar_y.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.__scrollbar_x = tk.Scrollbar(self, orient="horizontal", command=self.__scroll_x_action)
        self.canvas.configure(xscrollcommand=self.__scrollbar_x.set)
        self.__scrollbar_x.grid(row=1, column=0, columnspan=2, sticky=tk.E + tk.W)

        self.canvas.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.canvas_window = self.canvas.create_window(0, 0, window=self.frame, anchor="nw", tags="self.frame")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrollbar_y_sichtbar = True

        self.frame.bind("<Configure>", self.__on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.scrollbar_x_height = self.__scrollbar_x.winfo_reqheight()
        self.scrollbar_y_width = self.__scrollbar_y.winfo_reqwidth()

    # self.update() nach jedem Scrollen, um Schlieren zu vermeiden
    def __scroll_x_action(self, _first, _second):
        self.canvas.xview(_first, _second)
        self.update()

    def __scroll_y_action(self, _first, _second):
        self.canvas.yview(_first, _second)
        self.update()

    def __on_frame_configure(self, _event):
        # Reset the scroll region to encompass the inner frame
        if _event:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, _event):
        # Resize the inner frame to match the canvas
        if _event:
            min_width = self.frame.winfo_reqwidth()
            min_height = self.frame.winfo_reqheight()

            if self.winfo_width() >= min_width:
                new_width = self.winfo_width()
                # Hide the scrollbar when not needed
                self.__scrollbar_x.grid_remove()
            else:
                new_width = min_width
                # Show the scrollbar when needed
                self.__scrollbar_x.grid()

            if self.winfo_height() >= min_height:
                new_height = self.winfo_height()
                # Hide the scrollbar when not needed
                self.__scrollbar_y.grid_remove()
                self.__scrollbar_y_sichtbar = False
            else:
                new_height = min_height
                # Show the scrollbar when needed
                self.__scrollbar_y.grid()
                self.__scrollbar_y_sichtbar = True

            self.canvas.itemconfig(self.canvas_window, width=new_width, height=new_height)

        self.frame.bind_class(
            "Canvas", "<MouseWheel>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "Canvas", "<Button-4>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "Canvas", "<Button-5>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))

    def __on_mousewheel_scroll(self, _event, _canvas):
        if self.__scrollbar_y_sichtbar:
            _canvas.yview_scroll(int(-1 * (_event.delta / 120)), "units")
