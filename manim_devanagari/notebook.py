import textwrap
from manim import *
from typing import Iterable, Sequence
from typing_extensions import Self, TypeAlias
from manim.typing import Vector3D
from manim.mobject.opengl.opengl_vectorized_mobject import OpenGLVMobject


def Footer(
    width=None,
    stroke_opacity=0,
    fill_color=WHITE,
    fill_opacity=1,
    z_index=1,
    height=0.8,
) -> Rectangle:
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
    def __init__(self, *tex_strings, align="l", **kwargs):
        self.align = align
        super().__init__(*tex_strings, **kwargs)


class MathTex(MathTex):
    def __init__(self, *tex_strings, align="l", **kwargs):
        self.align = align
        super().__init__(*tex_strings, **kwargs)


class MarkupText(MarkupText):
    def __init__(self, text: str, align="l", **kwargs):
        self.align = align
        super().__init__(text, **kwargs)


class Notebook(VMobject):
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


class QGroup(VMobject):
    def __init__(
        self,
        *vmobjects,
        question_no=0,
        lang="en",
        style={"font_size": 25, "color": GREEN_E, "weight": BOLD},
        **kwargs,
    ):
        super().__init__(**kwargs)
        vmobjects = [self.language(lang, question_no, **style), *vmobjects]
        self.add(*vmobjects)
        self.question_arrange(aligned_edge=LEFT)

    def language(self, lang, question_no=0, **style):
        text = {"hi": "प्रश्‍न"}.get(lang, "Question")
        if question_no:
            text = "{} {}:".format(text, question_no)
        else:
            text = f"{text} :"

        return Text(text, **style)

    def question_arrange(
        self,
        direction: Vector3D = DOWN,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
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


class AGroup(VMobject):
    def __init__(
        self,
        *vmobjects,
        solve=True,
        lang="en",
        style={"font_size": 25, "color": GREEN_E, "weight": BOLD},
        **kwargs,
    ):
        super().__init__(**kwargs)
        vmobjects = [self.language(lang, solve, **style), *vmobjects]

        self.add(*vmobjects)
        self.question_arrange(aligned_edge=LEFT)

    def language(self, lang, solve=False, **style):
        text = ""
        if solve:
            text = {"hi": "हल"}.get(lang, "Solution")
        else:
            text = {"hi": "उत्तर"}.get(lang, "Answer")

        return Text(f"{text} :", **style)

    def question_arrange(
        self,
        direction: Vector3D = DOWN,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
        center: bool = True,
        **kwargs,
    ) -> Self:
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
