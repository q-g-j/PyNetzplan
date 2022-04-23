# -*- coding: utf-8 -*-
import tkinter
from tkinter import ttk

from libs.common import Common
from libs.tkinter.autoscrollbar import AutoScrollbar


class Vorgangstabelle:
    def __init__(self, _root):
        self.__root = _root
        self.vorgangslisten_tabelle = None

    def erstelle_vorgangslisten_tabelle(self):
        self.vorgangslisten_tabelle = ttk.Treeview(self.__root, show='headings',
                                                   height=25, style="Header.Treeview")

        self.vorgangslisten_tabelle.tag_configure('odd_row', background='#40403e')
        # self.vorgangelisten_tabelle.tag_bind('selected', '<1>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewSelect>>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewOpen>>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewClose>>', self.cb)

        self.vorgangslisten_tabelle['columns'] = (
            'Nummer',
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

        self.vorgangslisten_tabelle.column("#0", width=0, stretch=False)
        self.vorgangslisten_tabelle.column("Nummer", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("Beschreibung", anchor="w", minwidth=300, stretch=True)
        self.vorgangslisten_tabelle.column("Dauer", anchor="e", width=70, stretch=False)
        self.vorgangslisten_tabelle.column("Zeiteinheit", anchor="w", width=120, stretch=False)
        self.vorgangslisten_tabelle.column("FAZ", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("FEZ", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("SAZ", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("SEZ", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("GP", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("FP", anchor="e", width=50, stretch=False)
        self.vorgangslisten_tabelle.column("Vorgänger", anchor="w", minwidth=240, stretch=True)
        self.vorgangslisten_tabelle.column("Nachfolger", anchor="w", minwidth=240, stretch=True)

        self.vorgangslisten_tabelle.heading("#0", text="", anchor="center")
        self.vorgangslisten_tabelle.heading("Nummer", text="Nr.", anchor="center")
        self.vorgangslisten_tabelle.heading("Beschreibung", text="Beschreibung", anchor="center")
        self.vorgangslisten_tabelle.heading("Dauer", text="Dauer", anchor="center")
        self.vorgangslisten_tabelle.heading("Zeiteinheit", text="Zeiteinheit", anchor="center")
        self.vorgangslisten_tabelle.heading("FAZ", text="FAZ", anchor="center")
        self.vorgangslisten_tabelle.heading("FEZ", text="FEZ", anchor="center")
        self.vorgangslisten_tabelle.heading("SAZ", text="SAZ", anchor="center")
        self.vorgangslisten_tabelle.heading("SEZ", text="SEZ", anchor="center")
        self.vorgangslisten_tabelle.heading("GP", text="GP", anchor="center")
        self.vorgangslisten_tabelle.heading("FP", text="FP", anchor="center")
        self.vorgangslisten_tabelle.heading("Vorgänger", text="Vorgänger", anchor="center")
        self.vorgangslisten_tabelle.heading("Nachfolger", text="Nachfolger", anchor="center")

        self.vorgangslisten_tabelle.grid(column=0, row=0, sticky="nsew")
        self.__root.rowconfigure(0, weight=1)
        self.__root.columnconfigure(0, weight=1)

        scrollbar_x = AutoScrollbar(self.__root, orient="horizontal", command=self.vorgangslisten_tabelle.xview)
        scrollbar_y = AutoScrollbar(self.__root, orient="vertical", command=self.vorgangslisten_tabelle.yview)
        self.vorgangslisten_tabelle.configure(xscrollcommand=scrollbar_x.set)
        self.vorgangslisten_tabelle.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_x.grid(column=0, row=1, sticky="we")
        scrollbar_y.grid(column=1, row=0, sticky="ns")

    def vorgangslisten_tabelle_verschiebe_nach_links(self, ab_index):
        verschoben_index_liste = []
        for item in self.vorgangslisten_tabelle.get_children():
            if int(self.vorgangslisten_tabelle.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.vorgangslisten_tabelle.item(item)['values'][0]))
                self.vorgangslisten_tabelle.set(item, 0,
                                                value=int(self.vorgangslisten_tabelle.item(item)['values'][0]) - 1)

        for item in self.vorgangslisten_tabelle.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.vorgangslisten_tabelle.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] -= 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.vorgangslisten_tabelle.set(item, 10, value=vorgaenger_liste_string)

    def vorgangslisten_tabelle_verschiebe_nach_rechts(self, ab_index):
        verschoben_index_liste = []
        for item in self.vorgangslisten_tabelle.get_children():
            if int(self.vorgangslisten_tabelle.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.vorgangslisten_tabelle.item(item)['values'][0]))
                self.vorgangslisten_tabelle.set(item, 0,
                                                value=int(self.vorgangslisten_tabelle.item(item)['values'][0]) + 1)

        for item in self.vorgangslisten_tabelle.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.vorgangslisten_tabelle.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] += 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.vorgangslisten_tabelle.set(item, 10, value=vorgaenger_liste_string)

    def vorgangslisten_tabelle_streifen(self):
        for itemindex in range(len(self.vorgangslisten_tabelle.get_children())):
            if itemindex % 2 != 0:
                self.vorgangslisten_tabelle.item(
                    self.vorgangslisten_tabelle.get_children()[itemindex], tags=('odd_row',))
            else:
                self.vorgangslisten_tabelle.item(
                    self.vorgangslisten_tabelle.get_children()[itemindex], tags=())
