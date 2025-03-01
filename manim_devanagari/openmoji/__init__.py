import os
from manim import *

OPEN_MOJI_DIR_BLACK = f"{__file__}/openmoji-svg-black"
OPEN_MOJI_DIR_COLOR = f"{__file__}/openmoji-svg-black"
EXTRAS_OPEN_MOJI_CSV = f"{__file__}/extras-openmoji.csv"
EXTRAS_UNICODE_CSV = f"{__file__}/extras-unicode.csv"
OPEN_MOJI_CSV = f"{__file__}/openmoji.csv"


def openmoji(hexcode, openmoji_color=True, **kwargs):
    svg_file = None
    svg_file = f"{OPEN_MOJI_DIR_BLACK}/{hexcode}.svg"
    if openmoji_color:
        svg_file = f"{OPEN_MOJI_DIR_COLOR}/{hexcode}.svg"

    if os.path.exists(svg_file):
        return SVGMobject(svg_file, **kwargs)
