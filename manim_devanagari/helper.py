import re
from manim import *
import manimpango
import functools
from typing import Sequence
from manim_devanagari import (
    Text,
    Paragraph,
    MarkupText,
    Tex,
    MathTex,
    MathTex_Display,
    QuestionText,
    SolutionText,
    AnswerText,
    Deva_Text,
    Deva_MarkupText,
    Deva_Paragraph,
    Deva_Tex,
    Deva_MathTex,
    Deva_MathTex_Display,
    Deva_QuestionText,
    Deva_AnswerText,
    Deva_SolutionText,
)

# @functools.lru_cache(maxsize=None)


def font_list() -> list[str]:
    return manimpango.list_fonts()


def check_font(self, font: str, tuple_value=False) -> bool:
    fonts_list = font_list()
    font_variants = [font, font.lower(), font.capitalize(), font.title()]

    if font.lower() == "sans-serif":
        font = "sans"

    for variant in font_variants:
        if variant in fonts_list:
            return (variant, True) if tuple_value else True

    logger.warning(f"Font {font} not in {fonts_list}.")
    return (font, False) if tuple_value else False


def check_default_font(self, font: str) -> str:
    fonts = [
        font,
        "Lohit Devanagari",
        "Arial Unicode MS",
        "Noto Sans Devanagari",
        "Mangal",
        "Devanagari New",
        "Nirmala UI",
        "Hind",
    ]
    for f in fonts:
        f, check_font = check_font(f, tuple_value=True)
        if check_font:
            return f

    logger.error(f"Font {font} is not font")


def is_hindi(text: str) -> bool:
    """
    Check if the text contains Hindi characters.

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text contains Hindi characters, False otherwise.
    """
    return any("\u0900" <= char <= "\u097F" for char in text if char.isalpha())


def is_english(text: str) -> bool:
    """
    Check if the text contains only English characters.

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text contains only English alphabetic characters and spaces, False otherwise.
    """
    return all(char.isalpha() or char.isspace() for char in text)


def contains_inline_math(markdown_text):
    # Initialize a counter for dollar signs
    dollar_count = 0
    i = 0

    while i < len(markdown_text):
        # Check for escaped dollar sign
        if markdown_text[i : i + 2] == r"\$":
            i += 2  # Skip the escaped dollar sign
            continue

        # Count dollar signs
        if markdown_text[i] == "$":
            dollar_count += 1

        i += 1

    # Return True if there are an even number of unescaped dollar signs
    return dollar_count % 2 == 0 and dollar_count > 0


def is_latex(text: str) -> bool:
    """
    Check if the text contains LaTeX commands.

    Args:
        text (str): The input text to check.

    Returns:
        bool: True if the text contains LaTeX commands, False otherwise.
    """
    latex_pattern = r"\\[a-zA-Z]+"
    return bool(re.search(latex_pattern, text))


def is_math_mode_inline(text: str) -> bool:
    return text.startswith("$") and text.endswith("$")


def is_math_mode_display(text: str) -> bool:
    return text.startswith("$$") and text.endswith("$$")


def is_html(text):
    # Check if the text contains any HTML-like tags
    if "<" in text and ">" in text:
        # A simple check for well-formedness
        return is_well_formed(text)
    return False


def is_well_formed(html):
    stack = []
    tag = ""
    in_tag = False

    # Remove backslashes for checking
    html = html.replace("\\", "")  # Remove backslashes

    for char in html:
        if char == "<":
            if tag:  # If we were already in a tag, it's malformed
                return False
            in_tag = True
            tag = ""
        elif char == ">":
            if not in_tag:  # If we weren't in a tag, it's malformed
                return False
            in_tag = False
            if tag.startswith("/"):  # Closing tag
                if not stack or stack[-1] != tag[1:]:
                    return False
                stack.pop()
            else:  # Opening tag
                stack.append(tag)
            tag = ""
        elif in_tag:
            tag += char

    return len(stack) == 0  # Stack should be empty if well-formed


