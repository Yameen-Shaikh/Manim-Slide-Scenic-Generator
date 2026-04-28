# theme.py
from manim import *

class Theme:
    # Colors
    PRIMARY = GREEN
    PRIMARY_DARK = GOLD_A
    TEXT_MAIN = WHITE
    ACCENT = RED
    ERROR = RED

    # Font Sizes / Scales
    TITLE_SIZE = 32
    BULLET_SIZE = 24
    VS_SIZE = 40
    HERO_SCALE = 1.1
    QUOTE_SCALE = 0.8
    IMAGE_SCALE_DEFAULT = 0.6
    IMAGE_SCALE_HERO = 1.5

    # Spacing & Positioning
    BUFF_DEFAULT = 0.5
    BUFF_LARGE = 1.0
    SHIFT_DEFAULT = 0.5
    
    # Animation Timings
    RUN_TIME_FAST = 0.4
    RUN_TIME_NORMAL = 0.6
    LAG_RATIO = 0.1