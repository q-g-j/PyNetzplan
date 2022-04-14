# -*- coding: utf-8 -*-

# Speichere jeden Vorgang und seine Daten als Klassenobject: 
class Vorgang:
    def __init__(self, _index, _beschreibung, _dauer, _vorgaenger_liste):
        self.index = _index
        self.beschreibung = _beschreibung
        self.dauer = _dauer
        self.faz = 0
        self.saz = 0
        self.fez = 0
        self.sez = 0
        self.gp = 0
        self.fp = 0
        self.vorgaenger_liste = _vorgaenger_liste
        self.nachfolger_liste = []
