# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.tkinter.tkcommon import TkCommon


class Netzplan:
    def __init__(self, _root):
        self.__root = _root

        self.__toplevel = None

    def erstelle_fenster(self):
        self.__toplevel = tk.Toplevel(self.__root)
        self.__toplevel.wm_transient(self.__root)
        self.__toplevel.grab_set()
        self.__toplevel.config(padx=2, pady=2)
        self.__toplevel.title("Netzplan")
        TkCommon.center(self.__toplevel)


class NetzplanVorgang:
    def __init__(self):
        pass
