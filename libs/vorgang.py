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
        self.linien_anker_links = {'x1': -1, 'y1': - 1, 'x1_versatz': -1}
        self.linien_anker_rechts = {'x1': -1, 'y1': - 1, 'x1_versatz': -1}
