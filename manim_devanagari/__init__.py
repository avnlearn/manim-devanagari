import textwrap
from manim import *
from typing import Sequence


noto_sans = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    preamble=r"""
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


class Themes(Scene):
    def set_theme(
        self,
        background_color=BLACK,
        font="sans-serif",
        font_size=DEFAULT_FONT_SIZE,
        set_footer=True,
        footer_color=WHITE,
    ):
        self.Footer = Footer(width=self.camera.frame_width, fill_color=footer_color)
        if set_footer:
            self.add(self.Footer)
        match str(background_color):
            case "#FFFFFF":
                self.camera.background_color = background_color
                _COLOR = BLACK
                Text.set_default(color=_COLOR)
                Paragraph.set_default(color=_COLOR)
                MarkupText.set_default(color=_COLOR)
                Tex.set_default(color=_COLOR)
                MathTex.set_default(color=_COLOR)
                Deva_Tex.set_default(color=_COLOR)
                Deva_MathTex.set_default(color=_COLOR)
                Deva_MarkupText.set_default(color=_COLOR)

        Text.set_default(font=font, font_size=font_size)
        Paragraph.set_default(font=font, font_size=font_size)
        MarkupText.set_default(font=font, font_size=font_size)
        Tex.set_default(font_size=font_size)
        MathTex.set_default(font_size=font_size)
        Deva_Tex.set_default(font_size=font_size)
        Deva_MathTex.set_default(font_size=font_size)
        Deva_MarkupText.set_default(font=font, font_size=font_size)


def video_font_size(key=config["quality"], font_size=20):
    match key:
        case "low_quality":
            font_size = 40
            Matrix.set_default(
                v_buff=0.5,
                h_buff=0.5,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
            MobjectMatrix.set_default(
                v_buff=0.6,
                h_buff=1.8,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
        case "fourk_quality":
            font_size = 30
            Matrix.set_default(
                v_buff=0.8,
                h_buff=0.7,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
            MobjectMatrix.set_default(
                v_buff=0.6,
                h_buff=1.8,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
            header_font_size = font_size + 10
            Text.set_default(font_size=font_size - 5, font="sans-serif")
            MarkupText.set_default(font_size=font_size - 7, font="sans-serif")
            Tex.set_default(font_size=font_size)
            MathTex.set_default(font_size=font_size)
            return (font_size, header_font_size)
        case None if config["pixel_height"] == 1920 and config["pixel_width"] == 1080:
            font_size = 20
            Matrix.set_default(
                v_buff=0.3,
                h_buff=0.5,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
            MobjectMatrix.set_default(
                v_buff=0.5,
                h_buff=0.9,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )

    header_font_size = font_size + 10
    Text.set_default(font_size=font_size, font="Noto Sans")
    MarkupText.set_default(font_size=font_size, font="Noto Sans")
    Tex.set_default(font_size=font_size)
    MathTex.set_default(font_size=font_size)

    return (font_size, header_font_size)
