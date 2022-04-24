# -*- coding: utf-8 -*-

import tkinter as tk

from libs.tkinter.fonts import Fonts
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.scrollingframe import ScrollingFrame
from libs.tkinter.style import Style


class Netzplan(tk.Toplevel):
    def __init__(self, _root, _vorgangsliste):
        tk.Toplevel.__init__(self, _root)
        self.__root = _root
        self.withdraw()

        self.vorgangsliste = _vorgangsliste

        self.config(padx=0, pady=0)
        self.title("Netzplan")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrolling_frame = ScrollingFrame(self, _background='white')
        self.__scrolling_frame.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.__vorgang_width = 0
        self.__vorgang_height = 0

        self.__spalten = 5
        self.__zeilen = 5

        spalte = 0
        zeile = 0
        for vorgangsindex in range(len(self.vorgangsliste)):
            vorgang_frame = _VorgangFrame(self.__scrolling_frame.frame, self.vorgangsliste[vorgangsindex],
                                          spalte, zeile)
            vorgang_frame.grid(column=spalte, row=zeile)
            self.__vorgang_width = vorgang_frame.width
            self.__vorgang_height = vorgang_frame.height
            self.vorgangsliste[vorgangsindex].gridx = spalte
            self.vorgangsliste[vorgangsindex].gridy = zeile
            spalte += 1

        # Berechne die Größe des Fensters:
        self.__scrolling_frame.canvas.config(width=self.__spalten * (self.__vorgang_width + 80),
                                             height=self.__zeilen * (self.__vorgang_height + 40))

        self.deiconify()
        # self.wm_transient(self.__root)
        self.resizable(width=True, height=True)
        TkCommon.center(self)


