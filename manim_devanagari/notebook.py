import textwrap
from manim import *
from typing import Iterable, Sequence
from typing_extensions import Self, TypeAlias
from manim.typing import Vector3D
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject

"""
This module provides custom Manim classes for creating structured text elements,
footers, and organized groups of questions and answers for educational content.
"""

def Footer(
    width=None,
    stroke_opacity=0,
    fill_color=WHITE,
    fill_opacity=1,
    z_index=1,
    height=0.8,
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
        direction_align: str | None = None,
        *args,
        **kwargs,
    ):
        self.align = align
        self.direction_align = direction_align
        super().__init__(text, **kwargs)


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
        wrap_width: int = 50,
        align: str = "l",
        direction_align: str | None = None,
        **kwargs,
    ):
        self.wrap = wrap
        self.wrap_width = wrap_width
        self.direction_align = direction_align
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


class Tex(Tex):
    """
    Custom Tex class that allows for alignment options.

    Args:
        tex_strings (str): The LaTeX strings to display.
        align (str): The alignment of the text. Defaults to "l" (left).
    """
    def __init__(self, *tex_strings, align="l", **kwargs):
        self.align = align
        super().__init__(*tex_strings, **kwargs)


class MathTex(MathTex):
    """
    Custom MathTex class that allows for alignment options.

    Args:
        tex_strings (str): The LaTeX strings to display.
        align (str): The alignment of the text. Defaults to "l" (left).
    """
    def __init__(self, *tex_strings, align="l", **kwargs):
        self.align = align
        super().__init__(*tex_strings, **kwargs)


class MarkupText(MarkupText):
    """
    Custom MarkupText class that allows for alignment options.

    Args:
        text (str): The text to display.
        align (str): The alignment of the text. Defaults to "l" (left).
    """
    def __init__(self, text: str, align="l", **kwargs):
        self.align = align
        super().__init__(text, **kwargs)


