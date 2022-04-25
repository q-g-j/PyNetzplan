# -*- coding: utf-8 -*-

from tkinter import ttk

from libs.common import Common
from libs.tkinter.autoscrollbar import AutoScrollbar


class Vorgangstabelle(ttk.Treeview):
    def __init__(self, _parent):
        ttk.Treeview.__init__(self, _parent, show='headings',
                              height=25, style="Header.Treeview")

        self.tag_configure('odd_row', background='#40403e')
        # self.vorgangelisten_tabelle.tag_bind('selected', '<1>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewSelect>>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewOpen>>', self.cb)
        # self.vorgangelisten_tabelle.tag_bind('selected', '<<TreeviewClose>>', self.cb)

        self['columns'] = (
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

        self.column("#0", width=0, stretch=False)
        self.column("Nummer", anchor="e", width=50, stretch=False)
        self.column("Beschreibung", anchor="w", minwidth=300, stretch=True)
        self.column("Dauer", anchor="e", width=70, stretch=False)
        self.column("Zeiteinheit", anchor="w", width=120, stretch=False)
        self.column("FAZ", anchor="e", width=50, stretch=False)
        self.column("FEZ", anchor="e", width=50, stretch=False)
        self.column("SAZ", anchor="e", width=50, stretch=False)
        self.column("SEZ", anchor="e", width=50, stretch=False)
        self.column("GP", anchor="e", width=50, stretch=False)
        self.column("FP", anchor="e", width=50, stretch=False)
        self.column("Vorgänger", anchor="w", minwidth=240, stretch=True)
        self.column("Nachfolger", anchor="w", minwidth=240, stretch=True)

        self.heading("#0", text="", anchor="center")
        self.heading("Nummer", text="Nr.", anchor="center")
        self.heading("Beschreibung", text="Beschreibung", anchor="center")
        self.heading("Dauer", text="Dauer", anchor="center")
        self.heading("Zeiteinheit", text="Zeiteinheit", anchor="center")
        self.heading("FAZ", text="FAZ", anchor="center")
        self.heading("FEZ", text="FEZ", anchor="center")
        self.heading("SAZ", text="SAZ", anchor="center")
        self.heading("SEZ", text="SEZ", anchor="center")
        self.heading("GP", text="GP", anchor="center")
        self.heading("FP", text="FP", anchor="center")
        self.heading("Vorgänger", text="Vorgänger", anchor="center")
        self.heading("Nachfolger", text="Nachfolger", anchor="center")

        self.grid(column=0, row=0, sticky="nsew")
        _parent.rowconfigure(0, weight=1)
        _parent.columnconfigure(0, weight=1)

        scrollbar_x = AutoScrollbar(_parent, orient="horizontal", command=self.xview)
        scrollbar_y = AutoScrollbar(_parent, orient="vertical", command=self.yview)
        self.configure(xscrollcommand=scrollbar_x.set)
        self.configure(yscrollcommand=scrollbar_y.set)
        scrollbar_x.grid(column=0, row=1, sticky="we")
        scrollbar_y.grid(column=1, row=0, sticky="ns")

    def vorgangslisten_tabelle_verschiebe_nach_links(self, ab_index):
        verschoben_index_liste = []
        for item in self.get_children():
            if int(self.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.item(item)['values'][0]))
                self.set(item, 0,
                         value=int(self.item(item)['values'][0]) - 1)

        for item in self.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] -= 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.set(item, 10, value=vorgaenger_liste_string)

    def vorgangslisten_tabelle_verschiebe_nach_rechts(self, ab_index):
        verschoben_index_liste = []
        for item in self.get_children():
            if int(self.item(item)['values'][0]) >= int(ab_index):
                verschoben_index_liste.append(int(self.item(item)['values'][0]))
                self.set(item, 0,
                         value=int(self.item(item)['values'][0]) + 1)

        for item in self.get_children():
            vorgaenger_liste = Common.string_zu_liste(str(self.item(item)['values'][10]))

            for vorgaengerindex in range(len(vorgaenger_liste)):
                if int(vorgaenger_liste[vorgaengerindex]) in verschoben_index_liste:
                    vorgaenger_liste[vorgaengerindex] += 1

            vorgaenger_liste_string = Common.liste_zu_string(vorgaenger_liste)

            self.set(item, 10, value=vorgaenger_liste_string)

    def vorgangslisten_tabelle_streifen(self):
        for itemindex in range(len(self.get_children())):
            if itemindex % 2 != 0:
                self.item(
                    self.get_children()[itemindex], tags=('odd_row',))
            else:
                self.item(
                    self.get_children()[itemindex], tags=())
