# -*- coding: utf-8 -*-

import json
import os
from .berechnungen import Berechnungen
from .vorgang import Vorgang
from .testdaten import Testdaten
from prettytable import PrettyTable


# Eingabe eines chars ohne Enter drücken zu müssen.
# Snippet kopiert von folgender Seite:
# https://code.activestate.com/recipes/134892/
class Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


# Diese Klasse dient der Ausgabe auf einer Konsole.
# Aktuell implementiert ist die Ausgabe der Objekte der Vorgangsliste.
# TODO: einfache visuelle Darstellung als Netzplan
class Konsole:
    def __init__(self):
        berechnungen = Berechnungen()
        testdaten = Testdaten()
        
        modus = self.__eingabe_auswahl_modus()

        if modus == 2:
            vorgangsliste, zeiteinheit = self.__eingabe_vorgangsliste()
            berechnungen.berechne_vorgangsdaten(vorgangsliste)
            self.__ausgabe_vorgangsliste(vorgangsliste, zeiteinheit)
            json_string = json.dumps([o.__dict__ for o in vorgangsliste], indent=4, ensure_ascii=False)
            with open('data/vorgangsliste_out.json', 'w') as json_file:
                json_file.write(json_string)
        else:
            beispieldaten_nummer = self.__eingabe_bespieldatensatz_nummer()
            vorgangsliste, zeiteinheit = testdaten.test_nummer(beispieldaten_nummer)
            berechnungen.berechne_vorgangsdaten(vorgangsliste)
            self.__ausgabe_vorgangsliste(vorgangsliste, zeiteinheit)
            json_string = json.dumps([o.__dict__ for o in vorgangsliste], indent=4, ensure_ascii=False)
            with open('data/vorgangsliste_out.json', 'w') as json_file:
                json_file.write(json_string)

    @staticmethod
    def __cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def __eingabe_auswahl_modus():
        print("Bitte zwischen folgenden Möglichkeiten wählen:")
        print("")
        print("  1:   Verarbeitung und Ausgabe eines Beispieldatensatzes")
        print("  2:   Eingabe eines eigenen Datensatzes")
        print("")
        auswahl = int(input("Auswahl: "))
        if auswahl == 1:
            return 1
        else:
            return 2

    @staticmethod
    def __eingabe_bespieldatensatz_nummer():
        return int(input("Welcher Beispieldatensatz soll verarbeitet werden? "))

    @staticmethod
    def __eingabe_vorgangsliste():
        vorgangsliste = list([])
        print("Im Folgenden werden die Daten für die Vorgangsliste abgefragt.")
        print("Drücke 'q', wenn der letzte Vorgang eingegeben wurde.")
        print("")
        zeiteinheit = input("Zeiteinheit: ")
        print("")
        c = 1
        while True:
            print("Vorgang Nr. " + str("{:2d}".format(c)))
            beschreibung = input("Beschreibung ('q' für Ende): " if c > 1 else "Beschreibung: ")
            if beschreibung == 'q' or beschreibung == 'Q':
                break
            dauer = input("Dauer: ")
            vorgaenger = input("Vorgänger (durch Kommata getrennt, nur Enter für leer): ")
            if vorgaenger != "":
                vorgaenger_liste_strings = vorgaenger.split(",")
                vorgaenger_liste = [int(x) for x in vorgaenger_liste_strings]
            else:
                vorgaenger_liste = list([])
            print("")
            vorgangsliste.append(Vorgang(int(c), beschreibung, int(dauer), vorgaenger_liste))
            c += 1
        return vorgangsliste, zeiteinheit

    @staticmethod
    def __ausgabe_vorgangsliste(_vorgangsliste, _zeiteinheit):
        vorgangsliste = _vorgangsliste
        zeiteinheit = _zeiteinheit
        vorgangstabelle = PrettyTable()
        vorgangstabelle.title = "Vorgangsliste"
        vorgangstabelle.field_names = [
            "Index", "Beschreibung", "Dauer", "Zeiteinheit",
            "FAZ", "FEZ", "SAZ", "SEZ", "GP", "FP",
            "Vorgänger", "Nachfolger"
        ]
        for vorgang in vorgangsliste:
            vorgaenger = ""
            nachfolger = ""
            if len(vorgang.vorgaenger_liste) == 0:
                vorgaenger = "keine"
            else:
                c = 0
                for v in vorgang.vorgaenger_liste:
                    if c != len(vorgang.vorgaenger_liste) - 1:
                        vorgaenger += str(v)
                        vorgaenger += ","
                    else:
                        vorgaenger += str(v)
                    c += 1
            if len(vorgang.nachfolger_liste) == 0:
                nachfolger = "keine"
            else:
                c = 0
                for n in vorgang.nachfolger_liste:
                    if c != len(vorgang.nachfolger_liste) - 1:
                        nachfolger += str(n)
                        nachfolger += ","
                    else:
                        nachfolger += str(n)
                    c += 1
            index = str("{:2d}".format(vorgang.index))
            beschreibung = vorgang.beschreibung
            dauer = str("{:2d}".format(vorgang.dauer))
            zeiteinheit = zeiteinheit
            faz = str("{:2d}".format(vorgang.faz))
            fez = str("{:2d}".format(vorgang.fez))
            saz = str("{:2d}".format(vorgang.saz))
            sez = str("{:2d}".format(vorgang.sez))
            gp = str("{:2d}".format(vorgang.gp))
            fp = str("{:2d}".format(vorgang.fp))

            vorgangstabelle.add_row([
                index,
                beschreibung,
                dauer,
                zeiteinheit,
                faz,
                fez,
                saz,
                sez,
                gp,
                fp,
                vorgaenger,
                nachfolger
            ])
        print(vorgangstabelle)
        
        print("")
        print("Taste drücken zum Beenden...")
        getch = Getch()
        getch()
