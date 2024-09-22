
from manim import *

class Text_Example(Scene):
    def construct(self):
        t = Text("Hello World")
        print(t)

if __name__ == "__main__":
    render = Text_Example()
    render.render()