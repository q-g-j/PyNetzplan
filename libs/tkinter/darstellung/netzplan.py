# -*- coding: utf-8 -*-

import tkinter as tk
import io
import math

from libs.berechnungen import Berechnungen
from libs.tkinter.tkcommon import TkCommon
from libs.tkinter.fonts import Fonts
from libs.tkinter.scrollingframe import ScrollingFrame
from libs.vorgang import Vorgang
from PIL import Image


class Netzplan(tk.Toplevel):
    def __init__(self, _root, _vorgangsliste):
        tk.Toplevel.__init__(self, _root, borderwidth=0, background='white')
        self.__root = _root
        self.title("Netzplan")
        self.withdraw()

        self.__fonts = Fonts()

        self.__canvas_netzplan = None

        self.__vorgangs_breite = 240
        self.__vorgangs_zeilen_hoehe = 28
        self.__vorgangs_spalten_breite = 50
        self.__vorgangs_hoehe = self.__vorgangs_zeilen_hoehe * 4 + 5

        self.___vorgangs_abstand_horizontal = 80
        self.___vorgangs_abstand_vertikal = 50

        self.__offset_vertikal = 50
        self.__offset_horizontal = 50

        self.__vorgangsliste = _vorgangsliste
        self.__vorgangs_2d_liste = list()

        self.__berechnungen = Berechnungen(self.__vorgangsliste)
        self.__spalten, self.__zeilen = self.__berechnungen.berechne_netzplan(self.__vorgangsliste)

        spalten_liste = list()
        for vorgang in self.__vorgangsliste:
            if vorgang.grid_coords['spalte'] not in spalten_liste:
                spalten_liste.append(vorgang.grid_coords['spalte'])

        for spalte in range(max(spalten_liste) + 1):
            self.__vorgangs_2d_liste.append(list())

        for spalte in range(max(spalten_liste) + 1):
            for vorgang in self.__vorgangsliste:
                if vorgang.grid_coords['spalte'] == spalte:
                    self.__vorgangs_2d_liste[spalte].append(vorgang)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.__scrolling_frame = ScrollingFrame(self)
        self.__scrolling_frame.grid(column=0, row=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.__canvas_netzplan = tk.Canvas(self.__scrolling_frame.frame, background='white', highlightthickness=0)
        self.__canvas_netzplan.pack(fill=tk.BOTH, expand=True)

        for vorgangsindex in range(len(self.__vorgangsliste)):
            self.zeichne_vorgang(self.__vorgangsliste[vorgangsindex], False)

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
        legende.grid_coords['spalte'] = 0
        legende.grid_coords['zeile'] = self.__zeilen

        self.zeichne_vorgang(legende, True)

        self.__zeilen += 1

        bbox = self.__canvas_netzplan.bbox('all')

        canvas_width = bbox[2] - bbox[0] + 2 * self.__offset_horizontal
        canvas_height = bbox[3] - bbox[1] + 2 * self.__offset_vertikal

        self.__canvas_netzplan.config(width=canvas_width, height=canvas_height)

        if canvas_width + 100 > self.__root.winfo_screenwidth():
            canvas_width = self.__root.winfo_screenwidth() * 0.9
        if canvas_height + 100 > self.__root.winfo_screenheight():
            canvas_height = self.__root.winfo_screenheight() * 0.8

        self.minsize(500, 300)

        self.__scrolling_frame.canvas.config(width=canvas_width, height=canvas_height)
        self.__scrolling_frame.canvas.configure(scrollregion=self.__scrolling_frame.canvas.bbox("all"))

        self.deiconify()

        TkCommon.center(self)

        self.update()

        # ps = self.__canvas_netzplan.postscript(colormode='color', x=0, y=0, pagewidth=canvas_width * 20, pageheight=canvas_height * 20)
        #
        # """ canvas postscripts seem to be saved at 0.60 scale, so we need to increase the default dpi (72) by 60 percent """
        # im = Netzplan.open_eps(ps, dpi=119.5)
        # im.save('out.eps', dpi=(119.5, 119.5))
        #
        # img = Image.open('out.eps')
        # img.save('out.png', 'png', quality=99)

    @staticmethod
    def open_eps(ps, dpi=300.0):
        img = Image.open(io.BytesIO(ps.encode('utf-8')))
        original = img.size
        scale = dpi / 72.0
        # if dpi != 0:
        #     img.load()
        if scale != 1:
            new = (int(round(scale * original[0])), int(round(scale * original[1])))
            img.thumbnail(new, Image.ANTIALIAS)
        return img

    def zeichne_vorgang(self, _vorgang, _ist_legende):
        # weiß und grau ohne linke vertikale Linie
        vorgang_x1 = self.__offset_horizontal + _vorgang.grid_coords['spalte'] * (
                self.__vorgangs_breite + self.___vorgangs_abstand_horizontal) + 1

        # weiß und grau ohne obere horizontale Linie
        vorgang_y1 = self.__offset_vertikal + _vorgang.grid_coords['zeile'] * (
                self.__vorgangs_hoehe + self.___vorgangs_abstand_vertikal) + 1

        # horizontale Linie oberhalb des grauen Rechtecks:
        linie_horizontal_1_x1 = vorgang_x1 - 1
        linie_horizontal_1_y1 = vorgang_y1 + self.__vorgangs_zeilen_hoehe + 1
        linie_horizontal_1_x2 = linie_horizontal_1_x1 + self.__vorgangs_breite
        linie_horizontal_1_y2 = linie_horizontal_1_y1
        self.__canvas_netzplan.create_line(
            linie_horizontal_1_x1, linie_horizontal_1_y1, linie_horizontal_1_x2, linie_horizontal_1_y2
        )

        # if _vorgang.index == 1:
        #     linie_horizontal = self.__canvas_netzplan.bbox(linie_horizontal_id)
        #     linie_horizontal_width = linie_horizontal[2] - linie_horizontal[0]
        #     linie_horizontal_height = linie_horizontal[3] - linie_horizontal[1]
        #     print("linie_horizontal_width =", linie_horizontal_width)
        #     print("linie_horizontal_height =", linie_horizontal_height)

        # graues Rechteck, oberer Teil:
        graues_rechteck_oben_x1 = vorgang_x1
        graues_rechteck_oben_y1 = vorgang_y1 + self.__vorgangs_zeilen_hoehe + 2
        graues_rechteck_oben_x2 = vorgang_x1 + self.__vorgangs_breite - 2
        graues_rechteck_oben_y2 = graues_rechteck_oben_y1 + self.__vorgangs_zeilen_hoehe - 2
        self.__canvas_netzplan.create_rectangle(
            graues_rechteck_oben_x1, graues_rechteck_oben_y1, graues_rechteck_oben_x2, graues_rechteck_oben_y2,
            width=0, outline="", fill='grey80'
        )

        # if _vorgang.index == 1:
        #     graues_rechteck_oben = self.__canvas_netzplan.bbox(graues_rechteck_oben_id)
        #     graues_rechteck_oben_width = graues_rechteck_oben[2] - graues_rechteck_oben[0]
        #     graues_rechteck_oben_height = graues_rechteck_oben[3] - graues_rechteck_oben[1]
        #
        #     print("graues_rechteck_oben_width =", graues_rechteck_oben_width)
        #     print("graues_rechteck_oben_height =", graues_rechteck_oben_height)

        # horizontale Linie in der Mitte des grauen Rechtecks:
        linie_horizontal_2_x1 = vorgang_x1 - 1
        linie_horizontal_2_y1 = vorgang_y1 + self.__vorgangs_zeilen_hoehe * 2
        linie_horizontal_2_x2 = linie_horizontal_1_x1 + self.__vorgangs_breite
        linie_horizontal_2_y2 = linie_horizontal_2_y1
        self.__canvas_netzplan.create_line(
            linie_horizontal_2_x1, linie_horizontal_2_y1, linie_horizontal_2_x2, linie_horizontal_2_y2
        )

        # graues Rechteck, unterer Teil:
        graues_rechteck_unten_x1 = vorgang_x1
        graues_rechteck_unten_y1 = vorgang_y1 + self.__vorgangs_zeilen_hoehe * 2 + 1
        graues_rechteck_unten_x2 = vorgang_x1 + self.__vorgangs_breite - 2
        graues_rechteck_unten_y2 = graues_rechteck_unten_y1 + self.__vorgangs_zeilen_hoehe - 2
        self.__canvas_netzplan.create_rectangle(
            graues_rechteck_unten_x1, graues_rechteck_unten_y1, graues_rechteck_unten_x2, graues_rechteck_unten_y2,
            width=0, outline="", fill='grey80'
        )

        # if _vorgang.index == 1:
        #     graues_rechteck_unten = self.__canvas_netzplan.bbox(graues_rechteck_unten_id)
        #     graues_rechteck_unten_width = graues_rechteck_unten[2] - graues_rechteck_unten[0]
        #     graues_rechteck_unten_height = graues_rechteck_unten[3] - graues_rechteck_unten[1]
        #
        #     print("graues_rechteck_oben_width =", graues_rechteck_unten_width)
        #     print("graues_rechteck_oben_height =", graues_rechteck_unten_height)

        # horizontale Linie unterhalb des grauen Rechtecks:
        linie_horizontal_3_x1 = vorgang_x1 - 1
        linie_horizontal_3_y1 = vorgang_y1 + self.__vorgangs_zeilen_hoehe * 3 - 1
        linie_horizontal_3_x2 = linie_horizontal_3_x1 + self.__vorgangs_breite
        linie_horizontal_3_y2 = linie_horizontal_3_y1
        self.__canvas_netzplan.create_line(
            linie_horizontal_3_x1, linie_horizontal_3_y1, linie_horizontal_3_x2, linie_horizontal_3_y2
        )

        # vertikale Linie links:
        linie_vertikal_links_x1 = linie_horizontal_1_x1
        linie_vertikal_links_y1 = linie_horizontal_1_y1
        linie_vertikal_links_x2 = linie_horizontal_1_x1
        linie_vertikal_links_y2 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe * 2 - 1
        linie_vertikal_links_id = self.__canvas_netzplan.create_line(
            linie_vertikal_links_x1, linie_vertikal_links_y1, linie_vertikal_links_x2, linie_vertikal_links_y2
        )

        if _vorgang.index == 1:
            linie_vertikal_links = self.__canvas_netzplan.bbox(linie_vertikal_links_id)
            linie_vertikal_links_width = linie_vertikal_links[2] - linie_vertikal_links[0]
            linie_vertikal_links_height = linie_vertikal_links[3] - linie_vertikal_links[1]
            print("linie_vertikal_links_width =", linie_vertikal_links_width)
            print("linie_vertikal_links_height =", linie_vertikal_links_height)

        # vertikale Linie rechts:
        linie_vertikal_rechts_x1 = linie_horizontal_1_x2 - 1
        linie_vertikal_rechts_y1 = linie_horizontal_1_y1
        linie_vertikal_rechts_x2 = linie_vertikal_rechts_x1
        linie_vertikal_rechts_y2 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe * 2 - 1
        self.__canvas_netzplan.create_line(
            linie_vertikal_rechts_x1, linie_vertikal_rechts_y1, linie_vertikal_rechts_x2, linie_vertikal_rechts_y2
        )

        # vertikale Linie Index|Beschreibung und Dauer|Zeiteinheit:
        linie_vertikal_index_beschreibung_x1 = linie_vertikal_links_x1 + self.__vorgangs_spalten_breite
        linie_vertikal_index_beschreibung_y1 = linie_horizontal_1_y1
        linie_vertikal_index_beschreibung_x2 = linie_vertikal_links_x1 + self.__vorgangs_spalten_breite
        linie_vertikal_index_beschreibung_y2 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe * 2 - 1
        self.__canvas_netzplan.create_line(
            linie_vertikal_index_beschreibung_x1, linie_vertikal_index_beschreibung_y1,
            linie_vertikal_index_beschreibung_x2, linie_vertikal_index_beschreibung_y2
        )

        # vertikale Linie Zeiteinheit|GP:
        linie_vertikal_zeiteinheit_gp_x1 = linie_horizontal_1_x2 - self.__vorgangs_spalten_breite * 2 - 1
        linie_vertikal_zeiteinheit_gp_y1 = linie_horizontal_2_y1
        linie_vertikal_zeiteinheit_gp_x2 = linie_horizontal_1_x2 - self.__vorgangs_spalten_breite * 2 - 1
        linie_vertikal_zeiteinheit_gp_y2 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe * 2 - 1
        self.__canvas_netzplan.create_line(
            linie_vertikal_zeiteinheit_gp_x1, linie_vertikal_zeiteinheit_gp_y1,
            linie_vertikal_zeiteinheit_gp_x2, linie_vertikal_zeiteinheit_gp_y2
        )

        # vertikale Linie GP|FP:
        linie_vertikal_gp_fp_x1 = linie_horizontal_1_x2 - self.__vorgangs_spalten_breite - 1
        linie_vertikal_gp_fp_y1 = linie_horizontal_2_y1
        linie_vertikal_gp_fp_x2 = linie_horizontal_1_x2 - self.__vorgangs_spalten_breite - 1
        linie_vertikal_gp_fp_y2 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe * 2 - 1
        self.__canvas_netzplan.create_line(
            linie_vertikal_gp_fp_x1, linie_vertikal_gp_fp_y1,
            linie_vertikal_gp_fp_x2, linie_vertikal_gp_fp_y2
        )

        # FAZ-Text:
        text_faz_x1 = vorgang_x1 - 1 + self.__vorgangs_spalten_breite / 2
        text_faz_y1 = vorgang_y1 + 1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_faz_x1, text_faz_y1, text=_vorgang.faz, font=self.__fonts.font_main)

        # FEZ-Text:
        text_fez_x1 = linie_horizontal_1_x2 - 1 - self.__vorgangs_spalten_breite / 2
        text_fez_y1 = vorgang_y1 + 1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_fez_x1, text_fez_y1, text=_vorgang.fez, font=self.__fonts.font_main)

        # Index-Text:
        text_index_x1 = vorgang_x1 - 1 + self.__vorgangs_spalten_breite / 2
        text_index_y1 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(
            text_index_x1, text_index_y1, text=_vorgang.index, font=self.__fonts.font_main_bold
        )

        # Beschreibung-Text:
        text_beschreibung_x1 = vorgang_x1 + self.__vorgangs_breite - 1 - (
                self.__vorgangs_breite - self.__vorgangs_spalten_breite) / 2
        text_beschreibung_y1 = linie_horizontal_1_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(
            text_beschreibung_x1, text_beschreibung_y1, text=_vorgang.beschreibung, font=self.__fonts.font_main
        )

        # Dauer-Text:
        text_dauer_x1 = vorgang_x1 - 1 + self.__vorgangs_spalten_breite / 2
        text_dauer_y1 = linie_horizontal_2_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(
            text_dauer_x1, text_dauer_y1, text=_vorgang.dauer, font=self.__fonts.font_main
        )

        # Zeiteinheit-Text:
        text_zeiteinheit_x1 = vorgang_x1 + self.__vorgangs_spalten_breite - 2 + (
                self.__vorgangs_breite - self.__vorgangs_spalten_breite * 3) / 2
        text_zeiteinheit_y1 = linie_horizontal_2_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(
            text_zeiteinheit_x1, text_zeiteinheit_y1, text=_vorgang.zeiteinheit, font=self.__fonts.font_main
        )

        # SAZ-Text:
        text_saz_x1 = vorgang_x1 - 1 + self.__vorgangs_spalten_breite / 2
        text_saz_y1 = linie_horizontal_3_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_saz_x1, text_saz_y1, text=_vorgang.saz, font=self.__fonts.font_main)

        # SEZ-Text:
        text_sez_x1 = linie_horizontal_1_x2 - 1 - self.__vorgangs_spalten_breite / 2
        text_sez_y1 = linie_horizontal_3_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_sez_x1, text_sez_y1, text=_vorgang.sez, font=self.__fonts.font_main)

        # GP-Text:
        text_gp_x1 = linie_vertikal_rechts_x1 - self.__vorgangs_spalten_breite - self.__vorgangs_spalten_breite / 2
        text_gp_y1 = linie_horizontal_2_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_gp_x1, text_gp_y1, text=_vorgang.gp, font=self.__fonts.font_main)

        # FP-Text:
        text_fp_x1 = linie_horizontal_1_x2 - 1 - self.__vorgangs_spalten_breite / 2
        text_fp_y1 = linie_horizontal_2_y1 + self.__vorgangs_zeilen_hoehe / 2
        self.__canvas_netzplan.create_text(text_fp_x1, text_fp_y1, text=_vorgang.fp, font=self.__fonts.font_main)
