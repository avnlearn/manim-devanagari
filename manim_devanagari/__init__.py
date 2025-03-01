import textwrap
from manim import *
from typing import Sequence

# Define a custom TexTemplate for Devanagari script
_Devanagari = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    documentclass="\\documentclass[preview]{standalone}",
    preamble="\\usepackage{fontspec}\n\\usepackage{polyglossia}\n\\usepackage{cancel}\n\\setmainlanguage{english}\n\\setotherlanguage{hindi}\\setmainfont[Script=Devanagari]{Noto Sans}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
)


def Footer(
    width: float = None,
    stroke_opacity: float = 0,
    fill_color: color = WHITE,
    fill_opacity: float = 1,
    z_index: int = 1,
    height: float = 0.8,
) -> Rectangle:
    """
    Creates a footer rectangle at the bottom of the screen.

    Args:
        width (float, optional): The width of the footer. Defaults to the frame height.
        stroke_opacity (float): The opacity of the stroke. Defaults to 0.
        fill_color (Color): The fill color of the footer. Defaults to WHITE.
        fill_opacity (float): The opacity of the fill. Defaults to 1.
        z_index (int): The z-index of the footer. Defaults to 1.
        height (float): The height of the footer. Defaults to 0.8.

    Returns:
        Rectangle: The footer rectangle object.

    Example:
        footer = Footer(width=10, fill_color=BLUE)
        self.add(footer)
    """
    footer = Rectangle(
        stroke_opacity=stroke_opacity,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        z_index=z_index,
        width=width if width else config.frame_height,
        height=height,
    )
    footer.to_edge(DOWN, buff=0.0)
    return footer


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
        super().__init__(*args, tex_template=_Devanagari, **kwargs)


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


