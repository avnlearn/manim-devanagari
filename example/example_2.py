from manim import *
from manim_devanagari.notebook import *


config.background_color = WHITE


class Example(Scene):
    def construct(self):
        Text.set_default(font_size=20, color=BLACK)
        Paragraph.set_default(font_size=20, color=BLACK)
        MathTex.set_default(font_size=20, color=BLACK)

        self.add(Footer(width=self.camera.frame_width))

        notebook = Notebook(
            Text("Question 1:"),
            Text("What is speed?", align="c"),
            AGroup(
                Paragraph(
                    "Speed is a measure of how quickly an object moves or how fast a process occurs. It is typically defined as the distance traveled per unit of time. The formula for speed is:",
                    wrap_width=50,
                ),
                MathTex(
                    r"\text{Speed} = \dfrac{\text{Distance}}{\text{Time}}", name="c"
                ),
                Paragraph(
                    "Speed can be expressed in various units, such as meters per second (m/s), kilometers per hour (km/h), or miles per hour (mph). In physics, speed is a scalar quantity, meaning it only has magnitude and no direction. When direction is considered, it is referred to as velocity."
                ),
            ),
        )

        self.play(Write(notebook))
        self.wait()


if __name__ == "__main__":
    pass
