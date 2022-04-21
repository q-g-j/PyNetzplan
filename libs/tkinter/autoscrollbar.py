# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk


# AutoScrollbar-Klasse
#
# Snippet kopiert von:
# https://www.geeksforgeeks.org/autohiding-scrollbars-using-python-tkinter/

# Creating class AutoScrollbar
class AutoScrollbar(ttk.Scrollbar):

    # Defining set method with all
    # its parameter
    def set(self, low, high):

        if float(low) <= 0.0 and float(high) >= 1.0:

            # Using grid_remove
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, low, high)

    # Defining pack method
    def pack(self, **kw):
        # If pack is used it throws an error
        raise (tk.TclError, "pack cannot be used with \
        this widget")

    # Defining place method
    def place(self, **kw):

        # If place is used it throws an error
        raise (tk.TclError, "place cannot be used  with \
        this widget")
