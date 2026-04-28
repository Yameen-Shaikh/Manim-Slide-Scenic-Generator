# main.py
import json
from manim import *
from manim_slides import Slide
from layouts import SlideLayouts
from assets import AssetManager
from animations import Animator  # New import

class BasicSlide(Slide):
    def construct(self):
        self.assets = AssetManager() 
        self.animator = Animator(self)   # Initialize animator
        layouts = SlideLayouts(self)     # Pass self (which now has animator)
        
        with open('scenes.json', 'r') as f:
            scenes = json.load(f)
        
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