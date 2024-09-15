from manim import *
import manimpango
import functools


@functools.lru_cache(maxsize=None)
def font_list() -> list[str]:
    return manimpango.list_fonts()


def check_font(self, font: str, tuple_value=False) -> bool:
    fonts_list = font_list()
    font_variants = [font, font.lower(), font.capitalize(), font.title()]

    if font.lower() == "sans-serif":
        font = "sans"

    for variant in font_variants:
        if variant in fonts_list:
            return (variant, True) if tuple_value else True

    logger.warning(f"Font {font} not in {fonts_list}.")
    return (font, False) if tuple_value else False


def check_default_font(self, font: str) -> str:
    fonts = [
        font,
        "Lohit Devanagari",
        "Arial Unicode MS",
        "Noto Sans Devanagari",
        "Mangal",
        "Devanagari New",
        "Nirmala UI",
        "Hind",
    ]
    for f in fonts:
        f, check_font = check_font(f, tuple_value=True)
        if check_font:
            return f

    logger.error(f"Font {font} not in {fonts}.")
