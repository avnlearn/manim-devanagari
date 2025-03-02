import os
from manim import SVGMobject

OPEN_MOJI_DIR_BLACK = f"{os.path.dirname(__file__)}/openmoji-svg-black"
OPEN_MOJI_DIR_COLOR = f"{os.path.dirname(__file__)}/openmoji-svg-color"
EXTRAS_OPEN_MOJI_CSV = f"{os.path.dirname(__file__)}/extras-openmoji.csv"
EXTRAS_UNICODE_CSV = f"{os.path.dirname(__file__)}/extras-unicode.csv"
OPEN_MOJI_CSV = f"{os.path.dirname(__file__)}/openmoji.csv"


class OpenMoji(SVGMobject):
    def __init__(self, hexcode, openmoji_color=True, **kwargs):
        svg_file = f"{OPEN_MOJI_DIR_BLACK}/{hexcode}.svg"

        if openmoji_color:
            svg_file = f"{OPEN_MOJI_DIR_COLOR}/{hexcode}.svg"
        if os.path.exists(svg_file):
            super().__init__(file_name=svg_file, **kwargs)
