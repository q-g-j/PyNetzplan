# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


class ScrollingFrame(ttk.Frame):
    def __init__(self, _parent):
        ttk.Frame.__init__(self, _parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, background='white')
        self.frame = ttk.Frame(self.canvas, style='Scrolling.TFrame')

        self.__scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.__scrollbar_y.set)
        self.__scrollbar_y.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.__scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.__scrollbar_x.set)
        self.__scrollbar_x.grid(row=1, column=0, sticky=tk.E + tk.W)

        self.canvas.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.__canvas_window = self.canvas.create_window(0, 0, window=self.frame, anchor="nw", tags="self.frame")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrollbar_y_sichtbar = True

        self.frame.bind("<Configure>", self.__on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

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

            self.canvas.itemconfig(self.__canvas_window, width=new_width, height=new_height)

        self.canvas.bind(
            "<MouseWheel>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.canvas.bind(
            "<Button-4>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.canvas.bind(
            "<Button-5>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))

        self.frame.bind(
            "<MouseWheel>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind(
            "<Button-4>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind(
            "<Button-5>", lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))

        self.frame.bind_class(
            "TFrame", "<MouseWheel>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "TFrame", "<Button-4>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "TFrame", "<Button-5>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))

        self.frame.bind_class(
            "TLabel", "<MouseWheel>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "TLabel", "<Button-4>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))
        self.frame.bind_class(
            "TLabel", "<Button-5>",
            lambda event, c=self.canvas: self.__on_mousewheel_scroll(event, c))

    def __on_mousewheel_scroll(self, _event, _canvas):
        if self.__scrollbar_y_sichtbar:
            _canvas.yview_scroll(int(-1 * (_event.delta / 120)), "units")
