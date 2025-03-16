from manim import *


AVN_COLOR_PROFILE = {
    "green_screen": PURE_GREEN,
    "blue_screen": PURE_BLUE,
    "light": {
        "background": WHITE,
        "color": BLACK,
        "primary": ManimColor("#166534"),
        "secondary": ManimColor("#9A3412"),
        "underline": ManimColor("#991B1B"),
        "bold": ManimColor("#4338CA"),
        "highlight": ManimColor("#92400E"),
        "link": ManimColor("#1E40AF"),
        "shape": ManimColor("#065F46"),
        "cancel": ManimColor("#3F6212"),
    },
    "dark": {
        "background": ManimColor("#181818"),
        "color": WHITE,
        "primary": ManimColor("#4ADE80"),
        "secondary": ManimColor("#FDBA74"),
        "underline": ManimColor("#EF4444"),
        "bold": ManimColor("#2DD4BF"),
        "highlight": ManimColor("#FACC15"),
        "link": ManimColor("#7DD3FC"),
        "shape": ManimColor("#34D399"),
        "cancel": ManimColor("#84CC16"),
    },
}
GREEN_SCREEN = AVN_COLOR_PROFILE["green_screen"]
BLUE_SCREEN = AVN_COLOR_PROFILE["blue_screen"]
DARK_THEME = AVN_COLOR_PROFILE["dark"]["background"]


def rand_color(
    id=0, scene: Scene = None, dark_theme: bool = False, chroma: bool = False
):

    colors = []

    match id:
        case "yt":
            colors = [
                AVN_COLOR_PROFILE["dark" if dark_theme else "light"][i]
                for i in AVN_COLOR_PROFILE.get("dark" if dark_theme else "light")
            ]
        case _:
            colors = [
                AVN_COLOR_PROFILE["dark" if dark_theme else "light"][i]
                for i in AVN_COLOR_PROFILE.get("dark" if dark_theme else "light")
            ]

    Text.set_default(color=colors[1])
    SingleStringMathTex.set_default(color=colors[1])
    Tex.set_default(color=colors[1])
    MarkupText.set_default(color=colors[1])
    Circle.set_default(color=colors[1])
    Line.set_default(color=colors[1])
    Mobject.set_default(color=colors[1])
    if isinstance(scene, Scene):
        config.background_color = colors[0]
        scene.camera.background_color = config.background_color
    return colors


if __name__ == "__main__":
    print(rand_color("yt"))
