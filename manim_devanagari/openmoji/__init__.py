import os
from manim import SVGMobject

OPEN_MOJI_DIR_BLACK = f"{os.path.dirname(__file__)}/openmoji-svg-black"
OPEN_MOJI_DIR_COLOR = f"{os.path.dirname(__file__)}/openmoji-svg-color"
EXTRAS_OPEN_MOJI_CSV = f"{os.path.dirname(__file__)}/extras-openmoji.csv"
EXTRAS_UNICODE_CSV = f"{os.path.dirname(__file__)}/extras-unicode.csv"
OPEN_MOJI_CSV = f"{os.path.dirname(__file__)}/openmoji.csv"


class OpenMoji(SVGMobject):
    def __init__(self, hexcode: str, openmoji_color: bool = True, **kwargs):
        hexcode = hexcode.upper()
        svg_file = f"{OPEN_MOJI_DIR_BLACK}/{hexcode}.svg"
        if openmoji_color:
            svg_file = f"{OPEN_MOJI_DIR_COLOR}/{hexcode}.svg"
        if os.path.exists(svg_file):
            super().__init__(file_name=svg_file, **kwargs)


class uOpenMoji(OpenMoji):
    def __init__(self, unicode, openmoji_color=True, **kwargs):
        hexcode = hex(ord(unicode[0]))
        super().__init__(hexcode[2:], openmoji_color, **kwargs)
