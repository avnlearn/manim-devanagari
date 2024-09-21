import textwrap
from manim import *
from typing import Iterable, Sequence
from typing_extensions import Self, TypeAlias
from manim.typing import Vector3D
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject
from manim_devanagari.helper import (
    _str_to_mobject,
    SolutionText,
    AnswerText,
    QuestionText,
)


"""
This module provides custom Manim classes for creating structured text elements,
footers, and organized groups of questions and answers for educational content.
"""


class Notebook(VMobject):
    def __init__(self, *vmobjects, **kwargs):
        super().__init__(**kwargs)
        vmobjects = _str_to_mobject(*vmobjects)
        self.add(*vmobjects)
        self.arrange_notebook(DOWN, aligned_edge=LEFT)
        self.to_edge(UL)

    def arrange_notebook(
        self,
        direction: Vector3D = RIGHT,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
        cue_obj_stack = []
        math_display_mode = None
        for m1, m2 in zip(self.submobjects, self.submobjects[1:]):
            match type(m1).__name__:
                case "cue_column" | "Answer" | "Solution" | "Question":
                    m2.next_to(m1, RIGHT, buff, aligned_edge=UP)
                    cue_obj_stack.append(m1)
                case _:
                    m2.next_to(m1, direction, buff, **kwargs)
                    match type(m2).__name__:
                        case "cue_column" | "Answer" | "Solution" | "Question" if len(
                            cue_obj_stack
                        ):
                            m2.match_x(cue_obj_stack.pop(), RIGHT)

            match type(m1).__name__:
                case (
                    "MathTex"
                    | "MathTex_Display"
                    | "Deva_MathTex"
                    | "Deva_MathTex_Display"
                ):
                    if math_display_mode:
                        m1.match_x(math_display_mode)
                    else:
                        m1.to_edge(ORIGIN + RIGHT - LEFT)
                        math_display_mode = m1

        del cue_obj_stack
        del math_display_mode
        if center:
            self.center()
        return self


class cue_column_Text(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class cue_column_Paragraph(Paragraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class cue_column_MarkupText(MarkupText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class cue_column_Tex(Tex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class cue_column_MathTex(MathTex):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class cue_column(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Question(QuestionText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Answer(AnswerText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Solution(SolutionText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
