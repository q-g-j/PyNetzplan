# -*- coding: utf-8 -*-

# Speichere jeden Vorgang und seine Daten als Klassenobject:
class Vorgang:
    def __init__(self):
        self.index = 0
        self.beschreibung = ""
        self.dauer = 0
        self.zeiteinheit = ""
        self.faz = 0
        self.saz = 0
        self.fez = 0
        self.sez = 0
        self.gp = 0
        self.fp = 0
        self.vorgaenger_liste = []
        self.nachfolger_liste = []
        self.grid_coords = {'spalte': -1, 'zeile': -1}
        self.index_position = {'x1': -1, 'y1': - 1}
        self.beschreibung_position = {'x1': -1, 'y1': - 1}
        self.dauer_position = {'x1': -1, 'y1': - 1}
        self.zeiteinheit_position = {'x1': -1, 'y1': - 1}
        self.faz_position = {'x1': -1, 'y1': - 1}
        self.fez_position = {'x1': -1, 'y1': - 1}
        self.saz_position = {'x1': -1, 'y1': - 1}
        self.sez_position = {'x1': -1, 'y1': - 1}
        self.gp_position = {'x1': -1, 'y1': - 1}
        self.fp_position = {'x1': -1, 'y1': - 1}
