# Manim Devangari

Manim plugin for adding devanagari script.

# Table of Contents:

- [Installation](#installation)
- [Usage Devanagari](#usage-devanagari)

# Installation

- Install `pip install manim`
- Install font - `Noto Sans` and `Noto Sans Devanagari`

# Usage Devanagari

## Devanagari Template

`manim_devanagari.devanagari` supported Hindi, English and Math

### Example :

```python
from manim import *
import manim_devanagari

class DevanagariTex(Scene):
    def construct(self):
        dev_tex = VGroup(
            Tex("धन्यावद", tex_template=manim_devanagari.devanagari),
            Tex("धन्यावद (Thank you!)", tex_template=manim_devanagari.devanagari),
            Tex(r"द्विघात सुत्र (Quadratic formula) \\ $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$", tex_template=manim_devanagari.devanagari),
            MathTex(r"\text{भिन्न} = \dfrac{\text{अंश}}{\text{हर}}", tex_template=manim_devanagari.devanagari)
        ).arrange(DOWN)

        self.add(dev_tex)
```

![DevanagariTex](https://github.com/avnlearn/manim-devanagari/beta/assets/images/1.png?raw=true)

## Devanagari Class

- A string compiled with LaTeX in normal mode

```python
manim_devanagari.Deva_Tex(...)
```

- A string compiled with LaTeX in math mode.

```python
manim_devanagari.Deva_MathTex(...)
```

### Example :

```python
from manim import *
import manim_devanagari

class Devanagari_ClassTex(Scene):
    def construct(self):
        dev_tex = VGroup(
            manim_devanagari.Deva_Tex("धन्यावद", font_size=DEFAULT_FONT_SIZE),
            manim_devanagari.Deva_Tex("धन्यावद (Thank you!)", font_size=DEFAULT_FONT_SIZE),
            manim_devanagari.Deva_Tex(r"द्विघात सुत्र (Quadratic formula) \\ $x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$", font_size=DEFAULT_FONT_SIZE),
            manim_devanagari.Deva_MathTex(r"\text{भिन्न} = \dfrac{\text{अंश}}{\text{हर}}", font_size=DEFAULT_FONT_SIZE)
        ).arrange(DOWN)

        self.add(dev_tex)
```

![Devanagari_ClassTex](https://github.com/avnlearn/manim-devanagari/beta/assets/images/2.png?raw=true)

## Cancel Class

```python
manim_devanagari.Cancel(...)
```

### Example :

```python
from manim import *
import manim_devanagari

class Cancel_Math(Scene):
    def construct(self):
        cancel_tex = VGroup(
            manim_devanagari.Deva_MathTex(r"{{(1 + x)",r"(2 - x^2)}",r"\over",r"{(1 + x)}}", font_size=DEFAULT_FONT_SIZE),
            MathTex(r"{{(1 + x)",r"(2 - x^2)}",r"\over",r"{(2 - x^2)}}")
        ).arrange(DOWN)

        self.add(cancel_tex)
        self.add(manim_devanagari.Cancel(cancel_tex[0][0]))
        self.add(manim_devanagari.Cancel(cancel_tex[0][3]))

        self.add(manim_devanagari.Cancel(cancel_tex[1][1]))
        self.add(manim_devanagari.Cancel(cancel_tex[1][3]))
```

![Cancel_Math](https://github.com/avnlearn/manim-devanagari/beta/assets/images/3.png?raw=true)

## Addition Feature

- Question Header

```python
manim_devanagari.Question_Header(question_no, ...)
```

- Solution Header

```python
manim_devanagari.Solution_Header() # उत्तर :
```

```python
manim_devanagari.Solution_Header(ans=False) # हल :
```

### Example :

```python
from manim import *
import manim_devanagari

class Addition_feature(Scene):
    def construct(self):
        footer = Rectangle(
        width=self.camera.frame_width,
        height=0.8,
        stroke_opacity=0,
        fill_color=GREEN,
        fill_opacity=1,
        ).to_edge(DOWN / 10)

        cancel_tex = VGroup(
            manim_devanagari.Question_Header(1, font_size=DEFAULT_FONT_SIZE),
            manim_devanagari.Solution_Header(font_size=DEFAULT_FONT_SIZE),
            manim_devanagari.Solution_Header(ans=False, font_size=DEFAULT_FONT_SIZE)
        ).arrange(DOWN)
        self.add(cancel_tex, footer)
```

![Addition_feature](https://github.com/avnlearn/manim-devanagari/beta/assets/images/4.png?raw=true)

# Light Mode and Custom Font Size

```python
from manim_devanagari import *

_LIGHT_MODE = True # Light Mode is true
config.background_color = WHITE
_SET_FONT_SIZE = 30
```

# Groups

## Question Group

```python
Question_Group(question_number, item_1, item_2, ..., item_n)
```

```python
Question_Group(question_number, item_1, item_2, ..., item_n)
```

## Solution Group

```python
Solution_Group((question_number, item_1), item_2, ..., item_n)
```

```python
Solution_VGroup(question_number, item_1,(item_2, ..., item_n))
```

## Answer Group

```python
Answer_Group((question_number, item_1), item_2, ..., item_n)
```

```python
Answer_VGroup(question_number, item_1,(item_2, ..., item_n))
```

# String

## String Join

Space or newline is defalult

```python
Str_Join(item_1,item_2, ..., item_n, space=False)
```

## Bookmark

```python
Bookmark(mark)
```

```
<bookmark mark='{mark}'>
```
