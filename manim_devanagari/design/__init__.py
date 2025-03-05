from manim import *
from manim_devanagari import Deva_MathTex, Deva_Tex

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


class AvNLearnLogo(VGroup):
    def __init__(self, font_size=30, **kwargs):
        super().__init__(**kwargs)
        self.create_logo(font_size)

    def create_logo(self, font_size):

        avn_text = Deva_Tex(r"\textbf{AvN}", font_size=font_size, color=GREEN_D)

        learn_text = Deva_Tex("learn", font_size=font_size - 12, color=ORANGE)
        self.add(avn_text, learn_text)
        self.arrange(DOWN, buff=0.01)


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

        title = Deva_Tex(
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

        title = Deva_Tex(
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
        self.add(Deva_Tex(r"\textbf{Like}", font_size=font_size))
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
                Deva_Tex(r"\textbf{Subscribe}", font_size=font_size),
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
        self.add(Deva_Tex(r"\textbf{Comment}", font_size=font_size))
        self.add(
            Rectangle(
                color=BS381.BRILLIANT_GREEN,
                fill_opacity=1.0,
                stroke_width=0,
                width=0.02,
                height=0.3,
            )
        )
        self.add(Deva_Tex(r"\textbf{Share}", font_size=font_size))
        self.arrange(buff=MED_SMALL_BUFF)
        self.to_edge(direction, buff=buff)



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
        case "high_quality":
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
            Text.set_default(font_size=font_size - 5)
            MarkupText.set_default(font_size=font_size - 7)
            Tex.set_default(font_size=font_size)
            MathTex.set_default(font_size=font_size)
            return (font_size, header_font_size)
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
