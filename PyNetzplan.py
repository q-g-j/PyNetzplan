# -*- coding: utf-8 -*-

import tkinter as tk

from libs.common import Common
from libs.tkinter.mainwindow import Mainwindow


root = tk.Tk()
# root.resizable(width=False, height=False)
root.title("PyNetzplan")

root.geometry("1330x800")
root.minsize(600, 400)

Common.set_script_path()

Mainwindow(root)

# keep the window displaying
root.mainloop()
