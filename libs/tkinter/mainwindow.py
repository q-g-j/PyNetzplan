# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.common import Common
from libs.berechnungen import Berechnungen
from libs.vorgang import Vorgang
from libs.tkinter.fonts import Fonts
from libs.tkinter.menuleiste import Menuleiste
from libs.tkinter.vorgangstabelle import Vorgangstabelle
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.darstellung.netzplan import Netzplan
from libs.tkinter.style import Style
from libs.tkinter.dialoge.eingabe import EingabeDialoge
from libs.tkinter.dialoge.fehler import FehlerDialoge


class Mainwindow:
    def __init__(self, _root):
        self.__root = _root

        Style.set_theme(self.__root)
        Style.set_styles()

        self.__vorgangsliste = []

        self.__frame_vorgangstabelle = ttk.Frame(self.__root)
        self.__frame_mainwindow_buttons = ttk.Frame(self.__root)
        self.__frame_mainwindow_buttons.pack(side=tk.BOTTOM, fill=tk.X, expand=False)
        self.__frame_vorgangstabelle.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.__vorgangstabelle = Vorgangstabelle(self.__frame_vorgangstabelle)

        self.__fonts = Fonts()
        Menuleiste(self.__root, self.__vorgangstabelle)
        self.__dialog_neuervorgang = EingabeDialoge(self.__root, self, self.__vorgangstabelle)
        self.__fehler_dialoge = FehlerDialoge(self.__root)
        self.__erstelle_mainwindow_buttons()

        if 1330 > self.__root.winfo_screenwidth() or \
                800 > self.__root.winfo_screenheight():
            self.__root.geometry("%sx%s" % (str(int(self.__root.winfo_screenwidth() * 0.9)),
                                            str(int(self.__root.winfo_screenheight() * 0.8))))
        else:
            self.__root.geometry("1330x800")

        TkCommon.center(self.__root)

    def neuer_vorgang(self, dialog, index, beschreibung, dauer, zeiteinheit, vorgaenger_liste):
        # falls der angeforderte Index bereits belegt ist, verschiebe alle Indexe ab "index" um eins nach rechts:
        for item in self.__vorgangstabelle.get_children():
            if self.__vorgangstabelle.item(item)['values'][0] == index:
                self.__vorgangstabelle.vorgangslisten_tabelle_verschiebe_nach_rechts(index)
                break

        # Setze die Werte aller Vorgänge zurück
        # (außer: Index, Beschreibung, Dauer, Vorgängerliste):
        for item in self.__vorgangstabelle.get_children():
            values = self.__vorgangstabelle.item(item)['values']
            temp_list = list()
            for i in range(len(values)):
                if i not in (0, 1, 2, 3, 10):
                    temp_list.append("")
                elif i == 3:
                    temp_list.append(zeiteinheit)
                else:
                    temp_list.append(self.__vorgangstabelle.item(item)['values'][i])
            self.__vorgangstabelle.item(item, values=temp_list)

        # Füge schließlich den neuen Vorgang an der angeforderten Position ein:
        temp_list = list()
        for i in range(11):
            if i == 0:
                temp_list.append(index)
            elif i == 1:
                temp_list.append(beschreibung)
            elif i == 2:
                temp_list.append(dauer)
            elif i == 3:
                temp_list.append(zeiteinheit)
            elif i == 10:
                temp_list.append(Common.liste_zu_string(vorgaenger_liste))
            else:
                temp_list.append("")
        self.__vorgangstabelle.insert(parent='', index=index - 1, text='', values=temp_list)

        self.__vorgangstabelle.vorgangslisten_tabelle_streifen()

        # schließe den Dialog:
        dialog.destroy()

    def bearbeite_vorgang(self, dialog, index, beschreibung, dauer, zeiteinheit, vorgaenger_liste, aktives_element):
        # Setze die Werte aller Vorgänge zurück
        # (außer: Index, Beschreibung, Dauer, Zeiteinheit, Vorgängerliste):
        for item in self.__vorgangstabelle.get_children():
            temp_list = []
            for i in range(11):
                if i in (0, 1, 2, 10):
                    temp_list.append(self.__vorgangstabelle.item(item)['values'][i])
                elif i == 3:
                    temp_list.append(zeiteinheit)
                else:
                    temp_list.append("")
            self.__vorgangstabelle.item(item, values=temp_list)

        # Setze die neuen Werte für den zu bearbeitenden Vorgang:
        temp_list = list()
        for i in range(11):
            if i == 0:
                temp_list.append(index)
            elif i == 1:
                temp_list.append(beschreibung)
            elif i == 2:
                temp_list.append(dauer)
            elif i == 3:
                temp_list.append(zeiteinheit)
            elif i == 10:
                temp_list.append(Common.liste_zu_string(vorgaenger_liste))
            else:
                temp_list.append("")
        self.__vorgangstabelle.item(aktives_element, values=temp_list)

        # schließe den Dialog:
        dialog.destroy()

    def __erstelle_mainwindow_buttons(self):
        button_frame_left = ttk.Frame(self.__frame_mainwindow_buttons)
        button_frame_right = ttk.Frame(self.__frame_mainwindow_buttons)
        button_frame_left.pack(side=tk.TOP, anchor='nw', padx=2, pady=2, fill=tk.Y, expand=False)
        button_frame_right.pack(side=tk.RIGHT, padx=2, pady=2, fill=tk.Y, expand=False)

        button_neuer_vorgang = ttk.Button(
            button_frame_left,
            style="Normal.TButton",
            text="neuer Vorgang",
            command=self.__button_neuer_vorgang_action
        )
        button_editiere_vorgang = ttk.Button(
            button_frame_left,
            style="Normal.TButton",
            text="Vorgang bearbeiten",
            command=self.__button_bearbeite_vorgang_action
        )
        button_loesche_vorgang = ttk.Button(
            button_frame_left,
            style="Normal.TButton",
            text="Vorgang löschen",
            command=self.__button_loesche_vorgang_action
        )
        button_vorgangsliste_berechnen = ttk.Button(
            button_frame_right,
            style="Normal.TButton",
            text="Vorgangsliste vervollständigen",
            command=self.__button_vorgangsliste_berechnen_action
        )

        button_netzplan_anzeigen = ttk.Button(
            button_frame_right,
            style="Normal.TButton",
            text="Netzplan anzeigen",
            command=self.__button_netzplan_anzeigen_action
        )

        button_neuer_vorgang.grid(column=0, row=0, padx=2, pady=2, sticky="w")
        button_editiere_vorgang.grid(column=1, row=0, padx=2, pady=2, sticky="w")
        button_loesche_vorgang.grid(column=2, row=0, padx=2, pady=2, sticky="w")
        button_vorgangsliste_berechnen.grid(column=1, row=1, padx=2, pady=2, sticky="w")
        button_netzplan_anzeigen.grid(column=2, row=1, padx=2, pady=2, sticky="w")

        # aktiviere Highlighting der Buttons beim Darüberfahren mit der Maus:
        button_neuer_vorgang.bind(
            "<Enter>",
            lambda event, b=button_neuer_vorgang: TkCommon.hover_button(event, b)
        )
        button_neuer_vorgang.bind(
            "<Leave>",
            lambda event, b=button_neuer_vorgang: TkCommon.leave_button(event, b)
        )
        button_editiere_vorgang.bind(
            "<Enter>",
            lambda event, b=button_editiere_vorgang: TkCommon.hover_button(event, b)
        )
        button_editiere_vorgang.bind(
            "<Leave>",
            lambda event, b=button_editiere_vorgang: TkCommon.leave_button(event, b)
        )
        button_loesche_vorgang.bind(
            "<Enter>",
            lambda event, b=button_loesche_vorgang: TkCommon.hover_button(event, b)
        )
        button_loesche_vorgang.bind(
            "<Leave>",
            lambda event, b=button_loesche_vorgang: TkCommon.leave_button(event, b)
        )
        button_vorgangsliste_berechnen.bind(
            "<Enter>",
            lambda event, b=button_vorgangsliste_berechnen: TkCommon.hover_button(event, b)
        )
        button_vorgangsliste_berechnen.bind(
            "<Leave>",
            lambda event, b=button_vorgangsliste_berechnen: TkCommon.leave_button(event, b)
        )
        button_netzplan_anzeigen.bind(
            "<Enter>",
            lambda event, b=button_netzplan_anzeigen: TkCommon.hover_button(event, b)
        )
        button_netzplan_anzeigen.bind(
            "<Leave>",
            lambda event, b=button_netzplan_anzeigen: TkCommon.leave_button(event, b)
        )

    def __button_neuer_vorgang_action(self):
        self.__dialog_neuervorgang.neuer_vorgang()

    def __button_bearbeite_vorgang_action(self):
        if len(self.__vorgangstabelle.get_children()) != 0:
            try:
                aktives_element = self.__vorgangstabelle.selection()[0]
                self.__dialog_neuervorgang.bearbeite_vorgang(aktives_element)
            except IndexError:
                pass

    def __button_loesche_vorgang_action(self):
        if len(self.__vorgangstabelle.get_children()) != 0:
            aktives_item = self.__vorgangstabelle.selection()[0]
            ab_index = self.__vorgangstabelle.item(aktives_item)['values'][0]
            self.__vorgangstabelle.delete(aktives_item)

            for item in self.__vorgangstabelle.get_children():
                vorgaenger_liste = Common.string_zu_liste(
                    str(self.__vorgangstabelle.item(item)['values'][10]))

                for vorgaenger in vorgaenger_liste:
                    if int(vorgaenger) == int(ab_index):
                        vorgaenger_liste.remove(vorgaenger)

                vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

                self.__vorgangstabelle.set(item, 10, value=vorgaenger_liste_string)

            self.__vorgangstabelle.vorgangslisten_tabelle_verschiebe_nach_links(ab_index)

        self.__vorgangstabelle.vorgangslisten_tabelle_streifen()

    def __button_vorgangsliste_berechnen_action(self):
        vorgangsliste = []
        for item in self.__vorgangstabelle.get_children():
            vorgaenger_liste = Common.string_zu_liste(
                str(self.__vorgangstabelle.item(item)['values'][10]))
            vorgang = Vorgang()
            vorgang.index = int(self.__vorgangstabelle.item(item)['values'][0])
            vorgang.beschreibung = self.__vorgangstabelle.item(item)['values'][1]
            vorgang.dauer = int(self.__vorgangstabelle.item(item)['values'][2])
            vorgang.vorgaenger_liste = vorgaenger_liste
            vorgangsliste.append(vorgang)

        berechnungen = Berechnungen(vorgangsliste)
        rekursionsfehler_liste = berechnungen.berechne_vorgangsdaten()

        if len(rekursionsfehler_liste) != 0:
            self.__fehler_dialoge.vorgaenger_rekursions_fehler(rekursionsfehler_liste)

        c = 0
        for item in self.__vorgangstabelle.get_children():
            index = vorgangsliste[c].index
            beschreibung = vorgangsliste[c].beschreibung
            dauer = vorgangsliste[c].dauer
            zeiteinheit = self.__vorgangstabelle.item(item)['values'][3]
            faz = vorgangsliste[c].faz
            fez = vorgangsliste[c].fez
            saz = vorgangsliste[c].saz
            sez = vorgangsliste[c].sez
            gp = vorgangsliste[c].gp
            fp = vorgangsliste[c].fp
            vorgaenger_liste = vorgangsliste[c].vorgaenger_liste
            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)
            nachfolger_liste = vorgangsliste[c].nachfolger_liste
            nachfolger_liste_string = Common.liste_zu_string(nachfolger_liste)

            self.__vorgangstabelle.item(item, values=(index, beschreibung, dauer, zeiteinheit,
                                                      faz, fez, saz, sez, gp, fp,
                                                      vorgaenger_liste_string,
                                                      nachfolger_liste_string))

            c += 1

    def __button_netzplan_anzeigen_action(self):
        self.__button_vorgangsliste_berechnen_action()

        vorgangsliste = []
        for item in self.__vorgangstabelle.get_children():
            vorgaenger_liste = Common.string_zu_liste(
                str(self.__vorgangstabelle.item(item)['values'][10]))
            nachfolger_liste = Common.string_zu_liste(
                str(self.__vorgangstabelle.item(item)['values'][11]))
            vorgang = Vorgang()
            vorgang.index = int(self.__vorgangstabelle.item(item)['values'][0])
            vorgang.beschreibung = self.__vorgangstabelle.item(item)['values'][1]
            vorgang.dauer = int(self.__vorgangstabelle.item(item)['values'][2])
            vorgang.zeiteinheit = self.__vorgangstabelle.item(item)['values'][3]
            vorgang.faz = int(self.__vorgangstabelle.item(item)['values'][4])
            vorgang.fez = int(self.__vorgangstabelle.item(item)['values'][5])
            vorgang.saz = int(self.__vorgangstabelle.item(item)['values'][6])
            vorgang.sez = int(self.__vorgangstabelle.item(item)['values'][7])
            vorgang.gp = int(self.__vorgangstabelle.item(item)['values'][8])
            vorgang.fp = int(self.__vorgangstabelle.item(item)['values'][9])
            vorgang.vorgaenger_liste = vorgaenger_liste
            vorgang.nachfolger_liste = nachfolger_liste
            vorgangsliste.append(vorgang)

        if len(self.__vorgangstabelle.get_children()) != 0:
            Netzplan(self.__root, vorgangsliste)
