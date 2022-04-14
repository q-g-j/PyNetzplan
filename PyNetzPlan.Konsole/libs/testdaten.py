# -*# -*- coding: utf-8 -*-

from .vorgang import Vorgang
import json


class Testdaten:
    def test_nummer(self, nummer):
        with open("data/beispiel_vorgangslisten.json", "rb") as json_file:
            json_data = json.load(json_file)

        print("")
        vorgangsliste = list([])
        testdaten_nummer_string = str(nummer)

        if nummer < 10:
            testdaten_nummer_string = testdaten_nummer_string[:0] + "00" + testdaten_nummer_string[0:]

        elif nummer < 100:
            testdaten_nummer_string = testdaten_nummer_string[:0] + "0" + testdaten_nummer_string[0:]

        zeiteinheit = json_data['vorgangsliste_' + testdaten_nummer_string][0]['Zeiteinheit']

        for vorgang in json_data['vorgangsliste_' + testdaten_nummer_string]:
            vorgangsliste.append(
                Vorgang(vorgang['Index'], vorgang['Beschreibung'], vorgang['Dauer'], vorgang['Vorgänger'])
            )

        return vorgangsliste, zeiteinheit
