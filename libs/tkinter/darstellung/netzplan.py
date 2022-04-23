# -*- coding: utf-8 -*-

import tkinter as tk

from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.scrollingframe import ScrollingFrame


class Netzplan:
    def __init__(self, _root, _spalten, _zeilen):
        self.__root = _root
        self.__spalten = _spalten
        self.__zeilen = _zeilen

        self.__vorgangs2Dliste = list()

        toplevel = tk.Toplevel(self.__root)
        toplevel.config(padx=0, pady=0)
        toplevel.title("Netzplan")

        toplevel.grid_columnconfigure(0, weight=1)
        toplevel.grid_rowconfigure(0, weight=1)

        width = self.__spalten * 165 + self.__spalten * 20 * 2
        height = self.__zeilen * 64 + self.__zeilen * 20 * 2

        self.__scrolling_frame = ScrollingFrame(toplevel, _width=width, _height=height, _background='white')
        self.__scrolling_frame.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        for spalte in range(self.__spalten):
            for zeile in range(self.__zeilen):
                vorgang = VorgangFrame(self.__scrolling_frame.frame, spalte, zeile)
                vorgang.grid(column=spalte, row=zeile)
                vorgang.pack_propagate(False)

        TkCommon.center(toplevel)


class VorgangFrame(tk.Frame):
    def __init__(self, _frame, _spalte, _zeile):
        tk.Frame.__init__(self, _frame, relief=tk.SOLID, width=165, height=83, bg='white')

        self.grid(column=_spalte, row=_zeile, padx=20, pady=20, sticky='w')

        frame_frueheste = tk.Frame(self, width=165, height=20, bg='white')
        frame_frueheste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_frueheste.pack_propagate(False)

        frame_schwarz_name = tk.Frame(self, width=165, height=22, bg='black')
        frame_schwarz_name.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_name.pack_propagate(False)

        frame_schwarz_dauer_puffer = tk.Frame(self, width=165, height=21, bg='black')
        frame_schwarz_dauer_puffer.pack(side=tk.TOP, padx=(0, 0), pady=(0, 0), anchor='nw')
        frame_schwarz_dauer_puffer.pack_propagate(False)

        frame_spaeteste = tk.Frame(self, width=165, height=20, bg='white')
        frame_spaeteste.pack(side=tk.TOP, padx=(0, 0), anchor='nw')
        frame_spaeteste.pack_propagate(False)

        frame_faz = tk.Frame(frame_frueheste, width=40, height=20)
        frame_faz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_faz.pack_propagate(False)

        frame_fez = tk.Frame(frame_frueheste, width=40, height=20)
        frame_fez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_fez.pack_propagate(False)

        frame_index = tk.Frame(frame_schwarz_name, width=40, height=20)
        frame_index.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_index.pack_propagate(False)

        frame_beschreibung = tk.Frame(frame_schwarz_name, width=122, height=20)
        frame_beschreibung.pack(padx=(1, 0), pady=(1, 0), side=tk.LEFT, anchor='nw')
        frame_beschreibung.pack_propagate(False)

        frame_dauer = tk.Frame(frame_schwarz_dauer_puffer, width=40, height=20)
        frame_dauer.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_dauer.pack_propagate(False)

        frame_leer = tk.Frame(frame_schwarz_dauer_puffer, width=40, height=20, background='#d9d9d9')
        frame_leer.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_leer.pack_propagate(False)

        frame_gp = tk.Frame(frame_schwarz_dauer_puffer, width=40, height=20)
        frame_gp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_gp.pack_propagate(False)

        frame_fp = tk.Frame(frame_schwarz_dauer_puffer, width=40, height=20)
        frame_fp.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_fp.pack_propagate(False)

        frame_saz = tk.Frame(frame_spaeteste, width=40, height=20, bg='white')
        frame_saz.pack(padx=(1, 0), pady=(0, 0), side=tk.LEFT, anchor='nw')
        frame_saz.pack_propagate(False)

        frame_sez = tk.Frame(frame_spaeteste, width=40, height=20, bg='white')
        frame_sez.pack(padx=(0, 1), pady=(0, 0), side=tk.RIGHT, anchor='nw')
        frame_sez.pack_propagate(False)

        label_faz = tk.Label(frame_faz, text="FAZ", foreground='black', background='white')
        label_faz.pack(fill=tk.BOTH, expand=True)

        label_fez = tk.Label(frame_fez, text="FEZ", foreground='black', background='white')
        label_fez.pack(fill=tk.BOTH, expand=True)

        label_index = tk.Label(frame_index, text="Nr.", foreground='black', background='#d9d9d9')
        label_index.pack(fill=tk.BOTH, expand=True)

        label_beschreibung = tk.Label(frame_beschreibung, text="Beschreibung", foreground='black', background='#d9d9d9')
        label_beschreibung.pack(fill=tk.BOTH, expand=True)

        label_dauer = tk.Label(frame_dauer, text="1 h", foreground='black', background='#d9d9d9')
        label_dauer.pack(fill=tk.BOTH, expand=True)

        label_gp = tk.Label(frame_gp, text="GP", foreground='black', background='#d9d9d9')
        label_gp.pack(fill=tk.BOTH, expand=True)

        label_fp = tk.Label(frame_fp, text="FP", foreground='black', background='#d9d9d9')
        label_fp.pack(fill=tk.BOTH, expand=True)

        label_saz = tk.Label(frame_saz, text="SAZ", foreground='black', background='white')
        label_saz.pack(fill=tk.BOTH, expand=True)

        label_sez = tk.Label(frame_sez, text="SEZ", foreground='black', background='white')
        label_sez.pack(fill=tk.BOTH, expand=True)
