from manim import *

__version__ = "1.0"
devanagari = TexTemplate(
    tex_compiler="xelatex",
    output_format=".xdv",
    documentclass="\\documentclass[preview]{standalone}",
    preamble="\\usepackage{fontspec}\n\\usepackage{polyglossia}\n\\usepackage{cancel}\n\\setmainlanguage{english}\n\\setotherlanguage{hindi}\\setmainfont[Script=Devanagari]{Noto Sans}\n\\usepackage{amsmath}\n\\usepackage{amssymb}",
)

_FONT_NAME = "sans-serif"
# _FONT_NAME="Noto Sans"


class Deva_Tex(Tex):
    def __init__(self, *args, font_size=20, **kwargs):
        super().__init__(*args, tex_template=devanagari, font_size=font_size, **kwargs)


class Deva_MathTex(MathTex):
    def __init__(self, *args, font_size=20, **kwargs):
        super().__init__(*args, tex_template=devanagari, font_size=font_size, **kwargs)


class Deva_Text(Text):
    def __init__(self, *args, font=_FONT_NAME, font_size=16, **kwargs):
        super().__init__(*args, font=font, font_size=font_size, **kwargs)


class Deva_MarkupText(MarkupText):
    def __init__(self, *args, font=_FONT_NAME, font_size=15, **kwargs):
        super().__init__(*args, font=font, font_size=font_size, **kwargs)


class Question_Header(Text):
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


class Footer(Rectangle):
    def __init__(
        height=0.8,
        stroke_opacity: float = 0,
        fill_color=GREEN,
        fill_opacity=1,
        z_index=1,
        **kwargs,
    ):
        super().__init__(
            stroke_opacity=stroke_opacity,
            fill_color=fill_color,
            fill_opacity=fill_opacity,
            z_index=z_index,
            **kwargs,
        )
