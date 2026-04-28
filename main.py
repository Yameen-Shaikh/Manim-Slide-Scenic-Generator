# main.py
import json
from manim import *
from manim_slides import Slide
from layouts import SlideLayouts
from assets import AssetManager

class BasicSlide(Slide):
    def construct(self):
        # 1. Initialize our helpers
        self.assets = AssetManager() 
        layouts = SlideLayouts(self)
        
        # 2. Load data
        with open('scenes.json', 'r') as f:
            scenes = json.load(f)
        
        # 3. Define dispatch
        layout_handlers = {
            "hero": layouts.render_hero,
            "comparison": layouts.render_comparison,
            "bullets": layouts.render_bullets,
            "grid": layouts.render_grid,
            "quote": layouts.render_quote,
            "grid_seperate_image": layouts.render_grid_seperate_image,
        }

        # 4. Execute slides
        for data in scenes:
            self.clear()
            handler = layout_handlers.get(data.get("layout"))
            if handler:
                handler(data)
            self.next_slide()