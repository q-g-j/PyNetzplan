# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
# from PIL import Image
# import time

from libs.berechnungen import Berechnungen
from libs.tkinter.fonts import Fonts
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.scrollingframe import ScrollingFrame
from libs.tkinter.style import Style
from libs.vorgang import Vorgang


class Netzplan(tk.Toplevel):
    def __init__(self, _root, _vorgangsliste):
        tk.Toplevel.__init__(self, _root)
        self.__root = _root
        self.withdraw()

        self.vorgangsliste = _vorgangsliste

        self.__vorgangs_2d_liste = list()

        self.__berechnungen = Berechnungen(self.vorgangsliste)
        self.__spalten, self.__zeilen = self.__berechnungen.berechne_netzplan(self.vorgangsliste)

        spalten_liste = list()
        for vorgang in self.vorgangsliste:
            if vorgang.grid_spalte not in spalten_liste:
                spalten_liste.append(vorgang.grid_spalte)

        for spalte in range(max(spalten_liste)):
            self.__vorgangs_2d_liste.append(list())

        for spalte in range(max(spalten_liste)):
            for vorgang in self.vorgangsliste:
                if vorgang.grid_spalte == spalte:
                    self.__vorgangs_2d_liste[spalte].append(vorgang)

        self.config(padx=0, pady=0)
        self.title("Netzplan")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrolling_frame = ScrollingFrame(self)
        self.__scrolling_frame.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        zeilen_hoehe = 0
        zeile_max = 0
        for vorgangsindex in range(len(self.vorgangsliste)):
            vorgang_frame = _VorgangFrame(self.__scrolling_frame.frame, self.vorgangsliste[vorgangsindex])
            vorgang_frame.grid(column=self.vorgangsliste[vorgangsindex].grid_spalte,
                               row=self.vorgangsliste[vorgangsindex].grid_zeile, padx=40, pady=20, sticky='w')
            if zeile_max < self.vorgangsliste[vorgangsindex].grid_zeile:
                zeile_max = self.vorgangsliste[vorgangsindex].grid_zeile
            zeilen_hoehe = vorgang_frame.height

        legende = Vorgang()
        legende.index = "Nr."
        legende.beschreibung = "Beschreibung"
        legende.dauer = "Dauer"
        legende.zeiteinheit = "Zeiteinheit"
        legende.faz = "FAZ"
        legende.fez = "FEZ"
        legende.saz = "SAZ"
        legende.sez = "SEZ"
        legende.gp = "GP"
        legende.fp = "FP"

        legenden_frame = _VorgangFrame(self.__scrolling_frame.frame, legende)
        legenden_frame.grid(column=0, row=zeile_max + 1, padx=40, pady=(60, 30), sticky='w')
        self.__zeilen += 1

        frame_breiten_liste = list()

        for i in range(len(self.__vorgangs_2d_liste)):
            frame_breiten_liste.append(list())
            for j in range(len(self.__vorgangs_2d_liste[i])):
                frame_breiten_liste[i].append(self.__vorgangs_2d_liste[i][j].frame_breite)

        frame_breiten_gesamt = 0

        for i in range(len(frame_breiten_liste)):
            frame_breiten_gesamt += max(frame_breiten_liste[i])

        if self.__spalten * 80 + frame_breiten_gesamt + 50 > self.__root.winfo_screenwidth() or \
                self.__zeilen * (zeilen_hoehe + 40) + 40 > self.__root.winfo_screenheight():
            window_width = self.__root.winfo_screenwidth() * 0.9
            window_height = self.__root.winfo_screenheight() * 0.8
        else:
            window_width = self.__spalten * 80 + frame_breiten_gesamt + 50
            window_height = self.__zeilen * (zeilen_hoehe + 40) + 40

        self.minsize(500, 300)

        self.__scrolling_frame.canvas.config(width=window_width, height=window_height)

        self.__scrolling_frame.canvas.configure(scrollregion=self.__scrolling_frame.canvas.bbox("all"))

        self.deiconify()

        TkCommon.center(self)


