# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.fonts import Fonts


class EingabeDialoge:
    def __init__(self, _root):
        self.__root = _root
        self.__textbox_index = None
        self.__textbox_beschreibung = None
        self.__textbox_dauer = None
        self.__textbox_zeiteiheit = None
        self.__textbox_vorgaenger = None

    def neuer_vorgang(self, mainwindow):
        fonts = Fonts()
        toplevel = tk.Toplevel(self.__root)
        toplevel.resizable(width=False, height=False)
        toplevel.wm_transient(self.__root)
        toplevel.grab_set()
        toplevel.config(padx=2, pady=2)
        toplevel.title("Vorgang hinzufügen")

        label_index = ttk.Label(toplevel, text="Index:", font=fonts.font_main)
        label_beschreibung = ttk.Label(toplevel, text="Beschreibung:", font=fonts.font_main)
        label_dauer = ttk.Label(toplevel, text="Dauer:", font=fonts.font_main)
        label_zeiteinheit = ttk.Label(toplevel, text="Zeiteinheit:", font=fonts.font_main)
        label_vorgaenger = ttk.Label(toplevel, text="Vorgänger:", font=fonts.font_main)

        self.__textbox_index = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_beschreibung = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_dauer = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_zeiteiheit = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_vorgaenger = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )

        label_index.grid(column=0, row=0, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_beschreibung.grid(column=0, row=1, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_dauer.grid(column=0, row=2, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_zeiteinheit.grid(column=0, row=3, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_vorgaenger.grid(column=0, row=4, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)

        self.__textbox_index.grid(column=1, row=0, sticky="w", padx=2, pady=2)
        self.__textbox_beschreibung.grid(column=1, row=1, sticky="w", padx=2, pady=2)
        self.__textbox_dauer.grid(column=1, row=2, sticky="w", padx=2, pady=2)
        self.__textbox_zeiteiheit.grid(column=1, row=3, sticky="w", padx=2, pady=2)
        self.__textbox_vorgaenger.grid(column=1, row=4, sticky="w", padx=2, pady=2)

        frame = tk.Frame(toplevel)

        frame.grid(column=1, row=5, columnspan=1, padx=0, pady=0, sticky="e")

        button_ok = ttk.Button(
            frame,
            style="Normal.TButton",
            text="OK",
            width=12,
            command=lambda t=toplevel, r=mainwindow: self.__button_ok_neuer_vorgang_action(t, r)
        )
        button_abbrechen = ttk.Button(
            frame,
            style="Normal.TButton",
            text="Abbrechen",
            width=12,
            command=lambda t=toplevel: self.__button_abbrechen_action(t)
        )

        button_ok.grid(column=0, row=0, padx=2, pady=2, sticky="w")
        button_abbrechen.grid(column=1, row=0, padx=2, pady=2, sticky="w")

        self.__textbox_index.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_beschreibung.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_dauer.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_zeiteiheit.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_vorgaenger.bind("<Tab>", TkCommon.tab_pressed)

        button_ok.bind(
            "<Enter>",
            lambda event, button=button_ok: TkCommon.hover_button(event, button)
            )
        button_ok.bind(
            "<Leave>",
            lambda event, button=button_ok: TkCommon.leave_button(event, button)
            )

        button_abbrechen.bind(
            "<Enter>",
            lambda event, button=button_abbrechen: TkCommon.hover_button(event, button)
            )
        button_abbrechen.bind(
            "<Leave>",
            lambda event, button=button_abbrechen: TkCommon.leave_button(event, button)
            )

        if len(mainwindow.treeview_vorgangsliste.get_children()) != 0:
            zeiteinheit = (str(mainwindow.treeview_vorgangsliste.item(
                mainwindow.treeview_vorgangsliste.get_children()[0])["values"][3]))
            self.__textbox_zeiteiheit.insert("1.0", zeiteinheit)

        TkCommon.center(toplevel)

    def bearbeite_vorgang(self, mainwindow, aktives_element):
        fonts = Fonts()
        toplevel = tk.Toplevel(self.__root)
        toplevel.resizable(width=False, height=False)
        toplevel.wm_transient(self.__root)
        toplevel.grab_set()
        toplevel.config(padx=2, pady=2)
        toplevel.title("Vorgang bearbeiten")

        label_index = ttk.Label(toplevel, text="Index:", font=fonts.font_main)
        label_beschreibung = ttk.Label(toplevel, text="Beschreibung:", font=fonts.font_main)
        label_dauer = ttk.Label(toplevel, text="Dauer:", font=fonts.font_main)
        label_zeiteinheit = ttk.Label(toplevel, text="Zeiteinheit:", font=fonts.font_main)
        label_vorgaenger = ttk.Label(toplevel, text="Vorgänger:", font=fonts.font_main)

        label_index_text = ttk.Label(
            toplevel,
            text=str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][0]),
            font=fonts.font_main
        )
        self.__textbox_beschreibung = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_dauer = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_zeiteiheit = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )
        self.__textbox_vorgaenger = tk.Text(
            toplevel,
            font=fonts.font_block,
            height=0,
            width=50,
            relief=tk.SUNKEN,
            borderwidth=2,
            highlightthickness=1,
            padx=2,
            pady=2
        )

        label_index.grid(column=0, row=0, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_beschreibung.grid(column=0, row=1, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_dauer.grid(column=0, row=2, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_zeiteinheit.grid(column=0, row=3, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)
        label_vorgaenger.grid(column=0, row=4, sticky="w", padx=2, pady=2, ipadx=2, ipady=2)

        label_index_text.grid(column=1, row=0, sticky="w", padx=2, pady=2)
        self.__textbox_beschreibung.grid(column=1, row=1, sticky="w", padx=2, pady=2)
        self.__textbox_dauer.grid(column=1, row=2, sticky="w", padx=2, pady=2)
        self.__textbox_zeiteiheit.grid(column=1, row=3, sticky="w", padx=2, pady=2)
        self.__textbox_vorgaenger.grid(column=1, row=4, sticky="w", padx=2, pady=2)

        frame = tk.Frame(toplevel)

        frame.grid(column=1, row=5, columnspan=1, padx=0, pady=0, sticky="e")

        button_ok = ttk.Button(
            frame,
            style="Normal.TButton",
            text="OK",
            width=12,
            command=lambda t=toplevel, r=mainwindow, a=aktives_element: self.__button_ok_bearbeite_vorgang_action(
                t, r, a)
        )
        button_abbrechen = ttk.Button(
            frame,
            style="Normal.TButton",
            text="Abbrechen",
            width=12,
            command=lambda t=toplevel: self.__button_abbrechen_action(t)
        )

        button_ok.grid(column=0, row=0, padx=2, pady=2, sticky="w")
        button_abbrechen.grid(column=1, row=0, padx=2, pady=2, sticky="w")

        self.__textbox_beschreibung.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_dauer.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_zeiteiheit.bind("<Tab>", TkCommon.tab_pressed)
        self.__textbox_vorgaenger.bind("<Tab>", TkCommon.tab_pressed)

        button_ok.bind(
            "<Enter>",
            lambda event, button=button_ok: TkCommon.hover_button(event, button)
            )
        button_ok.bind(
            "<Leave>",
            lambda event, button=button_ok: TkCommon.leave_button(event, button)
            )

        button_abbrechen.bind(
            "<Enter>",
            lambda event, button=button_abbrechen: TkCommon.hover_button(event, button)
            )
        button_abbrechen.bind(
            "<Leave>",
            lambda event, button=button_abbrechen: TkCommon.leave_button(event, button)
            )

        if aktives_element:
            beschreibung = str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][1])
            dauer = str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][2])
            zeiteinheit = str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][3])
            vorgaenger = str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][10])
            self.__textbox_beschreibung.insert("1.0", beschreibung)
            self.__textbox_dauer.insert("1.0", dauer)
            self.__textbox_zeiteiheit.insert("1.0", zeiteinheit)
            self.__textbox_vorgaenger.insert("1.0", vorgaenger)

        TkCommon.center(toplevel)

    def __button_ok_neuer_vorgang_action(self, toplevel, mainwindow):
        vorgaenger_liste = []
        try:
            index = self.__textbox_index.get("1.0", 'end-1c').strip("\n")
            beschreibung = self.__textbox_beschreibung.get("1.0", 'end-1c').strip("\n")
            dauer = self.__textbox_dauer.get("1.0", 'end-1c').strip("\n")
            zeiteinheit = self.__textbox_zeiteiheit.get("1.0", 'end-1c').strip("\n")

            if self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n") != "":
                vorgaenger_liste_string = self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n").split(",")
                vorgaenger_liste = [int(x) for x in vorgaenger_liste_string]
        except ValueError:
            pass
        else:
            if index != "" and dauer != "":
                mainwindow.neuer_vorgang(toplevel, int(index), str(beschreibung), int(dauer), zeiteinheit,
                                         vorgaenger_liste)

    def __button_ok_bearbeite_vorgang_action(self, toplevel, mainwindow, aktives_element):
        vorgaenger_liste = []
        try:
            index = str(mainwindow.treeview_vorgangsliste.item(aktives_element)["values"][0])
            beschreibung = self.__textbox_beschreibung.get("1.0", 'end-1c').strip("\n")
            dauer = self.__textbox_dauer.get("1.0", 'end-1c').strip("\n")
            zeiteinheit = self.__textbox_zeiteiheit.get("1.0", 'end-1c').strip("\n")

            if self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n") != "":
                vorgaenger_liste_string = self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n").split(",")
                vorgaenger_liste = [int(x) for x in vorgaenger_liste_string]
        except ValueError:
            pass
        else:
            if index != "" and dauer != "":
                mainwindow.editiere_vorgang(toplevel, int(index), str(beschreibung), int(dauer), zeiteinheit,
                                            vorgaenger_liste, aktives_element)

    @staticmethod
    def __button_abbrechen_action(toplevel):
        toplevel.destroy()
