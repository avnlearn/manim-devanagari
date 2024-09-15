"""
manim_devanagari

This package provides custom classes and functions for rendering text and mathematical expressions
in the Devanagari script using the Manim animation engine. It extends the functionality of Manim
by allowing users to easily create animations that include Hindi text and mathematical notation.

Features:
- Custom Tex and MathTex classes for rendering LaTeX and mathematical expressions in Devanagari.
- Support for various text styles, including plain text, markup text, and answers.
- Grouping classes for organizing related text and solution elements.
- A cancel effect for visually striking annotations.

Usage:
To use this package, import the necessary classes and create instances as needed. For example:

    from manim_devanagari import Deva_Tex, Deva_MathTex, Solution

    # Create a Devanagari text object
    devanagari_text = Deva_Tex("नमस्ते")

    # Create a mathematical expression in Devanagari
    math_expression = Deva_MathTex(r"\frac{a}{b} = c")

    # Create a solution object
    solution = Solution("यह एक समाधान है।")

This package is designed to work with Manim and requires the appropriate setup for rendering
Devanagari text using XeLaTeX.

Author: Guddu Kumar
Version: 0.0.2
"""

from manim import *
from manim_devanagari.notebook import *


# Define a custom TexTemplate for Devanagari script
_Devanagari = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    documentclass="\\documentclass[preview]{standalone}",
    preamble="\\usepackage{fontspec}\n\\usepackage{polyglossia}\n\\usepackage{cancel}\n\\setmainlanguage{english}\n\\setotherlanguage{hindi}\\setmainfont[Script=Devanagari]{Noto Sans}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
)

# Font and color settings
_FONT_NAME = "sans-serif"
_SET_COLOR = BLACK
_SET_QUESTION_COLOR = RED
_SET_SOLUTION_COLOR = GREEN_E
_SET_FONT_SIZE = 35

_LIGHT_MODE = False
if _LIGHT_MODE:
    config.background_color = WHITE
    _SET_COLOR = WHITE

_SET_TEX_FONT_SIZE = _SET_FONT_SIZE - 5
_SET_TEXT_FONT_SIZE = _SET_TEX_FONT_SIZE - 4
_SET_MARKUPTEXT_FONT_SIZE = _SET_TEX_FONT_SIZE - 5


class Tex(Tex):
    """Custom Tex class for rendering LaTeX text with specified color and font size.

    Args:
        *args: Positional arguments for the Tex class.
        font_size (int): The font size for the rendered text. Default is _SET_TEX_FONT_SIZE.
        color (Color): The color of the text. Default is _SET_COLOR.
        **kwargs: Additional keyword arguments for the Tex class.

    Returns:
        None
    """

    def __init__(self, *args, font_size=_SET_TEX_FONT_SIZE, color=_SET_COLOR, **kwargs):
        super().__init__(*args, color=color, font_size=font_size, **kwargs)


class Deva_Tex(Tex):
    """Custom Tex class for rendering Devanagari text.

    Args:
        *args: Positional arguments for the Tex class.
        **kwargs: Additional keyword arguments for the Tex class.

    Returns:
        None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, tex_template=_Devanagari, **kwargs)


class MathTex(MathTex):
    """Custom MathTex class for rendering mathematical expressions with specified color and font size.

    Args:
        *args: Positional arguments for the MathTex class.
        font_size (int): The font size for the rendered math text. Default is _SET_TEX_FONT_SIZE.
        color (Color): The color of the math text. Default is _SET_COLOR.
        **kwargs: Additional keyword arguments for the MathTex class.

    Returns:
        None
    """

    def __init__(self, *args, font_size=_SET_TEX_FONT_SIZE, color=_SET_COLOR, **kwargs):
        super().__init__(*args, color=color, font_size=font_size, **kwargs)


class Deva_MathTex(MathTex):
    """Custom MathTex class for rendering Devanagari mathematical expressions.

    Args:
        *args: Positional arguments for the MathTex class.
        **kwargs: Additional keyword arguments for the MathTex class.

    Returns:
        None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, tex_template=_Devanagari, **kwargs)


class Text(Text):
    """Custom Text class for rendering plain text with specified color and font size.

    Args:
        *args: Positional arguments for the Text class.
        font_size (int): The font size for the rendered text. Default is _SET_TEXT_FONT_SIZE.
        color (Color): The color of the text. Default is _SET_COLOR.
        **kwargs: Additional keyword arguments for the Text class.

    Returns:
        None
    """

    def __init__(
        self, *args, font_size=_SET_TEXT_FONT_SIZE, color=_SET_COLOR, **kwargs
    ):
        super().__init__(*args, color=color, font_size=font_size, **kwargs)


class Deva_Text(Text):
    """Custom Text class for rendering Devanagari text.

    Args:
        *args: Positional arguments for the Text class.
        font (str): The font to be used for rendering. Default is _FONT_NAME.
        **kwargs: Additional keyword arguments for the Text class.

    Returns:
        None
    """

    def __init__(self, *args, font=_FONT_NAME, **kwargs):
        super().__init__(*args, font=font, **kwargs)


