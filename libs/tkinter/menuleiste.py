# -*- coding: utf-8 -*-

import json
import tkinter as tk
from tkinter import filedialog

from libs.common import Common
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.fonts import Fonts


class Menuleiste:
    def __init__(self, _root, _treeview_vorgangsliste):
        self.__root = _root
        self.__treeview_vorgangsliste = _treeview_vorgangsliste
        self.__fonts = Fonts()

    def erstelle_menuleiste(self):
        menuleiste = tk.Menu(self.__root)
        dateimenu = tk.Menu(menuleiste)
        darstellungsmenu = tk.Menu(menuleiste)

        dateimenu.add_command(label="Neue Vorgangsliste", font=self.__fonts.font_menu,
                              command=self.__menuleiste_dateimenu_neu_action)
        dateimenu.add_command(label="Öffnen ...", font=self.__fonts.font_menu,
                              command=self.__menuleiste_dateimenu_oeffne_action)
        # dateimenu.add_command(label="Speichern", font=self.__fonts.font_menu)
        dateimenu.add_command(label="Speichern als ...", font=self.__fonts.font_menu,
                              command=self.__menuleiste_dateimenu_speichern_als_action)
        dateimenu.add_command(label="Beenden", font=self.__fonts.font_menu,
                              command=self.__menuleiste_dateimenu_beenden_action)

        darstellungsmenu.add_command(label="Light-Modus", font=self.__fonts.font_menu,
                                     command=self.__menuleiste_darstellungsmenu_lightmode_action)
        darstellungsmenu.add_command(label="Dark-Modus", font=self.__fonts.font_menu,
                                     command=self.__menuleiste_darstellungsmenu_darkmode_action)

        menuleiste.add_cascade(label="Datei", menu=dateimenu)
        # menuleiste.add_cascade(label="Darstellung", menu=darstellungsmenu)

        self.__root.config(menu=menuleiste)

    def __menuleiste_darstellungsmenu_lightmode_action(self):
        self.__root.tk.call("set_theme", "light")

    def __menuleiste_darstellungsmenu_darkmode_action(self):
        self.__root.tk.call("set_theme", "dark")

    def __menuleiste_dateimenu_neu_action(self):
        for i in self.__treeview_vorgangsliste.get_children():
            self.__treeview_vorgangsliste.delete(i)

    def __menuleiste_dateimenu_oeffne_action(self):
        json_dateiname = filedialog.askopenfile(title="Vorgangsliste öffnen",
                                                filetypes=[("json-Datei", "*.json"), ("alle Dateien", "*.*")])

        if json_dateiname:
            for i in self.__treeview_vorgangsliste.get_children():
                self.__treeview_vorgangsliste.delete(i)
            json_data = json.load(json_dateiname)
            c = 0
            for vorgang in json_data:
                temp_list = list()
                try:
                    temp_list.append(vorgang['Index'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['Beschreibung'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['Dauer'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['Zeiteinheit'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['FAZ'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['FEZ'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['SAZ'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['SEZ'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['GP'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(vorgang['FP'])
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(Common.liste_zu_string(vorgang['Vorgaengerliste']))
                except KeyError:
                    temp_list.append("")
                try:
                    temp_list.append(Common.liste_zu_string(vorgang['Nachfolgerliste']))
                except KeyError:
                    temp_list.append("")

                if len(self.__treeview_vorgangsliste.get_children()) % 2 != 0:
                    self.__treeview_vorgangsliste.insert(parent='', index=c, text='', values=temp_list,
                                                         tags=('odd_row',))
                else:
                    self.__treeview_vorgangsliste.insert(parent='', index=c, text='', values=temp_list)
                c += 1

    def __menuleiste_dateimenu_speichern_action(self):
        pass

    def __menuleiste_dateimenu_speichern_als_action(self):
        json_datei = filedialog.asksaveasfile(mode='w', title="Vorgangsliste speichern",
                                              filetypes=[("json-Datei", "*.json")], defaultextension=".json")

        if json_datei:
            vorgangsliste = list()
            for item in self.__treeview_vorgangsliste.get_children():
                try:
                    index = int(self.__treeview_vorgangsliste.item(item)['values'][0])
                except (ValueError, IndexError):
                    index = ""
                try:
                    beschreibung = int(self.__treeview_vorgangsliste.item(item)['values'][1])
                except (ValueError, IndexError):
                    beschreibung = ""
                try:
                    dauer = int(self.__treeview_vorgangsliste.item(item)['values'][2])
                except (ValueError, IndexError):
                    dauer = ""
                try:
                    zeiteinheit = int(self.__treeview_vorgangsliste.item(item)['values'][3])
                except (ValueError, IndexError):
                    zeiteinheit = ""
                try:
                    faz = int(self.__treeview_vorgangsliste.item(item)['values'][4])
                except (ValueError, IndexError):
                    faz = ""
                try:
                    fez = int(self.__treeview_vorgangsliste.item(item)['values'][5])
                except (ValueError, IndexError):
                    fez = ""
                try:
                    saz = int(self.__treeview_vorgangsliste.item(item)['values'][6])
                except (ValueError, IndexError):
                    saz = ""
                try:
                    sez = int(self.__treeview_vorgangsliste.item(item)['values'][7])
                except (ValueError, IndexError):
                    sez = ""
                try:
                    gp = int(self.__treeview_vorgangsliste.item(item)['values'][8])
                except (ValueError, IndexError):
                    gp = ""
                try:
                    fp = int(self.__treeview_vorgangsliste.item(item)['values'][9])
                except (ValueError, IndexError):
                    fp = ""
                try:
                    vorgaenger_liste = Common.string_zu_liste(
                        str(self.__treeview_vorgangsliste.item(item)['values'][10]))
                except (ValueError, IndexError):
                    vorgaenger_liste = list()
                try:
                    nachfolger_liste = Common.string_zu_liste(
                        str(self.__treeview_vorgangsliste.item(item)['values'][11]))
                except (ValueError, IndexError):
                    nachfolger_liste = list()
                vorgangsliste.append({'Index': index,
                                      'Beschreibung': beschreibung,
                                      'Dauer': dauer,
                                      'Zeiteinheit': zeiteinheit,
                                      'FAZ': faz,
                                      'FEZ': fez,
                                      'SAZ': saz,
                                      'SEZ': sez,
                                      'GP': gp,
                                      'FP': fp,
                                      'Vorgaengerliste': vorgaenger_liste,
                                      'Nachfolgerliste': nachfolger_liste})

            json_data = json.dumps(vorgangsliste, indent=4)
            json_datei.write(json_data)

    def __menuleiste_dateimenu_beenden_action(self):
        self.__root.destroy()
        quit()
        