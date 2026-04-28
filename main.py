# main.py
import json
from manim import *
from manim_slides import Slide
from theme import Theme
from layouts import SlideLayouts

class BasicSlide(Slide):
    def construct(self):
        with open('scenes.json', 'r') as f:
            scenes = json.load(f)
        
        # Instantiate the layout helper, passing 'self' (the slide)
        layouts = SlideLayouts(self)
        
        layout_handlers = {
            "hero": layouts.render_hero,
            "comparison": layouts.render_comparison,
            "bullets": layouts.render_bullets,
            "grid": layouts.render_grid,
            "quote": layouts.render_quote,
            "grid_seperate_image": layouts.render_grid_seperate_image,
        }

        for data in scenes:
            self.clear()
            handler = layout_handlers.get(data.get("layout"))
            if handler:
                handler(data)
            self.next_slide() 

    # Keeping get_img here since it interacts directly with Manim's file system handling
    def get_img(self, path):
        try: 
            return ImageMobject(f"assets/{path}")
        except Exception: 
            return Square(color=Theme.ERROR).set_fill(Theme.ERROR, 0.2)