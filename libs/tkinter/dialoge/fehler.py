# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.fonts import Fonts


class FehlerDialoge:
    def __init__(self, _root):
        self.__root = _root

    def vorgaenger_rekursions_fehler(self, rekursionsfehler_liste):
        fonts = Fonts()
        toplevel = tk.Toplevel(self.__root)
        toplevel.resizable(width=False, height=False)
        toplevel.wm_transient(self.__root)
        toplevel.grab_set()
        toplevel.config(padx=2, pady=2)
        toplevel.title("Fehler!")

        label_titel = ttk.Label(toplevel, text="Fehler!", font=fonts.font_title, foreground="red")
        label_titel.grid(column=0, row=0, padx=2, pady=2)
        label_leer_1 = ttk.Label(toplevel, text=" ")
        label_leer_1.grid(column=0, row=1, padx=2, pady=2, sticky="w")
        label_grund = ttk.Label(toplevel,
                                text="Ein Vorgang darf nicht ein Vorgänger einer seiner eigenen Vorgänger sein!",
                                font=fonts.font_main, foreground="red")
        label_grund.grid(column=0, row=2, padx=2, pady=2, sticky="w")
        label_leer_2 = ttk.Label(toplevel, text=" ")
        label_leer_2.grid(column=0, row=3, padx=2, pady=2, sticky="w")
        label_liste = ttk.Label(toplevel, text="Überprüfe folgende Kombinationen von Vorgängen / Vorgängern:",
                                font=fonts.font_main)
        label_liste.grid(column=0, row=4, padx=2, pady=2, sticky="w")
        label_leer_2 = ttk.Label(toplevel, text=" ")
        label_leer_2.grid(column=0, row=5, padx=2, pady=2, sticky="w")

        row = 6
        for listenindex in range(len(rekursionsfehler_liste)):
            label = ttk.Label(toplevel, text="Vorgang: " + str(rekursionsfehler_liste[listenindex][0]) +
                                             ", Vorgänger: " + str(rekursionsfehler_liste[listenindex][1]),
                              font=fonts.font_main)
            label.grid(column=0, row=row, padx=2, pady=2, sticky="w")
            if listenindex % 2 != 0 and listenindex != len(rekursionsfehler_liste) - 1:
                label_leer = ttk.Label(toplevel, text=" ")
                label_leer.grid(column=0, row=row + 1, padx=2, pady=2, sticky="w")
                row += 2
            else:
                row += 1

        TkCommon.center(toplevel)