class Deva_MarkupText(MarkupText):
    """Custom MarkupText class for rendering Devanagari text with markup support.

    Args:
        *args: Positional arguments for the MarkupText class.
        color (Color): The color of the text. Default is _SET_COLOR.
        font_size (int): The font size for the rendered text. Default is _SET_MARKUPTEXT_FONT_SIZE.
        **kwargs: Additional keyword arguments for the MarkupText class.

    Returns:
        None
    """

    def __init__(
        self, *args, color=_SET_COLOR, font_size=_SET_MARKUPTEXT_FONT_SIZE, **kwargs
    ):
        super().__init__(*args, color=color, font_size=font_size, **kwargs)


class Question_Header(QuestionText):
    """Custom QuestionText class for rendering question headers.

    Args:
        question_no (str): The question number to be displayed.
        lang (str): The language code for the text. Default is "hi" (Hindi).
        font (str): The font to be used for rendering. Default is _FONT_NAME.
        font_size (int): The font size for the rendered text. Default is 30.
        color (Color): The color of the text. Default is _SET_QUESTION_COLOR.
        weight (str): The weight of the font (e.g., BOLD). Default is BOLD.
        **kwargs: Additional keyword arguments for the QuestionText class.

    Returns:
        None
    """

    def __init__(
        self,
        question_no,
        lang="hi",
        font=_FONT_NAME,
        font_size=30,
        color=_SET_QUESTION_COLOR,
        weight=BOLD,
        **kwargs
    ):
        super().__init__(
            question_no=question_no,
            font=font,
            font_size=font_size,
            color=color,
            weight=weight,
            **kwargs
        )


class Solution(SolutionText):
    """Custom SolutionText class for rendering solutions.

    Args:
        font (str): The font to be used for rendering. Default is _FONT_NAME.
        font_size (int): The font size for the rendered text. Default is 25.
        color (Color): The color of the text. Default is _SET_SOLUTION_COLOR.
        weight (str): The weight of the font (e.g., BOLD). Default is BOLD.
        **kwargs: Additional keyword arguments for the SolutionText class.

    Returns:
        None
    """

    def __init__(
        self,
        font=_FONT_NAME,
        font_size=25,
        color=_SET_SOLUTION_COLOR,
        weight=BOLD,
        **kwargs
    ):
        super().__init__(
            lang="hi",
            font=font,
            font_size=font_size,
            color=color,
            weight=weight,
            **kwargs
        )


class Solution_Group(AGroup):
    """Custom AGroup class for grouping solution elements.

    Args:
        *vmobjects: Variable number of mobjects to be grouped.
        **kwargs: Additional keyword arguments for the AGroup class.

    Returns:
        None
    """

    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, lang="hi", **kwargs)


class Answer(AnswerText):
    """Custom AnswerText class for rendering answers.

    Args:
        font (str): The font to be used for rendering. Default is _FONT_NAME.
        font_size (int): The font size for the rendered text. Default is 25.
        color (Color): The color of the text. Default is _SET_SOLUTION_COLOR.
        weight (str): The weight of the font (e.g., BOLD). Default is BOLD.
        **kwargs: Additional keyword arguments for the AnswerText class.

    Returns:
        None
    """

    def __init__(
        self,
        font=_FONT_NAME,
        font_size=25,
        color=_SET_SOLUTION_COLOR,
        weight=BOLD,
        **kwargs
    ):
        super().__init__(
            lang="hi",
            font=font,
            font_size=font_size,
            color=color,
            weight=weight,
            **kwargs
        )


class Answer_Group(AGroup):
    """Custom AGroup class for grouping answer elements.

    Args:
        *vmobjects: Variable number of mobjects to be grouped.
        **kwargs: Additional keyword arguments for the AGroup class.

    Returns:
        None
    """

    def __init__(self, *vmobjects, **kwargs):
        super().__init__(*vmobjects, lang="hi", **kwargs)


class Cancel(VGroup):
    """Custom VGroup class for creating a cancel effect on a given mobject.

    Args:
        mobject (Mobject | None): The mobject to be canceled. Default is None.
        stroke_color (Color): The color of the cancel line. Default is RED.
        stroke_width (float): The width of the cancel line. Default is 2.0.
        scale_factor (float): The scale factor for the cancel effect. Default is 1.5.
        **kwargs: Additional keyword arguments for the VGroup class.

    Returns:
        None
    """

    def __init__(
        self,
        mobject: Mobject | None = None,
        stroke_color: ParsableManimColor = RED,
        stroke_width: float = 2.0,
        scale_factor: float = 1.5,
        **kwargs
    ) -> None:
        super().__init__(Line(UP + RIGHT, DOWN + LEFT), **kwargs)
        if mobject is not None:
            self.replace(mobject, stretch=True)
        self.scale(scale_factor)
        self.set_stroke(color=stroke_color, width=stroke_width)


def Str_Join(*args: str, space=False, **kwargs):
    """Join strings with a specified separator (space or newline).

    Args:
        *args: Strings to be joined.
        space (bool): If True, join with a space; otherwise, join with a newline. Default is False.
        **kwargs: Additional keyword arguments (not used).

    Returns:
        str: The joined string.
    """
    args = [str(i) for i in args]
    return (" " if space else "\n").join(args)


def Bookmark(mark):
    """Create a bookmark in the format required for rendering.

    Args:
        mark (str): The mark to be used for the bookmark.

    Returns:
        str: The formatted bookmark string.
    """
    return "<bookmark mark='{}'/>".format(mark)
