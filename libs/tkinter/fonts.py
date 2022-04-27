# -*- coding: utf-8 -*-

import platform
import pyglet

from libs.common import Common


class Fonts:
    def __init__(self):
        pyglet.font.add_file(Common.script_path + "/fonts/BowlbyOne-Regular.otf")
        pyglet.font.add_file(Common.script_path + "/fonts/JetBrainsMono-Regular.ttf")
        pyglet.font.add_file(Common.script_path + "/fonts/selawk.ttf")

        if platform.system() == "Darwin":
            self.font_title = (
                "Selawik",
                13,
                "bold"
            )
            self.font_main = (
                "Selawik",
                11,
                "normal"
            )
            self.font_main_bold = (
                "Selawik",
                11,
                "bold"
            )
            self.font_buttons = (
                "Selawik",
                11,
                "normal"
            )
            self.font_eingabe = (
                "Selawik",
                11,
                "normal"
            )
            self.font_menu = (
                "Selawik",
                10,
                "normal"
            )
            self.font_table_header = (
                "Selawik",
                13,
                "normal"
            )
            self.font_table = (
                "Selawik",
                13,
                "normal"
            )
            self.font_block = (
                "JetBrains Mono Regular",
                10,
                "normal"
            )
        else:
            self.font_title = (
                "Selawik",
                13,
                "bold"
            )
            self.font_main = (
                "Selawik",
                11,
                "normal"
            )
            self.font_main_bold = (
                "Selawik",
                11,
                "bold"
            )
            self.font_buttons = (
                "Selawik",
                11,
                "normal"
            )
            self.font_eingabe = (
                "Selawik",
                11,
                "normal"
            )
            self.font_menu = (
                "Selawik",
                10,
                "normal"
            )
            self.font_table_header = (
                "Selawik",
                13,
                "normal"
            )
            self.font_table = (
                "Selawik",
                13,
                "normal"
            )
            self.font_block = (
                "JetBrains Mono Regular",
                10,
                "normal"
            )
