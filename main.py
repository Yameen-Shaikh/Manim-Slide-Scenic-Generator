import json
from manim import *
from manim_slides import Slide

class BasicSlide(Slide):
    def construct(self):
        with open('scenes.json', 'r') as f:
            scenes = json.load(f)
        
        layout_handlers = {
            "hero": self.render_hero,
            "comparison": self.render_comparison,
            "bullets": self.render_bullets,
            "grid": self.render_grid,
            "quote": self.render_quote,
            "grid_seperate_image": self.render_grid_seperate_image,
        }

        for data in scenes:
            self.clear()
            handler = layout_handlers.get(data.get("layout"))
            if handler:
                handler(data)
            self.next_slide() 

    def render_hero(self, data):
        title = Text(data["text"], color=GOLD, weight=BOLD).scale(1.1).to_edge(UP, buff=1)
        img = self.get_img(data.get("image")).scale(1.5).shift(DOWN * 0.5)
        self.play(Write(title), FadeIn(img, scale=0.8), run_time=0.6)

    def render_comparison(self, data):
        header = Text(data["text"], color=WHITE, font_size=32).to_edge(UP)
        vs = Text("VS", color=RED, font_size=40).move_to(DOWN * 0.5)
        l_img = self.get_img(data.get("left_img")).scale(1).shift(LEFT * 3.5 + DOWN * 0.5)
        r_img = self.get_img(data.get("right_img")).scale(1).shift(RIGHT * 3.5 + DOWN * 0.5)
        self.play(Write(header), Write(vs), FadeIn(l_img, shift=RIGHT), FadeIn(r_img, shift=LEFT), run_time=0.6)

    def render_bullets(self, data):
        header = Text(data["text"], color=GOLD).to_edge(UP)
        img = self.get_img(data.get("image")).scale(1.2).to_edge(LEFT, buff=1)
        self.play(Write(header), FadeIn(img, shift=RIGHT), run_time=0.6)
        
        prev_bullet = None
        for i, point in enumerate(data.get("points", [])):
            bullet = Text(f"• {point}", color=WHITE, font_size=24)
            if i == 0:
                prev_bullet = bullet.next_to(img, RIGHT, buff=1).align_to(img, UP)
            else:
                prev_bullet = bullet.next_to(prev_bullet, DOWN, buff=0.5).align_to(prev_bullet, LEFT)
            
            self.play(FadeIn(bullet, shift=RIGHT), run_time=0.4)
            self.next_slide()

    def render_grid(self, data):
        header = Text(data["text"], color=GOLD).to_edge(UP)
        images = Group(*[self.get_img(img_path).scale(0.6) for img_path in data.get("images", [])])
        images.arrange_in_grid(rows=2, buff=0.5).shift(DOWN * 0.5)
        self.play(Write(header), FadeIn(images, shift=UP, lag_ratio=0.1), run_time=0.6)

    def render_grid_seperate_image(self, data):
        header = Text(data["text"], color=GOLD).to_edge(UP)
        self.play(Write(header), run_time=0.6)

        positions = [UP + LEFT, UP + RIGHT, DOWN + LEFT, DOWN + RIGHT]
        for i, img_path in enumerate(data.get("images", [])):
            if i < len(positions):
                img = self.get_img(img_path).scale(0.6).to_edge(positions[i], buff=1)
                self.play(FadeIn(img, shift=UP), run_time=0.4)
                self.next_slide() 

    def render_quote(self, data):
        quote = Text(f'"{data["text"]}"', slant=ITALIC, color=GOLD_A).scale(0.8)
        box = SurroundingRectangle(quote, color=GOLD, buff=0.5)
        self.play(Create(box), Write(quote), run_time=0.6)

    def get_img(self, path):
        try: 
            return ImageMobject(f"assets/{path}")
        except Exception: 
            return Square(color=RED).set_fill(RED, 0.2)