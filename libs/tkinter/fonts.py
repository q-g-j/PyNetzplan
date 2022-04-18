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
            self.font_header = (
                "Selawik",
                14,
                "normal"
            )
            self.font_main = (
                "Selawik",
                12,
                "normal"
            )
            self.font_block = (
                "JetBrains Mono Regular",
                12,
                "normal"
            )
            self.font_title = (
                "Selawik",
                14,
                "bold"
            )
        else:
            self.font_header = (
                "Selawik",
                12,
                "normal"
            )
            self.font_main = (
                "Selawik",
                10,
                "normal"
            )
            self.font_block = (
                "JetBrains Mono Regular",
                10,
                "normal"
            )
            self.font_title = (
                "Selawik",
                12,
                "bold"
            )
