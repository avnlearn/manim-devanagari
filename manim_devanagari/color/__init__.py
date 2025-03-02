from manim import *


def rand_color(id=0, scene: Scene = None):
    # [background_color, color, question_color, card_background, sub_card_background]
    colors = []

    match id:
        case "yt":
            config.background_color = WHITE
            Text.set_default(color=BLACK)
            SingleStringMathTex.set_default(color=BLACK)
            Tex.set_default(color=BLACK)
            MarkupText.set_default(color=BLACK)

            colors = [
                ManimColor("#16a34a"),
                ManimColor("#2563eb"),
                ManimColor("#4f46e5"),
                ManimColor("#84cc16"),
                ManimColor("#f97316"),
            ]
            if isinstance(scene, Scene):
                scene.camera.background_color = config.background_color

        case 0:
            colors = [
                DARKER_GREY,
                WHITE,
                PURE_RED,
                ManimColor("#052e16"),
                ManimColor("#f97316"),
            ]
        case 1:
            color = [
                WHITE,
                BLACK,
                ManimColor("#F9BF09"),
                ManimColor("#E43F49"),
                ManimColor("#2a013d"),
                ManimColor("#f97316"),
            ]
        case 2:
            color = [
                ManimColor.from_hex("#141c33"),
                ManimColor.from_hex("#eff5fa"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]
        case 3:
            color = [
                ManimColor.from_hex("#f1f1f1"),
                ManimColor.from_hex("#F9BF09"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]
        case 4:
            color = [
                ManimColor.from_hex("#f1f1f1"),
                ManimColor.from_hex("#F9BF09"),
                ManimColor.from_hex("#E43F49"),
                ManimColor.from_hex("#2a013d"),
                ManimColor.from_hex("#f97316"),
            ]

    return tuple(colors)
