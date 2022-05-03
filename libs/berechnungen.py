# -*- coding: utf-8 -*-

import math


# Diese Klasse stellt die Methode "berechne_vorgangsdaten()" für das Berechnen der
# folgenden Vorgangsdaten zur Verfügung:
# Nachfolger, FAZ, FEZ, SAZ, SEZ, Gesamtpuffer und freier Puffer.
# Zur Berechnung wird eine Vorgangsliste als Parameter benötigt, die Objekte vom Typ Vorgang enthält.
class Berechnungen:
    def __init__(self, _vorgangsliste):
        self.__vorgangsliste = _vorgangsliste
        self.__baum = list()

    def berechne_vorgangsdaten(self):
        # überprüfe auf Rekursionsfehler, die zu einer endlosen Schleife führen würden
        # (ein Vorgang darf nicht ein Vorgänger einer seiner Vorgänger sein) und
        # gib ggfs. eine Liste von entsprechenden Paaren ("Vorgang, Vorgänger") zurück:
        rekursionsfehler_liste = []
        for vorgangslistenindex in range(len(self.__vorgangsliste)):
            for vorgaenger in self.__vorgangsliste[vorgangslistenindex].vorgaenger_liste:
                vorgaengerliste = []
                for vorgangslistenindex2 in range(len(self.__vorgangsliste)):
                    if vorgaenger == self.__vorgangsliste[vorgangslistenindex2].index:
                        vorgaengerliste = self.__vorgangsliste[vorgangslistenindex2].vorgaenger_liste
                if self.__vorgangsliste[vorgangslistenindex].index in vorgaengerliste:
                    rekursionsfehler_liste.append([self.__vorgangsliste[vorgangslistenindex].index, vorgaenger])

        if len(rekursionsfehler_liste) != 0:
            return rekursionsfehler_liste

        while True:
            ist_vorgang_vor_vorgaenger, vorgangslistenindex, vorgaengerlistenindex = \
                self.__ist_vorgang_vor_vorgaenger()
            if not ist_vorgang_vor_vorgaenger:
                break
            else:
                self.__vorgangsliste.insert(vorgaengerlistenindex + 1, self.__vorgangsliste.pop(vorgangslistenindex))

        # Vorwärtsrechnung:
        for vorgangslistenindex in range(len(self.__vorgangsliste)):
            self.__vorgangsliste[vorgangslistenindex].nachfolger_liste = self.__nachfolger(vorgangslistenindex)
            self.__vorgangsliste[vorgangslistenindex].faz = self.__faz(vorgangslistenindex)
            self.__vorgangsliste[vorgangslistenindex].fez = self.__fez(vorgangslistenindex)

        # Rückwärtsrechnung:
        vorgangslistenindex = len(self.__vorgangsliste) - 1
        while vorgangslistenindex >= 0:
            self.__vorgangsliste[vorgangslistenindex].sez = self.__sez(vorgangslistenindex)
            self.__vorgangsliste[vorgangslistenindex].saz = self.__saz(vorgangslistenindex)
            self.__vorgangsliste[vorgangslistenindex].gp = self.__gp(vorgangslistenindex)
            self.__vorgangsliste[vorgangslistenindex].fp = self.__fp(vorgangslistenindex)
            vorgangslistenindex -= 1

        return rekursionsfehler_liste

    def __ist_vorgang_vor_vorgaenger(self):
        vorgaengerlistenindex = 0
        for vorgangslistenindex in range(len(self.__vorgangsliste)):
            if len(self.__vorgangsliste[vorgangslistenindex].vorgaenger_liste) != 0:
                for i in range(len(self.__vorgangsliste)):
                    if self.__vorgangsliste[i].index == max(self.__vorgangsliste[vorgangslistenindex].vorgaenger_liste):
                        vorgaengerlistenindex = i
                if vorgangslistenindex < vorgaengerlistenindex:
                    return True, vorgangslistenindex, vorgaengerlistenindex
        return False, 0, 0

    def __nachfolger(self, index):
        return_list = list()
        for vorgang in self.__vorgangsliste:
            if self.__vorgangsliste[index].index in vorgang.vorgaenger_liste:
                return_list.append(vorgang.index)
        return return_list

    def __faz(self, index):
        if not index == 0:
            temp_list = []
            for vorgaenger in self.__vorgangsliste[index].vorgaenger_liste:
                for vorgangslistenindex in range(len(self.__vorgangsliste)):
                    if self.__vorgangsliste[vorgangslistenindex].index == vorgaenger:
                        temp_list.append(self.__vorgangsliste[vorgangslistenindex].fez)
            if len(temp_list) != 0:
                return max(temp_list)
            else:
                return 0
        else:
            return 0

    def __fez(self, index):
        return self.__vorgangsliste[index].faz + self.__vorgangsliste[index].dauer

    def __saz(self, index):
        return self.__vorgangsliste[index].sez - self.__vorgangsliste[index].dauer

    def __sez(self, index):
        if index == len(self.__vorgangsliste) - 1:
            return self.__vorgangsliste[index].fez
        else:
            temp_list = []
            for nachfolger in self.__vorgangsliste[index].nachfolger_liste:
                for vorgangslistenindex in range(len(self.__vorgangsliste)):
                    if self.__vorgangsliste[vorgangslistenindex].index == nachfolger:
                        temp_list.append(self.__vorgangsliste[vorgangslistenindex].saz)
            if len(temp_list) != 0:
                return min(temp_list)
            else:
                return self.__vorgangsliste[index].fez

    def __gp(self, index):
        return self.__vorgangsliste[index].saz - self.__vorgangsliste[index].faz

    def __fp(self, index):
        temp_list = []
        for nachfolger in self.__vorgangsliste[index].nachfolger_liste:
            for vorgangslistenindex in range(len(self.__vorgangsliste)):
                if self.__vorgangsliste[vorgangslistenindex].index == nachfolger:
                    temp_list.append(self.__vorgangsliste[vorgangslistenindex].faz)
        if len(temp_list) == 0:
            return 0
        else:
            return min(temp_list) - self.__vorgangsliste[index].fez

    def __pfade(self, _liste2d, _tree, _vorgangindex):
        if len(_liste2d) == 0 and len(_tree[_vorgangindex]) != 0:
            _liste2d.append(list())
            _liste2d[len(_liste2d) - 1].append(0)
        for nachfolgerindex in _tree[_vorgangindex]:
            if nachfolgerindex not in _liste2d[len(_liste2d) - 1]:
                _liste2d[len(_liste2d) - 1].append(nachfolgerindex)
                self.__pfade(_liste2d, _tree, nachfolgerindex)

    def kritischer_pfad(self, _vorgangslistenindex, _kp):
        pass

    def berechne_netzplan(self, _vorgangsliste):
        column_dict = dict()

        spalten_max = 0
        zeilen_max = 0

        column = 1
        for vorgang in self.__vorgangsliste:
            if vorgang.faz not in column_dict.keys():
                temp_liste = list()
                temp_liste.append(vorgang.index)
                for vorgang_neu in self.__vorgangsliste:
                    if vorgang_neu.index not in temp_liste:
                        if vorgang_neu.faz == vorgang.faz:
                            temp_liste.append(vorgang_neu.index)
                column_dict[vorgang.faz] = temp_liste
                column += 1

        sorted_dict = dict()

        for key in sorted(column_dict):
            sorted_dict[key] = column_dict[key]

        column = 0
        for key in sorted_dict.keys():
            spalten_max += 1
            row = 0
            for vorgangsindex in sorted_dict[key]:
                vorgang = _vorgangsliste[self.konv_vorgangsindex_nach_listenindex(vorgangsindex)]
                vorgang.grid_coords['spalte'] = column
                if self.konv_vorgangsindex_nach_listenindex(vorgangsindex) == 0:
                    if len(vorgang.nachfolger_liste) > 1:
                        vorgang.grid_coords['zeile'] = int(math.floor((len(vorgang.nachfolger_liste) - 1) / 2))
                    else:
                        vorgang.grid_coords['zeile'] = row
                else:
                    vorgang.grid_coords['zeile'] = row
                if zeilen_max <= row:
                    zeilen_max += 1
                row += 1
            column += 1

        return spalten_max, zeilen_max

    def konv_vorgangsindex_nach_listenindex(self, _vorgang):
        for i in range(len(self.__vorgangsliste)):
            if self.__vorgangsliste[i].index == _vorgang:
                return i

    def konv_listenindex_nach_vorgangsindex(self, _vorgangsindex):
        return self.__vorgangsliste[_vorgangsindex].index

    @staticmethod
    def __erstelle_baum(elements):
        root = list()
        list_of_nodes = []

        for i in range(len(elements)):
            list_of_nodes.append(Node(i))

        for i in range(len(elements)):

            if elements[i] == -1:
                root = list_of_nodes[i]

            else:
                list_of_nodes[elements[i]].add_child(list_of_nodes[i])

        return root


class Node:
    def __init__(self, _index):
        self.index = _index
        self.children = list()

    def add_child(self, _childindex):
        self.children.append(_childindex)

    def get_children(self):
        return self.children

    def get_index(self):
        return self.index