class _VorgangFrame(tk.Frame):
    def __init__(self, _frame, _vorgang, _spalte, _zeile):
        Style.set_styles()
        tk.Frame.__init__(self, _frame, relief=tk.SOLID, background='white')
        self.grid(column=_spalte, row=_zeile, padx=40, pady=20, sticky='w')

        self.width = 0
        self.height = 0

        fonts = Fonts()

        frame_frueheste = tk.Frame(self, bg='white')
        frame_frueheste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_frueheste.pack_propagate(False)

        frame_schwarz_name = tk.Frame(self, bg='black')  # +2
        frame_schwarz_name.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_name.pack_propagate(False)

        frame_schwarz_dauer_puffer = tk.Frame(self, bg='black')  # +1
        frame_schwarz_dauer_puffer.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_dauer_puffer.pack_propagate(False)

        frame_spaeteste = tk.Frame(self, bg='white')
        frame_spaeteste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_spaeteste.pack_propagate(False)

        frame_faz = tk.Frame(frame_frueheste, width=40)
        frame_faz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_faz.pack_propagate(False)

        frame_fez = tk.Frame(frame_frueheste, width=40)
        frame_fez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_fez.pack_propagate(False)

        frame_index = tk.Frame(frame_schwarz_name, width=40)
        frame_index.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_index.pack_propagate(False)

        frame_beschreibung = tk.Frame(frame_schwarz_name)
        frame_beschreibung.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_beschreibung.pack_propagate(False)

        frame_dauer = tk.Frame(frame_schwarz_dauer_puffer, width=40)
        frame_dauer.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_dauer.pack_propagate(False)

        frame_zeiteinheit = tk.Frame(frame_schwarz_dauer_puffer)
        frame_zeiteinheit.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_zeiteinheit.pack_propagate(False)

        frame_gp = tk.Frame(frame_schwarz_dauer_puffer, width=40)
        frame_gp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_gp.pack_propagate(False)

        frame_fp = tk.Frame(frame_schwarz_dauer_puffer, width=40)
        frame_fp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_fp.pack_propagate(False)

        frame_saz = tk.Frame(frame_spaeteste, width=40, bg='white')
        frame_saz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_saz.pack_propagate(False)

        frame_sez = tk.Frame(frame_spaeteste, width=40, bg='white')
        frame_sez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_sez.pack_propagate(False)

        label_faz = tk.Label(frame_faz, text=str(_vorgang.faz), foreground='black', background='white',
                             font=fonts.font_main)
        label_faz.pack(fill=tk.BOTH, expand=True)

        label_fez = tk.Label(frame_fez, text=str(_vorgang.fez), foreground='black', background='white',
                             font=fonts.font_main)
        label_fez.pack(fill=tk.BOTH, expand=True)

        label_index = tk.Label(frame_index, text=str(_vorgang.index), foreground='black', background='#d9d9d9',
                               font=fonts.font_main)
        label_index.pack(fill=tk.BOTH, expand=True)

        label_beschreibung = tk.Label(frame_beschreibung, text=_vorgang.beschreibung, foreground='black',
                                      background='#d9d9d9', font=fonts.font_main)
        label_beschreibung.pack(fill=tk.BOTH, expand=True)

        label_dauer = tk.Label(frame_dauer, text=str(_vorgang.dauer), foreground='black', background='#d9d9d9',
                               font=fonts.font_main)
        label_dauer.pack(fill=tk.BOTH, expand=True)

        label_zeiteinheit = tk.Label(frame_zeiteinheit, text=str(_vorgang.zeiteinheit), foreground='black',
                                     background='#d9d9d9', font=fonts.font_main)
        label_zeiteinheit.pack(fill=tk.BOTH, expand=True)

        label_gp = tk.Label(frame_gp, text=str(_vorgang.gp), foreground='black', background='#d9d9d9',
                            font=fonts.font_main)
        label_gp.pack(fill=tk.BOTH, expand=True)

        label_fp = tk.Label(frame_fp, text=str(_vorgang.fp), foreground='black', background='#d9d9d9',
                            font=fonts.font_main)
        label_fp.pack(fill=tk.BOTH, expand=True)

        label_saz = tk.Label(frame_saz, text=str(_vorgang.saz), foreground='black', background='white',
                             font=fonts.font_main)
        label_saz.pack(fill=tk.BOTH, expand=True)

        label_sez = tk.Label(frame_sez, text=str(_vorgang.sez), foreground='black', background='white',
                             font=fonts.font_main)
        label_sez.pack(fill=tk.BOTH, expand=True)

        if label_beschreibung.winfo_reqwidth() < 3 * 40 + 10:
            label_beschreibung_width = 3 * 40 + 10
        else:
            label_beschreibung_width = label_beschreibung.winfo_reqwidth() + 10

        label_zeiteinheit_width = label_zeiteinheit.winfo_reqwidth() + 10

        vorgangframe_base_width = label_beschreibung_width + 40 + 3
        vorgangframe_base_height = label_beschreibung.winfo_reqheight()

        if vorgangframe_base_width < label_zeiteinheit_width + 3 * 40 + 5:
            vorgangframe_base_width = label_zeiteinheit_width + 3 * 40 + 5

        self.width = vorgangframe_base_width
        self.height = vorgangframe_base_height * 4 + 3

        frame_frueheste.config(width=vorgangframe_base_width, height=vorgangframe_base_height)
        frame_schwarz_name.config(width=vorgangframe_base_width, height=vorgangframe_base_height + 2)
        frame_schwarz_dauer_puffer.config(width=vorgangframe_base_width, height=vorgangframe_base_height + 1)
        frame_spaeteste.config(width=vorgangframe_base_width, height=vorgangframe_base_height)
        frame_faz.config(height=vorgangframe_base_height)
        frame_fez.config(height=vorgangframe_base_height)
        frame_index.config(height=vorgangframe_base_height)
        frame_beschreibung.config(width=vorgangframe_base_width - 40 - 3, height=vorgangframe_base_height)
        frame_dauer.config(height=vorgangframe_base_height)
        frame_zeiteinheit.config(width=vorgangframe_base_width - 3 * 40 - 5, height=vorgangframe_base_height)
        frame_gp.config(height=vorgangframe_base_height)
        frame_fp.config(height=vorgangframe_base_height)
        frame_saz.config(height=vorgangframe_base_height)
        frame_sez.config(height=vorgangframe_base_height)

        self.update_idletasks()
        self.pack_propagate(False)