class Notebook(VMobject):
    """
    A class representing a notebook that arranges its contents.

    Args:
        vmobjects (VMobject): The VMobjects to add to the notebook.
    """
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(**kwargs)
        self.add(*vmobjects)
        self.notebook_arrange(aligned_edge=LEFT)
        self.to_corner(UL, buff=0.25)

    def notebook_arrange(
        self,
        direction: Vector3D = DOWN,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
        """
        Arranges the notebook's contents in a specified direction.

        Args:
            direction (Vector3D): The direction to arrange the contents. Defaults to DOWN.
            buff (float): The buffer space between objects. Defaults to DEFAULT_MOBJECT_TO_MOBJECT_BUFFER.
            center (bool): Whether to center the notebook. Defaults to True.

        Returns:
            Self: The Notebook object itself.
        """
        for m1, m2 in zip(self.submobjects, self.submobjects[1:]):
            m2.next_to(m1, direction, buff, **kwargs)

            align = (m1.align if hasattr(m1, "align") else m1.name).lower()
            match align:
                case "cue_column" | "cue-column" | "cue":
                    m1.to_edge(LEFT, buff=5 + buff)
                case "r" | "right":
                    m1.to_edge(RIGHT, buff=-(5 - buff))
                case "c" | "center":
                    m1.set_x(buff + 5)

        if center:
            self.center()
        return self


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
        lang="en",
        font_size=25,
        color=RED_A,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(
            self.language(question_no, lang), color, font_size, weight, **kwargs
        )

    def language(self, lang, question_no=0, **style):
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
            text = "{} {}:".format(text, question_no)
        else:
            text = f"{text} :"

        return text


class QGroup(VMobject):
    """
    A class representing a group of questions.

    Args:
        vmobjects (VMobject): The VMobjects to add to the group.
        question_no (int): The question number.
        lang (str): The language for the question text. Defaults to "en".
        style (dict): The style for the question text. Defaults to a dictionary with font size, color, and weight.

    Example:
        q_group = QGroup(QuestionText(1), QuestionText(2), lang="en")
        self.add(q_group)
    """
    def __init__(
        self,
        *vmobjects,
        question_no=0,
        lang="en",
        style={"font_size": 25, "color": RED_A, "weight": BOLD},
        **kwargs,
    ):
        super().__init__(**kwargs)
        vmobjects = [QuestionText(question_no, lang, **style), *vmobjects]
        self.add(*vmobjects)
        self.question_arrange(aligned_edge=LEFT)

    def question_arrange(
        self,
        direction: Vector3D = DOWN,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
        """
        Arranges the questions in the group.

        Args:
            direction (Vector3D): The direction to arrange the questions. Defaults to DOWN.
            buff (float): The buffer space between objects. Defaults to DEFAULT_MOBJECT_TO_MOBJECT_BUFFER.
            center (bool): Whether to center the group. Defaults to True.

        Returns:
            Self: The QGroup object itself.
        """
        self.submobjects[1].next_to(self.submobjects[0], RIGHT, buff, aligned_edge=UP)

        for m1, m2 in zip(self.submobjects[1:], self.submobjects[2:]):
            m2.next_to(m1, direction, buff, **kwargs)
            align = (m1.align if hasattr(m1, "align") else m1.name).lower()
            match align:
                case "cue_column" | "cue-column" | "cue":
                    m1.to_edge(LEFT, buff=5 + buff)
                case "r" | "right":
                    m1.to_edge(RIGHT, buff=-(5 - buff))
                case "c" | "center":
                    m1.set_x(buff + 5)

        if center:
            self.center()
        return self


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
        answer = AnswerText(1, lang="en")
        self.add(answer)
    """
    def __init__(
        self,
        question_no: int,
        lang="en",
        font_size=25,
        color=GREEN_E,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(self.language(lang), color, font_size, weight, **kwargs)

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
        font_size=25,
        color=GREEN_E,
        weight=BOLD,
        **kwargs,
    ):
        super().__init__(self.language(lang), color, font_size, weight, **kwargs)

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


class AGroup(VMobject):
    """
    A class representing a group of answers.

    Args:
        vmobjects (VMobject): The VMobjects to add to the group.
        solve (bool): Whether to include a solution text. Defaults to True.
        lang (str): The language for the solution text. Defaults to "en".
        style (dict): The style for the solution text. Defaults to a dictionary with font size, color, and weight.

    Example:
        a_group = AGroup(AnswerText(1), AnswerText(2), lang="en")
        self.add(a_group)
    """
    def __init__(
        self,
        *vmobjects,
        solve=True,
        lang="en",
        style={"font_size": 25, "color": GREEN_E, "weight": BOLD},
        **kwargs,
    ):
        super().__init__(**kwargs)
        vmobjects = [
            SolutionText(lang, **style) if solve else SolutionText(lang, **style),
            *vmobjects,
        ]

        self.add(*vmobjects)
        self.question_arrange(aligned_edge=LEFT)

    def question_arrange(
        self,
        direction: Vector3D = DOWN,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
        """
        Arranges the answers in the group.

        Args:
            direction (Vector3D): The direction to arrange the answers. Defaults to DOWN.
            buff (float): The buffer space between objects. Defaults to DEFAULT_MOBJECT_TO_MOBJECT_BUFFER.
            center (bool): Whether to center the group. Defaults to True.

        Returns:
            Self: The AGroup object itself.
        """
        self.submobjects[1].next_to(self.submobjects[0], RIGHT, buff, aligned_edge=UP)

        for m1, m2 in zip(self.submobjects[1:], self.submobjects[2:]):
            m2.next_to(m1, direction, buff, **kwargs)

            align = (m1.align if hasattr(m1, "align") else m1.name).lower()
            match align:
                case "cue_column" | "cue-column" | "cue":
                    m1.to_edge(LEFT, buff=5 + buff)
                case "r" | "right":
                    m1.to_edge(RIGHT, buff=-(5 - buff))
                case "c" | "center":
                    m1.set_x(buff + 5)

        if center:
            self.center()
        return self
