from manim import *
from manim_devanagari import Deva_MathTex
from typing_extensions import Iterable

class MatrixDimension(VGroup):
    def __init__(
        self,
        _matrix: Matrix | Iterable,
        dimension: Tex | MathTex | Text = None,
        color: ParsableManimColor = WHITE,
        font_size: int = 20,
        m_bold: bool = False,
        n_bold: bool = False,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if not isinstance(_matrix, Matrix):
            _matrix = Matrix(_matrix)

        if not dimension:
            if isinstance(_matrix, Matrix):
                m = len(_matrix.get_columns()[0])

                n = len(_matrix.get_rows()[0])
            elif isinstance(_matrix, Iterable):
                m = len(_matrix[0])
                n = len(_matrix[0][0])

            dimension = Deva_MathTex(
                (r"\textbf" if m_bold else r"\text") + r"{" + str(m) + "}",
                r"\times",
                (r"\textbf" if n_bold else r"\text") + r"{" + str(n) + "}",
                font_size=font_size,
            )

        dimension.next_to(_matrix, RIGHT, buff=0.08, aligned_edge=DOWN)
        # Add the rectangle and title to the group
        self.add(_matrix, dimension)