def _str_to_mobject_convert(text: str) -> VMobject:
    text_line = config.pixel_width
    if isinstance(text, str):
        is_latex_str = is_latex(text)
        is_str_inline_math = contains_inline_math(text)
        is_hindi_str = is_hindi(text)
        is_math_mode_display_str = is_math_mode_display(text)
        is_markuptext = is_html(text)
        if is_hindi_str:
            if is_math_mode_display_str:
                return Deva_MathTex_Display(text[2:-2].strip())
            elif is_latex_str or is_str_inline_math:
                if is_math_mode_inline(text):
                    return Deva_Tex(text[1:-1].strip())
                return Deva_Tex(text)
            elif is_markuptext:
                return Deva_MarkupText(text)
            else:
                if len(text) <= text_line:
                    return Deva_Text(text)
                return Deva_Paragraph(text)
        else:
            if is_math_mode_display_str:
                return MathTex_Display(text[2:-2].strip())
            elif is_latex_str or is_str_inline_math:
                if is_math_mode_inline(text):
                    return Deva_Tex(text[1:-1].strip())
                return Tex(text)
            elif is_markuptext:
                return MarkupText(text)
            else:
                if len(text) <= text_line:
                    return Text(text)
                return Paragraph(text)

    elif isinstance(text, tuple):
        str_lst = " ".join(text)
        is_latex_str = is_latex(str_lst)
        is_str_inline_math = contains_inline_math(str_lst)
        is_hindi_str = is_hindi(str_lst)
        is_math_mode_display_str = is_math_mode_display(str_lst)
        is_markuptext = is_html(str_lst)
        if is_hindi_str:
            if is_math_mode_display_str:
                return Deva_MathTex_Display(*text[1:-1])
            elif is_latex_str or is_str_inline_math:
                if is_math_mode_inline(str_lst):
                    return Deva_Tex(text[1:-1])
                return Deva_Tex(*text)
            elif is_markuptext:
                return Deva_MarkupText(str_lst)
            else:
                if len(text) > text_line:
                    return Deva_Text(str_lst)
                return Deva_Paragraph(*text)
        else:
            if is_math_mode_display_str:
                return MathTex_Display(*text[1:-1])
            elif is_latex_str or is_str_inline_math:
                if is_math_mode_inline(str_lst):
                    return Deva_Tex(text[1:-1])
                return Tex(*text)
            elif is_markuptext:
                return MarkupText(str_lst)
            else:
                if len(text) > text_line:
                    return Text(str_lst)
                return Paragraph(*text)
    return text


def _str_to_mobject(*vmobjects: VMobject) -> Sequence[VMobject]:
    return tuple(_str_to_mobject_convert(vmobject) for vmobject in vmobjects)


def mobject_to_text(mobject: Mobject) -> str():
    # Tex() or MathTex()
    match type(mobject).__name__:
        case "VGroup":
            m_str = []
            for m in mobject:
                m = mobject_to_text(m)
                if m:
                    m_str.append(m)
            return "\n".join(m_str)
        # Tex
        case "Deva_Tex" | "Tex":
            return mobject.get_tex_string()
        # Text
        case "Deva_Text" | "Text":
            return mobject.original_text
        # Paragraph
        case "Deva_Paragraph" | "Paragraph":
            return mobject.lines_text.original_text
        # MarkupText
        case "Deva_MarkupText" | "MarkupText":
            return mobject.lines_text.original_text
        case _:
            return str(mobject)


def mobject_str(*vmobjects, space=False, **kwargs):
    vmobjects = [mobject_to_text(vmobject) for vmobject in vmobjects]
    return (" " if space else "\n").join(vmobjects)


if __name__ == "__main__":
    # Example usage
    text_samples = [
        "नमस्ते, आप कैसे हैं?",  # Hindi
        "Hello, how are you?",  # English
        r"This is a LaTeX document: \textbf{Bold Text}",  # LaTeX
        "नमस्ते, Hello!",  # Mixed (Hindi and English)
        # Mixed (Hindi, English, LaTeX)
        r"This is a LaTeX document with Hindi: \textbf{नमस्ते}",
    ]

    for sample in text_samples:
        print(f"'{sample}' is of type: {check_text_type(sample)}")
