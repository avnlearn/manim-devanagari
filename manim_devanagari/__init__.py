import textwrap
from manim import *
from typing import Sequence, Iterator, Iterable

r"""
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{english}
\setotherlanguage{hindi}
\setmainfont[Script=Devanagari]{Noto Sans}
\usepackage{cancel}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{dsfont}
\usepackage{setspace}
\usepackage{tipa}
\usepackage{relsize}
\usepackage{textcomp}
\usepackage{mathrsfs}
\usepackage{calligra}
\usepackage{wasysym}
\usepackage{ragged2e}
\usepackage{physics}
\usepackage{xcolor}
\usepackage{microtype}
"""
noto_sans = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble=r"""
    \usepackage{fontspec}
    \usepackage{polyglossia}
    \usepackage{cancel}
    \setmainlanguage{english}
    \setotherlanguage{hindi}
    \setmainfont[Script=Devanagari]{Noto Sans}
    \usepackage{cancel}
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage{dsfont}
    \usepackage{setspace}
    \usepackage{tipa}
    \usepackage{relsize}
    \usepackage{textcomp}
    \usepackage{mathrsfs}
    \usepackage{calligra}
    \usepackage{wasysym}
    \usepackage{ragged2e}
    \usepackage{physics}
    \usepackage{xcolor}
    \usepackage{microtype}
    """,
)
_devanagari = noto_sans
# Define a custom TexTemplate for Devanagari script
# _Devanagari = TexTemplate(
#     _body='',
#     tex_compiler="xelatex",
#     output_format=".xdv",
#     documentclass="\\documentclass[preview]{standalone}",
#     preamble="\\usepackage{fontspec}\n\\usepackage{polyglossia}\n\\usepackage{cancel}\n\\setmainlanguage{english}\n\\setotherlanguage{hindi}\\setmainfont[Script=Devanagari]{Noto Sans}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
# )


class Paragraph(Paragraph):
    """
    Custom Paragraph class that wraps text and allows for alignment.

    Args:
        text (Sequence[str]): The text to display as a sequence of strings.
        wrap (bool): Whether to wrap the text. Defaults to True.
        wrap_width (int): The width for wrapping text. Defaults to 50.
        align (str): The alignment of the text. Defaults to "l" (left).
        direction_align (str | None): Optional direction alignment. Defaults to None.
    """

    def __init__(
        self,
        *text: Sequence[str],
        wrap: bool = True,
        wrap_width: int = config.pixel_width,
        align: str = "l",
        **kwargs,
    ):
        self.wrap = wrap
        self.wrap_width = wrap_width
        self.align = kwargs.get("alignment", align)
        self.original_text = map(self.wrap_text, text)
        super().__init__(
            *self.original_text,
            **kwargs,
        )

    def wrap_text(self, text: str) -> str:
        """
        Wraps and justifies the given text based on the specified alignment.

        Args:
            text (str): The text to wrap and justify.

        Returns:
            str: The wrapped and justified text.
        """
        wrapped_text = textwrap.fill(text, width=self.wrap_width)
        # Justify lines based on alignment using match-case
        match self.align:
            case "r" | "right":
                justify_func = str.rjust
            case "c" | "center":
                justify_func = str.center
            case "l" | "left":  # Support for both 'l' and 'left'
                justify_func = str.ljust
            case _:
                justify_func = str.ljust  # Default to left justify
        # Default to left justify
        return "\n".join(
            justify_func(line, self.wrap_width) for line in wrapped_text.splitlines()
        )


class Text(Text):
    """
    Custom Text class that allows for alignment options.

    Args:
        text (str): The text to display.
        align (str): The alignment of the text. Defaults to "l" (left).
        direction_align (str | None): Optional direction alignment. Defaults to None.
    """

    def __init__(
        self,
        text: str,
        align: str = "l",
        **kwargs,
    ):
        self.align = align
        super().__init__(text=text, **kwargs)


