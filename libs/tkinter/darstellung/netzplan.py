# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk

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

        self.__berechnungen = Berechnungen(self.vorgangsliste)
        self.__berechnungen.berechne_netzplan(self.vorgangsliste)

        self.config(padx=0, pady=0)
        self.title("Netzplan")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrolling_frame = ScrollingFrame(self)
        self.__scrolling_frame.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.__vorgang_width = 0
        self.__vorgang_height = 0

        self.__spalten = len(self.vorgangsliste)
        self.__zeilen = 0

        spalte = 0
        zeile = 0
        zeile_max = 0
        for vorgangsindex in range(len(self.vorgangsliste)):
            vorgang_frame = _VorgangFrame(self.__scrolling_frame.frame, self.vorgangsliste[vorgangsindex])
            vorgang_frame.grid(column=self.vorgangsliste[vorgangsindex].grid_spalte,
                               row=self.vorgangsliste[vorgangsindex].grid_zeile, padx=40, pady=20, sticky='w')
            self.__vorgang_width = vorgang_frame.width
            self.__vorgang_height = vorgang_frame.height
            if zeile_max < self.vorgangsliste[vorgangsindex].grid_zeile:
                zeile_max = self.vorgangsliste[vorgangsindex].grid_zeile
            spalte += 1

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
        legenden_frame.grid(column=0, row=zeile_max + 1, padx=40, pady=20, sticky='w')
        label_leer_1 = tk.Label(self.__scrolling_frame.frame, width=0, background='white', height=4)
        label_leer_1.grid(column=0, row=zeile_max + 1)
        legenden_frame.grid(column=0, row=zeile_max + 2)

        if self.__spalten * (self.__vorgang_width + 80) > self.__root.winfo_screenwidth() or \
                self.__zeilen * (self.__vorgang_height + 50) > self.__root.winfo_screenheight():
            self.geometry("%sx%s" % (str(int(self.__root.winfo_screenwidth() * 0.9)),
                                     str(int(self.__root.winfo_screenheight() * 0.8))))
        else:
            self.__scrolling_frame.canvas.config(width=self.__spalten * (self.__vorgang_width + 80),
                                                 height=self.__zeilen * (self.__vorgang_height + 50))

        self.minsize(800, 450)
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

        _vorgang.frame_width = vorgangframe_base_width

        self.update_idletasks()
        self.pack_propagate(False)
