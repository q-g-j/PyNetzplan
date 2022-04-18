# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

from libs.common import Common
from libs.berechnungen import Berechnungen
from libs.vorgang import Vorgang
from libs.tkinter.fonts import Fonts
from libs.tkinter.menuleiste import Menuleiste
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.dialoge.eingabe import EingabeDialoge
from libs.tkinter.dialoge.fehler import FehlerDialoge


class Mainwindow:
    def __init__(self, _root):
        self.__root = _root

        TkCommon.set_theme(self.__root)
        TkCommon.set_styles()

        self.__vorgangsliste = []
        self.__treeview_vorgangsliste = None
        self.__erstelle_vorgangslisten_tabelle()

        self.__fonts = Fonts()
        self.__menuleiste = Menuleiste(self.__root, self.__treeview_vorgangsliste)
        self.__dialog_neuervorgang = EingabeDialoge(self.__root, self, self.__treeview_vorgangsliste)
        self.__fehler_dialoge = FehlerDialoge(self.__root)

        self.__menuleiste.erstelle_menuleiste()
        self.__erstelle_mainwindow_buttons()

        TkCommon.center(self.__root)

    def neuer_vorgang(self, dialog, index, beschreibung, dauer, zeiteinheit, vorgaenger_liste):
        # falls der angeforderte Index bereits belegt ist, verschiebe alle Indexe ab "index" um eins nach rechts:
        for item in self.__treeview_vorgangsliste.get_children():
            if self.__treeview_vorgangsliste.item(item)['values'][0] == index:
                self.__vorgangslisten_tabelle_verschiebe_nach_rechts(index)
                break

        # Setze die Werte aller Vorgänge zurück
        # (außer: Index, Beschreibung, Dauer, Zeiteinheit, Vorgängerliste):
        for item in self.__treeview_vorgangsliste.get_children():
            values = self.__treeview_vorgangsliste.item(item)['values']
            temp_list = list()
            for i in range(len(values)):
                if i not in (0, 1, 2, 3, 10):
                    temp_list.append("")
                else:
                    temp_list.append(self.__treeview_vorgangsliste.item(item)['values'][i])
            self.__treeview_vorgangsliste.item(item, values=temp_list)

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
        self.__treeview_vorgangsliste.insert(parent='', index=index - 1, text='', values=temp_list)

        # schließe den Dialog:
        dialog.destroy()

    def bearbeite_vorgang(self, dialog, index, beschreibung, dauer, zeiteinheit, vorgaenger_liste, aktives_element):
        # Setze die Werte aller Vorgänge zurück
        # (außer: Index, Beschreibung, Dauer, Zeiteinheit, Vorgängerliste):
        for item in self.__treeview_vorgangsliste.get_children():
            temp_list = []
            for i in range(11):
                if i in (0, 1, 2, 10):
                    temp_list.append(self.__treeview_vorgangsliste.item(item)['values'][i])
                elif i == 3:
                    temp_list.append(zeiteinheit)
                else:
                    temp_list.append("")
            self.__treeview_vorgangsliste.item(item, values=temp_list)

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
        self.__treeview_vorgangsliste.item(aktives_element, values=temp_list)

        # schließe den Dialog:
        dialog.destroy()

    def __erstelle_mainwindow_buttons(self):
        button_frame_left = tk.Frame(self.__root)
        button_frame_right = tk.Frame(self.__root)
        button_frame_left.grid(column=0, row=1, columnspan=13, padx=2, pady=2, sticky="w")
        button_frame_right.grid(column=0, row=2, columnspan=13, padx=2, pady=2, sticky="e")

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
        # button_netzplan_anzeigen.grid(column=2, row=1, padx=2, pady=2, sticky="w")

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

    def __vorgangelisten_tabelle_anzahl_eintraege(self):
        return len(self.__treeview_vorgangsliste.get_children())

    def __vorgangslisten_tabelle_verschiebe_nach_links(self, ab_index):
        verschoben_index_liste = []
        for item in self.__treeview_vorgangsliste.get_children():
            if int(self.__treeview_vorgangsliste.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.__treeview_vorgangsliste.item(item)['values'][0]))
                self.__treeview_vorgangsliste.set(item, 0,
                                                  value=int(self.__treeview_vorgangsliste.item(item)['values'][0]) - 1)

        for item in self.__treeview_vorgangsliste.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.__treeview_vorgangsliste.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] -= 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.__treeview_vorgangsliste.set(item, 10, value=vorgaenger_liste_string)

    def __vorgangslisten_tabelle_verschiebe_nach_rechts(self, ab_index):
        verschoben_index_liste = []
        for item in self.__treeview_vorgangsliste.get_children():
            if int(self.__treeview_vorgangsliste.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.__treeview_vorgangsliste.item(item)['values'][0]))
                self.__treeview_vorgangsliste.set(item, 0,
                                                  value=int(self.__treeview_vorgangsliste.item(item)['values'][0]) + 1)

        for item in self.__treeview_vorgangsliste.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.__treeview_vorgangsliste.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] += 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.__treeview_vorgangsliste.set(item, 10, value=vorgaenger_liste_string)

    def __button_neuer_vorgang_action(self):
        self.__dialog_neuervorgang.neuer_vorgang()

    def __button_bearbeite_vorgang_action(self):
        if self.__vorgangelisten_tabelle_anzahl_eintraege() != 0:
            try:
                aktives_element = self.__treeview_vorgangsliste.selection()[0]
                self.__dialog_neuervorgang.bearbeite_vorgang(aktives_element)
            except IndexError:
                pass

    def __button_loesche_vorgang_action(self):
        if self.__vorgangelisten_tabelle_anzahl_eintraege() != 0:
            aktives_item = self.__treeview_vorgangsliste.selection()[0]
            ab_index = self.__treeview_vorgangsliste.item(aktives_item)['values'][0]
            self.__treeview_vorgangsliste.delete(aktives_item)

            for item in self.__treeview_vorgangsliste.get_children():
                vorgaenger_liste = Common.string_zu_liste(str(self.__treeview_vorgangsliste.item(item)['values'][10]))

                for vorgaenger in vorgaenger_liste:
                    if int(vorgaenger) == int(ab_index):
                        vorgaenger_liste.remove(vorgaenger)

                vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

                self.__treeview_vorgangsliste.set(item, 10, value=vorgaenger_liste_string)

            self.__vorgangslisten_tabelle_verschiebe_nach_links(ab_index)

    def __button_vorgangsliste_berechnen_action(self):
        vorgangsliste = []
        for item in self.__treeview_vorgangsliste.get_children():
            index = int(self.__treeview_vorgangsliste.item(item)['values'][0])
            beschreibung = str(self.__treeview_vorgangsliste.item(item)['values'][1])
            dauer = int(self.__treeview_vorgangsliste.item(item)['values'][2])
            vorgaenger_liste = Common.string_zu_liste(str(self.__treeview_vorgangsliste.item(item)['values'][10]))
            vorgang = Vorgang()
            vorgang.index = index
            vorgang.beschreibung = beschreibung
            vorgang.dauer = dauer
            vorgang.vorgaenger_liste = vorgaenger_liste
            vorgangsliste.append(vorgang)

        berechnungen = Berechnungen()
        rekursionsfehler_liste = berechnungen.berechne_vorgangsdaten(vorgangsliste)

        if len(rekursionsfehler_liste) != 0:
            self.__fehler_dialoge.vorgaenger_rekursions_fehler(rekursionsfehler_liste)

        c = 0
        for item in self.__treeview_vorgangsliste.get_children():
            index = vorgangsliste[c].index
            beschreibung = vorgangsliste[c].beschreibung
            dauer = vorgangsliste[c].dauer
            zeiteinheit = self.__treeview_vorgangsliste.item(item)['values'][3]
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

            self.__treeview_vorgangsliste.item(item, values=(index, beschreibung, dauer, zeiteinheit,
                                                             faz, fez, saz, sez, gp, fp,
                                                             vorgaenger_liste_string, nachfolger_liste_string))

            c += 1

    def __button_netzplan_anzeigen_action(self):
        pass

    def __erstelle_vorgangslisten_tabelle(self):
        self.__treeview_vorgangsliste = ttk.Treeview(self.__root, show='headings',
                                                     height=20, style="Header.Treeview")

        self.__treeview_vorgangsliste['columns'] = (
            'Index',
            'Beschreibung',
            'Dauer',
            'Zeiteinheit',
            'FAZ',
            'FEZ',
            'SAZ',
            'SEZ',
            'GP',
            'FP',
            'Vorgänger',
            'Nachfolger'
        )

        self.__treeview_vorgangsliste.column("#0", width=0, stretch=False)
        self.__treeview_vorgangsliste.column("Index", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("Beschreibung", anchor="w", width=300)
        self.__treeview_vorgangsliste.column("Dauer", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("Zeiteinheit", anchor="w", width=100)
        self.__treeview_vorgangsliste.column("FAZ", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("FEZ", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("SAZ", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("SEZ", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("GP", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("FP", anchor="e", width=50)
        self.__treeview_vorgangsliste.column("Vorgänger", anchor="w", width=160)
        self.__treeview_vorgangsliste.column("Nachfolger", anchor="w", width=160)

        self.__treeview_vorgangsliste.heading("#0", text="", anchor="center")
        self.__treeview_vorgangsliste.heading("Index", text="Index", anchor="center")
        self.__treeview_vorgangsliste.heading("Beschreibung", text="Beschreibung", anchor="center")
        self.__treeview_vorgangsliste.heading("Dauer", text="Dauer", anchor="center")
        self.__treeview_vorgangsliste.heading("Zeiteinheit", text="Zeiteinheit", anchor="center")
        self.__treeview_vorgangsliste.heading("FAZ", text="FAZ", anchor="center")
        self.__treeview_vorgangsliste.heading("FEZ", text="FEZ", anchor="center")
        self.__treeview_vorgangsliste.heading("SAZ", text="SAZ", anchor="center")
        self.__treeview_vorgangsliste.heading("SEZ", text="SEZ", anchor="center")
        self.__treeview_vorgangsliste.heading("GP", text="GP", anchor="center")
        self.__treeview_vorgangsliste.heading("FP", text="FP", anchor="center")
        self.__treeview_vorgangsliste.heading("Vorgänger", text="Vorgänger", anchor="center")
        self.__treeview_vorgangsliste.heading("Nachfolger", text="Nachfolger", anchor="center")

        self.__treeview_vorgangsliste.grid(column=0, row=0)

        scrollbar = ttk.Scrollbar(self.__root, orient="vertical", command=self.__treeview_vorgangsliste.yview)
        self.__treeview_vorgangsliste.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(column=12, row=0, sticky="ns")

    def __loesche_vorgangslisten_tabelle(self):
        self.__treeview_vorgangsliste.destroy()
