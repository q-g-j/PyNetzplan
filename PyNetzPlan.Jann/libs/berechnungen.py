# -*- coding: utf-8 -*-


# Diese Klasse stellt die Methode "berechne_vorgangsdaten()" für das Berechnen der
# folgenden Vorgangsdaten zur Verfügung:
# Nachfolger, FAZ, FEZ, SAZ, SEZ, Gesamtpuffer und freier Puffer.
# Zur Berechnung wird eine Vorgangsliste als Parameter benötigt, die Objekte vom Typ Vorgang enthält.
class Berechnungen(object):
    def __init__(self):
        self.vorgangsliste = []

    def berechne_vorgangsdaten(self, _vorgangsliste):
        self.vorgangsliste = _vorgangsliste

        while True:
            ist_vorgang_vor_vorgaenger, vorgangslistenindex, vorgaengerlistenindex = \
                self.__ist_vorgang_vor_vorgaenger()
            if not ist_vorgang_vor_vorgaenger:
                break
            else:
                self.vorgangsliste.insert(vorgaengerlistenindex + 1, self.vorgangsliste.pop(vorgangslistenindex))

        # Vorwärtsrechnung:
        for vorgangslistenindex in range(len(self.vorgangsliste)):
            self.vorgangsliste[vorgangslistenindex].nachfolger_liste = self.__nachfolger(vorgangslistenindex)
            self.vorgangsliste[vorgangslistenindex].faz = self.__faz(vorgangslistenindex)
            self.vorgangsliste[vorgangslistenindex].fez = self.__fez(vorgangslistenindex)

        # Rückwärtsrechnung:
        vorgangslistenindex = len(self.vorgangsliste) - 1
        while vorgangslistenindex >= 0:
            self.vorgangsliste[vorgangslistenindex].sez = self.__sez(vorgangslistenindex)
            self.vorgangsliste[vorgangslistenindex].saz = self.__saz(vorgangslistenindex)
            self.vorgangsliste[vorgangslistenindex].gp = self.__gp(vorgangslistenindex)
            self.vorgangsliste[vorgangslistenindex].fp = self.__fp(vorgangslistenindex)
            vorgangslistenindex -= 1

    def __ist_vorgang_vor_vorgaenger(self):
        vorgaengerlistenindex = 0
        for vorgangslistenindex in range(len(self.vorgangsliste)):
            if len(self.vorgangsliste[vorgangslistenindex].vorgaenger_liste) != 0:
                for i in range(len(self.vorgangsliste)):
                    if self.vorgangsliste[i].index == max(self.vorgangsliste[vorgangslistenindex].vorgaenger_liste):
                        vorgaengerlistenindex = i
                if vorgangslistenindex < vorgaengerlistenindex:
                    return True, vorgangslistenindex, vorgaengerlistenindex
        return False, 0, 0

    def __nachfolger(self, index):
        return_list = list([])
        for vorgang in self.vorgangsliste:
            if self.vorgangsliste[index].index in vorgang.vorgaenger_liste:
                return_list.append(vorgang.index)
        return return_list

    def __faz(self, index):
        if not index == 0:
            temp_list = []
            for vorgaenger in self.vorgangsliste[index].vorgaenger_liste:
                for vorgangslistenindex in range(len(self.vorgangsliste)):
                    if self.vorgangsliste[vorgangslistenindex].index == vorgaenger:
                        temp_list.append(self.vorgangsliste[vorgangslistenindex].fez)
            if len(temp_list) != 0:
                return max(temp_list)
            else:
                return 0
        else:
            return 0

    def __fez(self, index):
        return self.vorgangsliste[index].faz + self.vorgangsliste[index].dauer

    def __saz(self, index):
        return self.vorgangsliste[index].sez - self.vorgangsliste[index].dauer

    def __sez(self, index):
        if index == len(self.vorgangsliste) - 1:
            return self.vorgangsliste[index].fez
        else:
            temp_list = []
            for nachfolger in self.vorgangsliste[index].nachfolger_liste:
                for vorgangslistenindex in range(len(self.vorgangsliste)):
                    if self.vorgangsliste[vorgangslistenindex].index == nachfolger:
                        temp_list.append(self.vorgangsliste[vorgangslistenindex].saz)
            if len(temp_list) != 0:
                return min(temp_list)
            else:
                return self.vorgangsliste[index].fez

    def __gp(self, index):
        return self.vorgangsliste[index].saz - self.vorgangsliste[index].faz

    def __fp(self, index):
        temp_list = []
        for nachfolger in self.vorgangsliste[index].nachfolger_liste:
            for vorgangslistenindex in range(len(self.vorgangsliste)):
                if self.vorgangsliste[vorgangslistenindex].index == nachfolger:
                    temp_list.append(self.vorgangsliste[vorgangslistenindex].faz)
        if len(temp_list) == 0:
            return 0
        else:
            return min(temp_list) - self.vorgangsliste[index].fez