class _VorgangFrame(ttk.Frame):
    def __init__(self, _frame, _vorgang):
        Style.set_styles()
        ttk.Frame.__init__(self, _frame, relief=tk.SOLID, style='VorgangWhite.TFrame')

        self.width = 0
        self.height = 0

        fonts = Fonts()

        frame_frueheste = ttk.Frame(self, style='VorgangWhite.TFrame')
        frame_frueheste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_frueheste.pack_propagate(False)

        frame_schwarz_name = ttk.Frame(self, style='VorgangBlack.TFrame')
        frame_schwarz_name.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_name.pack_propagate(False)

        frame_schwarz_dauer_puffer = ttk.Frame(self, style='VorgangBlack.TFrame')
        frame_schwarz_dauer_puffer.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_dauer_puffer.pack_propagate(False)

        frame_spaeteste = ttk.Frame(self, style='VorgangWhite.TFrame')
        frame_spaeteste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_spaeteste.pack_propagate(False)

        frame_faz = ttk.Frame(frame_frueheste, width=50)
        frame_faz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_faz.pack_propagate(False)

        frame_fez = ttk.Frame(frame_frueheste, width=50)
        frame_fez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_fez.pack_propagate(False)

        frame_index = ttk.Frame(frame_schwarz_name, width=50)
        frame_index.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_index.pack_propagate(False)

        frame_beschreibung = ttk.Frame(frame_schwarz_name)
        frame_beschreibung.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_beschreibung.pack_propagate(False)

        frame_dauer = ttk.Frame(frame_schwarz_dauer_puffer, width=50)
        frame_dauer.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_dauer.pack_propagate(False)

        frame_zeiteinheit = ttk.Frame(frame_schwarz_dauer_puffer)
        frame_zeiteinheit.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_zeiteinheit.pack_propagate(False)

        frame_gp = ttk.Frame(frame_schwarz_dauer_puffer, width=50)
        frame_gp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_gp.pack_propagate(False)

        frame_fp = ttk.Frame(frame_schwarz_dauer_puffer, width=50)
        frame_fp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_fp.pack_propagate(False)

        frame_saz = ttk.Frame(frame_spaeteste, width=50)
        frame_saz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_saz.pack_propagate(False)

        frame_sez = ttk.Frame(frame_spaeteste, width=50)
        frame_sez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_sez.pack_propagate(False)

        label_faz = ttk.Label(frame_faz, text=str(_vorgang.faz), style='VorgangWhite.TLabel',
                              font=fonts.font_main)
        label_faz.pack(fill=tk.BOTH, expand=True)

        label_fez = ttk.Label(frame_fez, text=str(_vorgang.fez), style='VorgangWhite.TLabel',
                              font=fonts.font_main)
        label_fez.pack(fill=tk.BOTH, expand=True)

        label_index = ttk.Label(frame_index, text=str(_vorgang.index), style='VorgangGrey.TLabel',
                                font=fonts.font_main)
        label_index.pack(fill=tk.BOTH, expand=True)

        label_beschreibung = ttk.Label(frame_beschreibung, text=_vorgang.beschreibung, style='VorgangGrey.TLabel',
                                       font=fonts.font_main)
        label_beschreibung.pack(fill=tk.BOTH, expand=True)

        label_dauer = ttk.Label(frame_dauer, text=str(_vorgang.dauer), style='VorgangGrey.TLabel',
                                font=fonts.font_main)
        label_dauer.pack(fill=tk.BOTH, expand=True)

        label_zeiteinheit = ttk.Label(frame_zeiteinheit, text=str(_vorgang.zeiteinheit), style='VorgangGrey.TLabel',
                                      font=fonts.font_main)
        label_zeiteinheit.pack(fill=tk.BOTH, expand=True)

        label_gp = ttk.Label(frame_gp, text=str(_vorgang.gp), style='VorgangGrey.TLabel',
                             font=fonts.font_main)
        label_gp.pack(fill=tk.BOTH, expand=True)

        label_fp = ttk.Label(frame_fp, text=str(_vorgang.fp), style='VorgangGrey.TLabel',
                             font=fonts.font_main)
        label_fp.pack(fill=tk.BOTH, expand=True)

        label_saz = ttk.Label(frame_saz, text=str(_vorgang.saz), style='VorgangWhite.TLabel',
                              font=fonts.font_main)
        label_saz.pack(fill=tk.BOTH, expand=True)

        label_sez = ttk.Label(frame_sez, text=str(_vorgang.sez), style='VorgangWhite.TLabel',
                              font=fonts.font_main)
        label_sez.pack(fill=tk.BOTH, expand=True)

        if label_beschreibung.winfo_reqwidth() + 10 < 3 * 50:
            label_beschreibung_width = 3 * 50
        else:
            label_beschreibung_width = label_beschreibung.winfo_reqwidth() + 10

        label_zeiteinheit_width = label_zeiteinheit.winfo_reqwidth() + 10

        vorgangframe_base_width = label_beschreibung_width + 50 + 3
        vorgangframe_base_height = label_beschreibung.winfo_reqheight()

        if vorgangframe_base_width < label_zeiteinheit_width + 3 * 50 + 5:
            vorgangframe_base_width = label_zeiteinheit_width + 3 * 50 + 5

        self.width = vorgangframe_base_width
        self.height = vorgangframe_base_height * 4 + 3

        frame_frueheste.config(width=vorgangframe_base_width, height=vorgangframe_base_height)
        frame_schwarz_name.config(width=vorgangframe_base_width, height=vorgangframe_base_height + 2)
        frame_schwarz_dauer_puffer.config(width=vorgangframe_base_width, height=vorgangframe_base_height + 1)
        frame_spaeteste.config(width=vorgangframe_base_width, height=vorgangframe_base_height)
        frame_faz.config(height=vorgangframe_base_height)
        frame_fez.config(height=vorgangframe_base_height)
        frame_index.config(height=vorgangframe_base_height)
        frame_beschreibung.config(width=vorgangframe_base_width - 50 - 3, height=vorgangframe_base_height)
        frame_dauer.config(height=vorgangframe_base_height)
        frame_zeiteinheit.config(width=vorgangframe_base_width - 3 * 50 - 5, height=vorgangframe_base_height)
        frame_gp.config(height=vorgangframe_base_height)
        frame_fp.config(height=vorgangframe_base_height)
        frame_saz.config(height=vorgangframe_base_height)
        frame_sez.config(height=vorgangframe_base_height)

        _vorgang.frame_breite = vorgangframe_base_width

        self.update_idletasks()
        self.pack_propagate(False)