class QuestionText(Text):
    """
    A class representing a question text with language support.

    Args:
        question_no (int): The question number.
        lang (str): The language for the question text. Defaults to "en".
        font_size (int): The font size of the text. Defaults to 25.
        color (Color): The color of the text. Defaults to RED_A.
        weight (str): The weight of the text. Defaults to BOLD.

    Example:
        question = QuestionText(1, lang="en")
        self.add(question)
    """

    def __init__(
        self,
        question_no: int,
        lang: str = "en",
        color=PURE_RED,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(
            text=self.language(lang, question_no),
            color=color,
            weight=weight,
            **kwargs,
        )

    def language(self, lang, question_no=0):
        """
        Returns the question text in the specified language.

        Args:
            lang (str): The language code.
            question_no (int): The question number.

        Returns:
            str: The formatted question text.
        """
        text = {"hi": "प्रश्‍न"}.get(lang, "Question")
        if question_no:
            text = "{} {} :".format(text, question_no)
        else:
            text = f"{text} :"

        return text


class Deva_QuestionText(QuestionText):
    def __init__(self, question_no: int, lang: str = "hi", **kwargs):
        super().__init__(question_no=question_no, lang=lang, **kwargs)


class AnswerText(Text):
    """
    A class representing an answer text with language support.

    Args:
        question_no (int): The question number.
        lang (str): The language for the answer text. Defaults to "en".
        font_size (int): The font size of the text. Defaults to 25.
        color (Color): The color of the text. Defaults to GREEN_E.
        weight (str): The weight of the text. Defaults to BOLD.

    Example:
        answer = AnswerText(lang="en")
        self.add(answer)
    """

    def __init__(
        self,
        lang="en",
        color=GREEN_E,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(
            self.language(lang),
            color=color,
            weight=weight,
            **kwargs,
        )

    def language(self, lang):
        """
        Returns the answer text in the specified language.

        Args:
            lang (str): The language code.

        Returns:
            str: The formatted answer text.
        """
        text = {"hi": "उत्तर"}.get(lang, "Answer")
        return f"{text} :"


class Deva_AnswerText(AnswerText):
    def __init__(self, lang: str = "hi", **kwargs):
        super().__init__(lang=lang, **kwargs)


class SolutionText(Text):
    """
    A class representing a solution text with language support.

    Args:
        lang (str): The language for the solution text. Defaults to "en".
        font_size (int): The font size of the text. Defaults to 25.
        color (Color): The color of the text. Defaults to GREEN_E.
        weight (str): The weight of the text. Defaults to BOLD.

    Example:
        solution = SolutionText(lang="en")
        self.add(solution)
    """

    def __init__(
        self,
        lang="en",
        color=GREEN_E,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(
            text=self.language(lang),
            color=color,
            weight=weight,
            **kwargs,
        )

    def language(self, lang):
        """
        Returns the solution text in the specified language.

        Args:
            lang (str): The language code.

        Returns:
            str: The formatted solution text.
        """
        text = {"hi": "हल"}.get(lang, "Solution")
        return f"{text} :"


class Deva_SolutionText(SolutionText):
    def __init__(self, lang: str = "hi", **kwargs):
        super().__init__(lang=lang, **kwargs)


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
        **kwargs,
    ) -> None:
        super().__init__(Line(UP + RIGHT, DOWN + LEFT), **kwargs)
        if mobject is not None:
            self.replace(mobject, stretch=True)
        self.scale(scale_factor)
        self.set_stroke(color=stroke_color, width=stroke_width)


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


def rand_color(id=0, scene: Scene = None):
    # [background_color, color, question_color, card_background, sub_card_background]
    colors = []

    match id:
        case "yt":
            config.background_color = WHITE
            Text.set_default(color=BLACK)
            SingleStringMathTex.set_default(color=BLACK)
            Tex.set_default(color=BLACK)
            MarkupText.set_default(color=BLACK)

            colors = [
                ManimColor("#16a34a"),
                ManimColor("#2563eb"),
                ManimColor("#4f46e5"),
                ManimColor("#84cc16"),
                ManimColor("#f97316"),
            ]
            if isinstance(scene, Scene):
                scene.camera.background_color = config.background_color

        case 0:
            colors = [
                DARKER_GREY,
                WHITE,
                PURE_RED,
                ManimColor("#052e16"),
                ManimColor("#f97316"),
            ]
        case 1:
            color = [
                WHITE,
                BLACK,
                ManimColor("#F9BF09"),
                ManimColor("#E43F49"),
                ManimColor("#2a013d"),
                ManimColor("#f97316"),
            ]
        case 2:
            color = [
                ManimColor.from_hex("#141c33"),
                ManimColor.from_hex("#eff5fa"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]
        case 3:
            color = [
                ManimColor.from_hex("#f1f1f1"),
                ManimColor.from_hex("#F9BF09"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]
        case 4:
            color = [
                ManimColor.from_hex("#f1f1f1"),
                ManimColor.from_hex("#F9BF09"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]

    return tuple(colors)


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


class AvNLearnLogo(VGroup):
    def __init__(self, font_size=30, **kwargs):
        super().__init__(**kwargs)
        self.create_logo(font_size)

    def create_logo(self, font_size):

        # Create the "AvN" part of the logo
        avn_text = m_deva.Deva_Tex(r"\textbf{AvN}", font_size=font_size, color=GREEN_D)

        # Create the "learn" part of the logo
        learn_text = m_deva.Deva_Tex("learn", font_size=font_size - 12, color=ORANGE)

        # Arrange the texts vertically
        self.add(avn_text, learn_text)
        self.arrange(DOWN, buff=0.01)

        # # Optional: Add a background rectangle
        # background = Rectangle(
        #     width=avn_text.width + 0.5,
        #     height=avn_text.height + learn_text.height + 0.5,
        #     color=WHITE,
        #     fill_opacity=0.5
        # )
        # self.add(background)
        # self.move_to(background.get_center())
        # self.add_to_back(background)  # Add background behind the text


class AvnBackground(RoundedRectangle):
    r"""A rectangle background a :class:`~.Mobject`

    Examples
    --------
    .. manim:: AvnBackgroundExample
        :save_last_frame:

        class SurroundingRectExample(Scene):
            def construct(self):
                title = Title("A Quote from Newton")
                quote = Text(
                    "If I have seen further than others, \n"
                    "it is by standing upon the shoulders of giants.",
                    color=BLUE,
                ).scale(0.75)
                box = AvnBackground(quote, color=YELLOW, buff=MED_LARGE_BUFF)

                t2 = Tex(r"Hello World").scale(1.5)
                box2 = AvnBackground(t2, corner_radius=0.2)
                mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
                self.add(title, mobjects)
    """

    def __init__(
        self,
        *mobjects: Mobject,
        color: ParsableManimColor | None = ManimColor("#14532d"),
        stroke_width: float = 0,
        stroke_opacity: float = 0,
        fill_opacity: float = 1.0,
        buff: float = SMALL_BUFF,
        corner_radius: float = 0.0,
        line_stroke_width: int = 3,
        **kwargs,
    ):
        from manim.mobject.mobject import Group

        if not all(isinstance(mob, Mobject) for mob in mobjects):
            raise TypeError(
                "Expected all inputs for parameter mobjects to be a Mobjects"
            )

        group = Group(*mobjects)
        super().__init__(
            color=color,
            stroke_width=stroke_width,
            stroke_opacity=stroke_opacity,
            fill_opacity=fill_opacity,
            width=config.frame_width,
            height=group.height + 2 * buff,
            corner_radius=corner_radius,
            **kwargs,
        )
        self.buff = buff
        self.match_y(group)
        self.add(
            Underline(
                self,
                buff=0,
                stroke_width=line_stroke_width,
                color=ManimColor("#dc2626"),
            )
        )


class TitleBackground(VGroup):
    def __init__(
        self,
        text: str,
        bold: bool = True,
        color: ParsableManimColor = WHITE,
        bg_color: list[ParsableManimColor] = [ORANGE, GREEN_E],
        line_color: ParsableManimColor = PURE_RED,
        font_size: int = 48,
        text_buff: float = MED_LARGE_BUFF,
        bg_buff: float = 0.0,
        buff: float = MED_SMALL_BUFF,
        corner_radius: float = 0.0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # Create the title text

        title = m_deva.Deva_Tex(
            r"\textbf{" + text + r"}" if bold else str(text),
            color=color,
            font_size=font_size,
        )

        # Create the background rectangle
        rect = RoundedRectangle(
            width=config.frame_width - bg_buff,  # Add some padding
            height=title.height + text_buff,  # Add some padding
            color=bg_color,
            stroke_opacity=0.0,
            fill_color=bg_color,
            fill_opacity=1.0,
            corner_radius=corner_radius,
        )

        # Position the rectangle behind the title
        rect.move_to(title.get_center())

        # Add the rectangle and title to the group
        self.add(
            rect,
            title,
            Underline(
                rect, color=line_color, buff=0.0, stroke_width=5, stroke_opacity=0.8
            ),
        )
        title.to_edge(LEFT, buff=LARGE_BUFF)


class SubtitleBackground(VGroup):
    def __init__(
        self,
        text: str,
        bold: bool = True,
        color: ParsableManimColor = WHITE,
        bg_color: list[ParsableManimColor] = [ORANGE, GREEN_E],
        font_size: int = 30,
        bg_buff: float = MED_LARGE_BUFF,
        buff: float = MED_SMALL_BUFF,
        corner_radius: float = 0.0,
        **kwargs,
    ):
        super().__init__(**kwargs)

        # Create the title text

        title = m_deva.Deva_Tex(
            r"\textbf{" + text + r"}" if bold else str(text),
            color=color,
            font_size=font_size,
        )

        # Create the background rectangle
        rect = RoundedRectangle(
            width=title.width + bg_buff,  # Add some padding
            height=title.height + bg_buff,  # Add some padding
            color=bg_color,
            stroke_opacity=0,
            fill_color=bg_color,
            fill_opacity=1.0,
            corner_radius=corner_radius,
        )

        # Position the rectangle behind the title
        rect.move_to(title.get_center())

        # Add the rectangle and title to the group
        self.add(
            rect,
            title,
            Underline(rect, color=GRAY, buff=0.0, stroke_width=5, stroke_opacity=0.5),
        )
        # title.to_edge(LEFT, buff=LARGE_BUFF)


class YouTube_Like_Subscribe_Comment(VGroup):
    def __init__(self, font_size=30, direction=DOWN, buff=LARGE_BUFF, **kwargs):
        super().__init__(**kwargs)
        self.like_subscribe_comment(font_size, direction, buff)

    def like_subscribe_comment(self, font_size, direction, buff):
        self.add(m_deva.Deva_Tex(r"\textbf{Like}", font_size=font_size))
        self.add(
            Rectangle(
                color=BS381.BRILLIANT_GREEN,
                fill_opacity=1.0,
                stroke_width=0,
                width=0.02,
                height=0.3,
            )
        )
        self.add(
            VGroup(
                RoundedRectangle(
                    color=PURE_RED,
                    fill_opacity=1.0,
                    width=0.9,
                    height=0.3,
                    corner_radius=0.05,
                    stroke_color=PURE_RED,
                ),
                m_deva.Deva_Tex(r"\textbf{Subscribe}", font_size=font_size),
            )
        )
        self.add(
            Rectangle(
                color=BS381.BRILLIANT_GREEN,
                fill_opacity=1.0,
                stroke_width=0,
                width=0.02,
                height=0.3,
            )
        )
        self.add(m_deva.Deva_Tex(r"\textbf{Comment}", font_size=font_size))
        self.add(
            Rectangle(
                color=BS381.BRILLIANT_GREEN,
                fill_opacity=1.0,
                stroke_width=0,
                width=0.02,
                height=0.3,
            )
        )
        self.add(m_deva.Deva_Tex(r"\textbf{Share}", font_size=font_size))
        self.arrange(buff=MED_SMALL_BUFF)
        self.to_edge(direction, buff=buff)
