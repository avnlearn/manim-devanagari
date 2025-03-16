from manim import *
from manim_devanagari import Deva_MathTex, Deva_Tex
from manim_devanagari.colors import GREEN_SCREEN, BLUE_SCREEN
from manim.typing import Vector2D, Vector3D

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
    def __init__(self, font_size=40, **kwargs):
        super().__init__(**kwargs)
        self.create_logo(font_size)

    def create_logo(self, font_size):

        self.avn_text = Deva_Tex(r"\textbf{AvN}", font_size=font_size, color=GREEN_C)
        
        self.learn_text = Deva_Tex("learn", font_size=font_size - 15, color=ORANGE)
        self.add(self.avn_text, self.learn_text)
        self.arrange(DOWN, buff=0.02)
    
    @override_animation(Create)
    def create(self, run_time:float=2):
        return AnimationGroup(
            AddTextLetterByLetter(self.avn_text, run_time=run_time),
            TransformFromCopy(self.avn_text, self.learn_text, run_time=run_time - 0.6),
            lag_ratio=0.1
        )

class MobjectBackground(VGroup):
    def __init__(
        self,
        *mobject: Mobject,
        bg_color: list[ParsableManimColor] = [ManimColor("#f97316"), ManimColor("#fb923c"), ManimColor("#16a34a"), ManimColor("#14532d")],
        bg_opacity: float = 1.0,
        bg_stroke_opacity: float = 0.0,
        bg_w_buff: float = MED_LARGE_BUFF,
        bg_h_buff: float = MED_LARGE_BUFF,
        underline_color: list[ParsableManimColor] = DARKER_GRAY,
        underline_width: float = 8,
        underline_opacity: float = 0.8,
        buff: float = 0,
        corner_radius: float = 0.0,
        bg_h: float = None,
        bg_w: float = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        mobject_g = Group(*mobject)
        bg_h = mobject_g.width if bg_h is None else bg_h
        bg_w = mobject_g.height if bg_w is None else bg_w
        
        rect = RoundedRectangle(
            width=bg_w + bg_w_buff,  # Add some padding
            height=bg_h + bg_h_buff,  # Add some padding
            stroke_opacity=bg_stroke_opacity,
            fill_color=bg_color,
            fill_opacity=bg_opacity,
            corner_radius=corner_radius,
        )
        rect.move_to(mobject_g.get_center())
        self.add(
            rect,
            *mobject,
            
        )
        if underline_color:
            self.add(Underline(rect, color=underline_color, buff=buff, stroke_width=underline_width, stroke_opacity=underline_opacity))
    
   

class AvnBackground(RoundedRectangle):
    def __init__(
        self,
        *mobjects: Mobject,
        color: ParsableManimColor = ManimColor("#14532d"),
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

class TitleBackground(MobjectBackground):
    def __init__(
        self, *tex: str, bold: bool = True, color: ParsableManimColor = WHITE,
        bg_color: list[ParsableManimColor] = [ManimColor("#d97706"), ManimColor("#4d7c0f")],
        underline_color: ParsableManimColor = YELLOW,
        font_size: int = 48,
        bg_buff: float = 0.0,
        text_buff: float = MED_LARGE_BUFF,
        corner_radius: float = 0.0,
        aligned_edge: Vector3D = LEFT,
        buff: float = LARGE_BUFF,
        **kwargs
    ):
        # Create the title text
        if bold:
            tex = [r"\textbf{" + i + r"}" for i in tex]

        title = Deva_Tex(
            *tex,
            color=color,
            font_size=font_size,
        )
        super().__init__(title, 
        bg_color=bg_color, 
        underline_color=underline_color, 
        underline_opacity=1.0,
        underline_width=6,
        bg_h_buff=text_buff, bg_w_buff=bg_buff, 
        corner_radius=corner_radius, 
        bg_h=title.height, 
        bg_w=config.frame_width,
        **kwargs)

        title.to_edge(aligned_edge, buff=buff)


class SubtitleBackground(MobjectBackground):
    def __init__(
        self,
        *tex: str,
        bold: bool = True,
        color: ParsableManimColor = DARKER_GRAY,
        bg_color: list[ParsableManimColor] = [ManimColor("#fde047"), ManimColor("#bef264")],
        font_size: int = 40,
        bg_buff: float = MED_LARGE_BUFF,
        buff: float = MED_SMALL_BUFF,
        corner_radius: float = 0.0,
        **kwargs,
    ):
        # Create the title text
        if bold:
            tex = [r"\textbf{" + i + r"}" for i in tex]

        title = Deva_Tex(
            *tex,
            color=color,
            font_size=font_size,
        )
        super().__init__(title, 
        bg_color=bg_color, 
        underline_color=None, 
        underline_opacity=1.0,
        underline_width=6,
        bg_h_buff=bg_buff, bg_w_buff=bg_buff + 2, 
        corner_radius=corner_radius, 
        bg_h=title.height, 
        bg_w=title.width, **kwargs)
        
        


class TexBackground(VGroup):
    def __init__(
        self,
        *tex: str,
        color: ParsableManimColor = WHITE,
        bg_color: list[ParsableManimColor] = [MAROON_E, TEAL_E],
        font_size: int = 40,
        buff: float = MED_LARGE_BUFF,
        corner_radius: float = 0.0,
        **kwargs,
    ):
        super().__init__(**kwargs)
        title = Deva_Tex(
            *tex,
            color=color,
            font_size=font_size,
        )

        # Create the background rectangle
        rect = RoundedRectangle(
            width=title.width + buff,  # Add some padding
            height=title.height + buff,  # Add some padding
            color=bg_color,
            stroke_opacity=0,
            fill_color=bg_color,
            fill_opacity=1.0,
            corner_radius=corner_radius,
        )
        bg_rect = Rectangle(
            width=rect.width + 0.1,
            height=0.5,  # Add some padding
            color=ManimColor("#1e293b"),
            stroke_opacity=0,
            fill_color=ManimColor("#1e293b"),
            fill_opacity=0.6,
            
        )

        # Position the rectangle behind the title
        rect.move_to(title.get_center())
        bg_rect.move_to(rect.get_left(), aligned_edge=UL)
        # bg_rect.next_to(rect.get_edge_center(DR), buff=SMALL_BUFF)

        # Add the rectangle and title to the group
        self.add(
            bg_rect,
            rect,
            title
        )
        





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

class Background(Rectangle):
    def __init__(self, buff:int=0, **kwarges):
        super().__init__(height=config.frame_height - buff, width=config.frame_width - buff, **kwarges)

class GREEN_Background(Background):
    def __init__(self,color=GREEN_SCREEN, **kwarges):
        super().__init__(color=color, fill_color=color, fill_opacity=1.0,**kwarges)

class BLUE_Background(Background):
    def __init__(self,color=BLUE_SCREEN, **kwarges):
        super().__init__(color=color, fill_color=color, fill_opacity=1.0, **kwarges)


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
        case "low_quality":
            font_size = 40
            Matrix.set_default(
                v_buff=0.8,
                h_buff=0.8,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
            MobjectMatrix.set_default(
                v_buff=0.8,
                h_buff=1.3,
                bracket_h_buff=SMALL_BUFF,
                bracket_v_buff=SMALL_BUFF,
            )
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
    Text.set_default(font_size=font_size - 5, font="sans-serif")
    MarkupText.set_default(font_size=font_size - 7, font="sans-serif")
    Tex.set_default(font_size=font_size)
    Title.set_default(font_size=font_size)
    MathTex.set_default(font_size=font_size)
    return (font_size, header_font_size)
