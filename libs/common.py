# -*- coding: utf-8 -*-

import os
import sys


class Common:
    script_path = ""
    config_folder = ""

    @staticmethod
    def set_script_path():
        if hasattr(sys, '_MEIPASS'):
            Common.script_path = getattr(sys, '_MEIPASS') + "/"
        else:
            Common.script_path = os.path.abspath(".") + "/"

    @staticmethod
    def string_zu_liste(string):
        liste = list()
        if string != "":
            strings = string.split(',')
            liste = [int(x) for x in strings]
        return liste

    @staticmethod
    def liste_zu_string(liste):
        vorgaenger_liste_string = ""
        for i in range(len(liste)):
            if i == len(liste) - 1:
                vorgaenger_liste_string += str(liste[i])
            else:
                vorgaenger_liste_string += str(liste[i]) + ", "
        return vorgaenger_liste_string
