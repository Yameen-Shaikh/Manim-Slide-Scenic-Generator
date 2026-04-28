# assets.py
import logging
from pathlib import Path
from manim import ImageMobject, Square
from theme import Theme

# Set up standard logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class AssetManager:
    def __init__(self, base_dir: str = "assets"):
        self.base_dir = Path(base_dir)
        # Automatically create the assets directory if it doesn't exist
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def get_image(self, filename: str) -> ImageMobject | Square:
        if not filename:
            return self._get_fallback("No filename provided in JSON.")

        filepath = self.base_dir / filename

        if not filepath.is_file():
            return self._get_fallback(f"Image not found at path: {filepath}")

        try:
            # Manim requires a string path, so we cast the Path object back to str
            return ImageMobject(str(filepath))
        except Exception as e:
            return self._get_fallback(f"Failed to load image '{filename}'. Error: {e}")

    def _get_fallback(self, reason: str) -> Square:
        """Returns a red square and logs a warning when an image fails to load."""
        logger.warning(reason)
        return Square(color=Theme.ERROR).set_fill(Theme.ERROR, opacity=0.2)