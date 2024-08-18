"""
Devanagari plugin for manim

Attribute
---------

* _FONT_NAME
* devanagari
* __version__

Classes
-------

* `Deva_Tex(tex_string, ....)` is normal mode (`Tex`)
* `Deva_MathTex(tex_string, ....)` is math mode (`MathTex`)
* `Deva_Text(text_string, ...)` is non-LaTeX string (`Text`)
* `Deva_MarkupText(text_string, ...)` is non-LaTeX string (`MarkupText`)
* `Question_Header(question_no,...)` is Question Header
* `Solution_Header(ans, ...)` is Solution
* `Cancel(...)` is cancel mobject

"""

from manim import *

__version__ = "1.0.5"

devanagari = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    documentclass="\\documentclass[preview]{standalone}",
    preamble="\\usepackage{fontspec}\n\\usepackage{polyglossia}\n\\usepackage{cancel}\n\\setmainlanguage{english}\n\\setotherlanguage{hindi}\\setmainfont[Script=Devanagari]{Noto Sans}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
)

_FONT_NAME = "sans-serif"
# _FONT_NAME="Noto Sans"


class Deva_Tex(Tex):
    """Devanagari and English string compiled with LaTeX in normal mode."""

    def __init__(self, *args, font_size=20, **kwargs):
        super().__init__(*args, tex_template=devanagari, font_size=font_size, **kwargs)


class Deva_MathTex(MathTex):
    """Devanagari and English string compiled with LaTeX in math mode."""

    def __init__(self, *args, font_size=20, **kwargs):
        super().__init__(*args, tex_template=devanagari, font_size=font_size, **kwargs)


class Deva_Text(Text):
    """Display (non-LaTeX) text rendered using Pango ."""

    def __init__(self, *args, font=_FONT_NAME, font_size=16, **kwargs):
        super().__init__(*args, font=font, font_size=font_size, **kwargs)


class Deva_MarkupText(MarkupText):
    """
    Display (non-LaTeX) text rendered using Pango .

    Text objects behave like a VGroup-like iterable of all characters in the given text. In particular, slicing is possible.

    What is PangoMarkup?

    PangoMarkup is a small markup language like html and it helps you avoid using "range of characters" while coloring or styling a piece a Text. You can use this language with ~.MarkupText.

    A simple example of a marked-up string might be

    <span foreground="blue" size="x-large">Blue text</span> is <i>cool</i>!"
    and it can be used with ~.MarkupText as

    .. manim:: MarkupExample :save_last_frame:
    """

    def __init__(self, *args, font=_FONT_NAME, font_size=15, **kwargs):
        super().__init__(*args, font=font, font_size=font_size, **kwargs)


class Question_Header(Text):
    """Question Header
    Args:
        question_no (int): Question Number
    """

    def __init__(
        self,
        question_no,
        font=_FONT_NAME,
        font_size=30,
        color=RED,
        weight=BOLD,
        **kwargs,
    ):

        super().__init__(
            "प्रश्‍न {}:".format(question_no),
            font=font,
            font_size=font_size,
            color=color,
            weight=weight,
            **kwargs,
        )


class Solution_Header(Text):
    """Question Header
    Args:
        ans (bool): Default True is 'उत्तर' and False is 'हल'

    """

    def __init__(
        self,
        ans=True,
        font=_FONT_NAME,
        font_size=25,
        color=GREEN,
        weight=BOLD,
        **kwargs,
    ):

        super().__init__(
            "उत्तर :" if ans else "हल :",
            font=font,
            font_size=font_size,
            color=color,
            weight=weight,
            **kwargs,
        )


class Cancel(VGroup):
    r"""

    Cancel is `\cancel` same worked

    Args:
        mobject (Mobject): Manim Object

    """

    def __init__(
        self,
        mobject: Mobject | None = None,
        stroke_color: ParsableManimColor = RED,
        stroke_width: float = 2.0,
        scale_factor: float = 1.5,
        **kwargs,
    ) -> None:
        super().__init__(Line(UP + RIGHT, DOWN + LEFT), **kwargs)
        if mobject is not None:
            self.replace(mobject, stretch=True)
        self.scale(scale_factor)
        self.set_stroke(color=stroke_color, width=stroke_width)
