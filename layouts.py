# layouts.py
from manim import *
from theme import Theme

class SlideLayouts:
    def __init__(self, slide):
        self.slide = slide

    def render_hero(self, data):
        title = Text(data["text"], color=Theme.PRIMARY, weight=BOLD).scale(Theme.HERO_SCALE).to_edge(UP, buff=Theme.BUFF_LARGE)
        img = self.slide.assets.get_image(data.get("image")).scale(Theme.IMAGE_SCALE_HERO).shift(DOWN * Theme.SHIFT_DEFAULT)
        self.slide.play(Write(title), FadeIn(img, scale=0.8), run_time=Theme.RUN_TIME_NORMAL)

    def render_comparison(self, data):
        header = Text(data["text"], color=Theme.TEXT_MAIN, font_size=Theme.TITLE_SIZE).to_edge(UP)
        vs = Text("VS", color=Theme.ACCENT, font_size=Theme.VS_SIZE).move_to(DOWN * Theme.SHIFT_DEFAULT)
        l_img = self.slide.assets.get_image(data.get("left_img")).scale(1).shift(LEFT * 3.5 + DOWN * Theme.SHIFT_DEFAULT)
        r_img = self.slide.assets.get_image(data.get("right_img")).scale(1).shift(RIGHT * 3.5 + DOWN * Theme.SHIFT_DEFAULT)
        self.slide.play(Write(header), Write(vs), FadeIn(l_img, shift=RIGHT), FadeIn(r_img, shift=LEFT), run_time=Theme.RUN_TIME_NORMAL)

    def render_bullets(self, data):
        header = Text(data["text"], color=Theme.PRIMARY).to_edge(UP)
        img = self.slide.assets.get_image(data.get("image")).scale(1.2).to_edge(LEFT, buff=Theme.BUFF_LARGE)
        self.slide.play(Write(header), FadeIn(img, shift=RIGHT), run_time=Theme.RUN_TIME_NORMAL)
        
        prev_bullet = None
        for i, point in enumerate(data.get("points", [])):
            bullet = Text(f"• {point}", color=Theme.TEXT_MAIN, font_size=Theme.BULLET_SIZE)
            if i == 0:
                prev_bullet = bullet.next_to(img, RIGHT, buff=Theme.BUFF_LARGE).align_to(img, UP)
            else:
                prev_bullet = bullet.next_to(prev_bullet, DOWN, buff=Theme.BUFF_DEFAULT).align_to(prev_bullet, LEFT)
            
            self.slide.play(FadeIn(bullet, shift=RIGHT), run_time=Theme.RUN_TIME_FAST)
            self.slide.next_slide()

    def render_grid(self, data):
        header = Text(data["text"], color=Theme.PRIMARY).to_edge(UP)
        images = Group(*[self.slide.assets.get_image(img_path).scale(Theme.IMAGE_SCALE_DEFAULT) for img_path in data.get("images", [])])
        images.arrange_in_grid(rows=2, buff=Theme.BUFF_DEFAULT).shift(DOWN * Theme.SHIFT_DEFAULT)
        self.slide.play(Write(header), FadeIn(images, shift=UP, lag_ratio=Theme.LAG_RATIO), run_time=Theme.RUN_TIME_NORMAL)

    def render_grid_seperate_image(self, data):
        header = Text(data["text"], color=Theme.PRIMARY).to_edge(UP)
        self.slide.play(Write(header), run_time=Theme.RUN_TIME_NORMAL)

        positions = [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]
        for i, img_path in enumerate(data.get("images", [])):
            if i < len(positions):
                img = self.slide.assets.get_image(img_path).scale(Theme.IMAGE_SCALE_DEFAULT).to_edge(positions[i], buff=Theme.BUFF_LARGE)
                self.slide.play(FadeIn(img, shift=UP), run_time=Theme.RUN_TIME_FAST)
                self.slide.next_slide() 

    def render_quote(self, data):
        quote = Text(f'"{data["text"]}"', slant=ITALIC, color=Theme.PRIMARY_DARK).scale(Theme.QUOTE_SCALE)
        box = SurroundingRectangle(quote, color=Theme.PRIMARY, buff=Theme.BUFF_DEFAULT)
        self.slide.play(Create(box), Write(quote), run_time=Theme.RUN_TIME_NORMAL)