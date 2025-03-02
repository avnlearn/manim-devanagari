from manim import *
from manim_devanagari.openmoji import OpenMoji


class Example_openmoji(Scene):
    def construct(self):
        example = OpenMoji("1F9B8-1F3FC-200D-2640-FE0F")
        self.play(DrawBorderThenFill(example))
        self.wait()


if __name__ == "__main__":
    scene = Example_openmoji()
    scene.render()
