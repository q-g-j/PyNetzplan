# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.common import Common
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.fonts import Fonts


class EingabeDialoge:
    def __init__(self, _root, _mainwindow, _treeview_vorgangsliste):
        self.__root = _root
        self.__mainwindow = _mainwindow
        self.__treeview_vorgangsliste = _treeview_vorgangsliste
        self.__textbox_index = None
        self.__textbox_beschreibung = None
        self.__textbox_dauer = None
        self.__textbox_zeiteinheit = None
        self.__textbox_vorgaenger = None

    def neuer_vorgang(self):
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
        self.__textbox_zeiteinheit = tk.Text(
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
        self.__textbox_zeiteinheit.grid(column=1, row=3, sticky="w", padx=2, pady=2)
        self.__textbox_vorgaenger.grid(column=1, row=4, sticky="w", padx=2, pady=2)

        frame = tk.Frame(toplevel)

        frame.grid(column=1, row=5, columnspan=1, padx=0, pady=0, sticky="e")

        button_ok = ttk.Button(
            frame,
            style="Normal.TButton",
            text="OK",
            width=12,
            command=lambda t=toplevel: self.__button_ok_neuer_vorgang_action(t)
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
        self.__textbox_zeiteinheit.bind("<Tab>", TkCommon.tab_pressed)
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

        if len(self.__treeview_vorgangsliste.get_children()) != 0:
            zeiteinheit = (str(self.__treeview_vorgangsliste.item(
                self.__treeview_vorgangsliste.get_children()[0])["values"][3]))
            self.__textbox_zeiteinheit.insert("1.0", zeiteinheit)

        self.__textbox_index.bind("<Return>", lambda e: "break")
        self.__textbox_beschreibung.bind("<Return>", lambda e: "break")
        self.__textbox_dauer.bind("<Return>", lambda e: "break")
        self.__textbox_zeiteinheit.bind("<Return>", lambda e: "break")
        self.__textbox_vorgaenger.bind("<Return>", lambda e: "break")

        TkCommon.center(toplevel)

    def bearbeite_vorgang(self, aktives_element):
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
            text=str(self.__treeview_vorgangsliste.item(aktives_element)["values"][0]),
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
        self.__textbox_zeiteinheit = tk.Text(
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
        self.__textbox_zeiteinheit.grid(column=1, row=3, sticky="w", padx=2, pady=2)
        self.__textbox_vorgaenger.grid(column=1, row=4, sticky="w", padx=2, pady=2)

        frame = tk.Frame(toplevel)

        frame.grid(column=1, row=5, columnspan=1, padx=0, pady=0, sticky="e")

        button_ok = ttk.Button(
            frame,
            style="Normal.TButton",
            text="OK",
            width=12,
            command=lambda t=toplevel, a=aktives_element: self.__button_ok_bearbeite_vorgang_action(
                t, a)
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
        self.__textbox_zeiteinheit.bind("<Tab>", TkCommon.tab_pressed)
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

        self.__textbox_beschreibung.bind("<Return>", lambda e: "break")
        self.__textbox_dauer.bind("<Return>", lambda e: "break")
        self.__textbox_zeiteinheit.bind("<Return>", lambda e: "break")
        self.__textbox_vorgaenger.bind("<Return>", lambda e: "break")

        if aktives_element:
            beschreibung = str(self.__treeview_vorgangsliste.item(aktives_element)["values"][1])
            dauer = str(self.__treeview_vorgangsliste.item(aktives_element)["values"][2])
            zeiteinheit = str(self.__treeview_vorgangsliste.item(aktives_element)["values"][3])
            vorgaenger = str(self.__treeview_vorgangsliste.item(aktives_element)["values"][10])
            self.__textbox_beschreibung.insert("1.0", beschreibung)
            self.__textbox_dauer.insert("1.0", dauer)
            self.__textbox_zeiteinheit.insert("1.0", zeiteinheit)
            self.__textbox_vorgaenger.insert("1.0", vorgaenger)

        TkCommon.center(toplevel)

    def __button_ok_neuer_vorgang_action(self, toplevel):
        try:
            index_string = self.__textbox_index.get("1.0", 'end-1c').strip("\n")
            beschreibung = self.__textbox_beschreibung.get("1.0", 'end-1c').strip("\n")
            dauer_string = self.__textbox_dauer.get("1.0", 'end-1c').strip("\n")
            zeiteinheit = self.__textbox_zeiteinheit.get("1.0", 'end-1c').strip("\n")
            vorgaenger_liste_string = self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n")

            index = int(index_string)
            dauer = int(dauer_string)
            vorgaenger_liste = Common.string_zu_liste(vorgaenger_liste_string)
        except ValueError:
            pass
        else:
            if index not in vorgaenger_liste:
                self.__mainwindow.neuer_vorgang(toplevel, index, beschreibung, dauer, zeiteinheit,
                                                vorgaenger_liste)

    def __button_ok_bearbeite_vorgang_action(self, toplevel, aktives_element):
        try:
            index = self.__treeview_vorgangsliste.item(aktives_element)["values"][0]
            beschreibung = self.__textbox_beschreibung.get("1.0", 'end-1c').strip("\n")
            dauer_string = self.__textbox_dauer.get("1.0", 'end-1c').strip("\n")
            zeiteinheit = self.__textbox_zeiteinheit.get("1.0", 'end-1c').strip("\n")
            vorgaenger_liste_string = self.__textbox_vorgaenger.get("1.0", 'end-1c').strip("\n")

            dauer = int(dauer_string)
            vorgaenger_liste = Common.string_zu_liste(vorgaenger_liste_string)
        except ValueError:
            pass
        else:
            if index not in vorgaenger_liste:
                self.__mainwindow.bearbeite_vorgang(toplevel, index, beschreibung, dauer, zeiteinheit,
                                                    vorgaenger_liste, aktives_element)

    @staticmethod
    def __button_abbrechen_action(toplevel):
        toplevel.destroy()
