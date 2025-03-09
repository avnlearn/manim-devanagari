import os
from manim import SVGMobject

ICON_ROOT_DIR = f"{os.path.dirname(__file__)}"
OPEN_MOJI_DIR_BLACK = f"{ICON_ROOT_DIR}/openmoji/openmoji-svg-black"
OPEN_MOJI_DIR_COLOR = f"{ICON_ROOT_DIR}/openmoji/openmoji-svg-color"
EXTRAS_OPEN_MOJI_CSV = f"{ICON_ROOT_DIR}/openmoji/extras-openmoji.csv"
EXTRAS_UNICODE_CSV = f"{ICON_ROOT_DIR}/openmoji/extras-unicode.csv"
OPEN_MOJI_CSV = f"{ICON_ROOT_DIR}/openmoji/openmoji.csv"


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


class Font_Awesome_5(SVGMobject):
    def __init__(self, icon_name: str, icons_type: str = "solid", **kwargs):
        icon_name = icon_name.lower()
        icons_type = icons_type.lower()
        svg_file = (
            f"{ICON_ROOT_DIR}/fontawesome-free-5/svgs/{icons_type}/{icon_name}.svg"
        )
        if os.path.exists(svg_file) and os.path.isfile(svg_file):
            super().__init__(file_name=svg_file, **kwargs)


class Font_Awesome_6(SVGMobject):
    def __init__(self, icon_name: str, icons_type: str = "solid", **kwargs):
        icon_name = icon_name.lower()
        icons_type = icons_type.lower()
        svg_file = (
            f"{ICON_ROOT_DIR}/fontawesome-free-6/svgs/{icons_type}/{icon_name}.svg"
        )
        if os.path.exists(svg_file) and os.path.isfile(svg_file):
            super().__init__(file_name=svg_file, **kwargs)