class MarkupText(MarkupText):
    """
    Custom MarkupText class that allows for alignment options.

    Args:
        text (str): The text to display.
        align (str): The alignment of the text. Defaults to "l" (left).
        direction_align (str | None): Optional direction alignment. Defaults to None.
    """

    def __init__(
        self,
        text: str,
        align: str = "l",
        **kwargs,
    ):
        self.align = align
        super().__init__(text, **kwargs)


class Tex(Tex):
    """
    Custom Tex class that allows for alignment options.

    Args:
        tex_strings (str): The LaTeX strings to display.
        align (str): The alignment of the text. Defaults to "l" (left).
        direction_align (str | None): Optional direction alignment. Defaults to None.
    """

    def __init__(
        self,
        *tex_strings,
        align: str = "l",
        tex_environment="flushleft",
        **kwargs,
    ):
        self.align = align
        super().__init__(*tex_strings, tex_environment=tex_environment, **kwargs)


class MathTex(MathTex):
    """
    Custom MathTex class that allows for alignment options.

    Args:
        tex_strings (str): The LaTeX strings to display.
        align (str): The alignment of the text. Defaults to "l" (left).
        direction_align (str | None): Optional direction alignment. Defaults to None.
    """

    def __init__(self, *tex_strings, align: str = "l", **kwargs):

        self.align = align
        super().__init__(*tex_strings, **kwargs)


class MathTex_Display(MathTex):
    def __init__(self, *tex_strings, **kwargs):
        super().__init__(*tex_strings, **kwargs)


class Deva_Tex(Tex):
    """Custom Tex class for rendering Devanagari text.

    Args:
        *args: Positional arguments for the Tex class.
        **kwargs: Additional keyword arguments for the Tex class.

    Returns:
        None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, tex_template=_devanagari, **kwargs)


class Deva_MathTex(MathTex):
    """Custom MathTex class for rendering Devanagari mathematical expressions.

    Args:
        *args: Positional arguments for the MathTex class.
        **kwargs: Additional keyword arguments for the MathTex class.

    Returns:
        None
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, tex_template=_devanagari, **kwargs)


class Deva_Matrix(Matrix):
    def __init__(self, matrix: Iterable, **kwarges):
        super().__init__(matrix, element_to_mobject=Deva_MathTex, **kwarges)


class Deva_MathTex_Display(Deva_MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Deva_Text(Text):
    """Custom Text class for rendering Devanagari text.

    Args:
        *args: Positional arguments for the Text class.
        **kwargs: Additional keyword arguments for the Text class.

    Returns:
        None
    """

    def __init__(self, text: str, font="Noto Sans", **kwargs):
        super().__init__(text, font=font, **kwargs)


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

    def __init__(self, text: str, font="Noto Sans", **kwargs):
        super().__init__(text, font=font, **kwargs)


class Deva_Paragraph(Paragraph):
    def __init__(self, *text: Sequence[str], font="Noto Sans", **kwargs):
        super().__init__(*text, font=font, **kwargs)


class BoldTex(Tex):
    def __init__(self, *tex_strings, **kwargs):
        self.tex_string_original = " ".join(tex_strings)
        tex_strings = self.set_bold(*tex_strings)
        super().__init__(*tex_strings, **kwargs)

    def set_bold(self, *tex_strings):
        tex_strings = list(tex_strings)
        tex_strings[0] = r"\textbf{" + tex_strings[0]
        tex_strings[-1] = tex_strings[-1] + r"}"
        return tuple(tex_strings)


class BoldMath(MathTex):
    def __init__(self, *tex_strings, **kwargs):

        self.tex_string_original = " ".join(tex_strings)
        tex_strings = self.set_bold(*tex_strings)
        super().__init__(*tex_strings, **kwargs)

    def set_bold(self, *tex_strings):
        tex_strings = list(tex_strings)
        tex_strings[0] = r"\mathbf{" + tex_strings[0]
        tex_strings[-1] = tex_strings[-1] + r"}"
        return tuple(tex_strings)
