# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk


root = tk.Tk()

button = tkinter.ttk.Label(root, text="Hello World")
button.grid(column=0, row=0)

# keep the window displaying
root.mainloop()
