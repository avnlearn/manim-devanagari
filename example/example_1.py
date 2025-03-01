from manim import *
from manim_devanagari.notebook import Notebook, cue_column, Question, Answer, Solution


class Example_Notebook(Scene):
    def construct(self):
        Text.set_default(font_size=10, font="Noto Sans")
        Paragraph.set_default(font_size=10, font="Noto Sans")
        MathTex.set_default(font_size=10)

        m = Notebook(
            cue_column("Question 1 :"),
            "What is motion?",
            cue_column("Answer :"),
            "Motion is the change in position of an object over time.",
            r"$$v = \dfrac{d}{t}$$",
            cue_column("Question 2 :"),
            "What is force?",
            cue_column("Answer :"),
            "Force is an interaction that causes an object to change its velocity, direction, or shape. It is a vector quantity, meaning it has both magnitude and direction.",
            r"$$F = m \cdot a$$",
            cue_column("Question 3 :"),
            "what is sound?",
            cue_column("Answer :"),
            "Sound is a form of energy that travels as vibrations through a medium, such as air, water, or solids, and is perceived by our ears as auditory sensations.",
            cue_column("Question 4 :"),
            "what is speed?",
            cue_column("Answer :"),
            "Speed is the distance traveled per unit of time. The formula for speed is:",
            r"$$\text{Speed} = \dfrac{\text{Distance}}{\text{Time}}$$",
            "where speed is measured in units such as meters per second (m/s) or kilometers per hour (km/h).",
        )

        self.add(m)


if __name__ == "__main__":
    scene = Example_Notebook()
    scene.render()
