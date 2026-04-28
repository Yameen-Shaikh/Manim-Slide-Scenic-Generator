# animations.py
from manim import *
from theme import Theme

class Animator:
    def __init__(self, slide):
        self.slide = slide

    def reveal_title(self, *mobjects):
        """Standard animation for text headers and titles."""
        animations = [Write(m) for m in mobjects]
        self.slide.play(*animations, run_time=Theme.RUN_TIME_NORMAL)

    def enter_element(self, mobject, direction=UP, scale=1.0, fast=False):
        """Standard entrance for images or single elements."""
        run_time = Theme.RUN_TIME_FAST if fast else Theme.RUN_TIME_NORMAL
        self.slide.play(FadeIn(mobject, shift=direction, scale=scale), run_time=run_time)

    def enter_group(self, mobject_group, direction=UP):
        """Standard entrance for grids or groups of elements with a stagger effect."""
        self.slide.play(
            FadeIn(mobject_group, shift=direction, lag_ratio=Theme.LAG_RATIO), 
            run_time=Theme.RUN_TIME_NORMAL
        )

    def emphasize_quote(self, box, quote):
        """Custom animation for drawing a box and writing text."""
        self.slide.play(Create(box), Write(quote), run_time=Theme.RUN_TIME_NORMAL)
        
    def reveal_simultaneously(self, *animations):
        """Allows passing custom animations to run at the same time standardizing the runtime."""
        self.slide.play(*animations, run_time=Theme.RUN_TIME_NORMAL)