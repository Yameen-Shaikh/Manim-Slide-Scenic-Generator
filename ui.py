# ui.py
from manim import Text, SurroundingRectangle, ITALIC, BOLD, VGroup, UP, DOWN
from theme import Theme

class UI:
    @staticmethod
    def header(text: str) -> Text:
        """Standard slide header."""
        return Text(text, color=Theme.PRIMARY).to_edge(UP)

    @staticmethod
    def hero_title(text: str) -> Text:
        """Large, bold title for hero slides."""
        return Text(text, color=Theme.PRIMARY, weight=BOLD).scale(Theme.HERO_SCALE).to_edge(UP, buff=Theme.BUFF_LARGE)

    @staticmethod
    def comparison_header(text: str) -> Text:
        """Header specifically styled for comparison slides."""
        return Text(text, color=Theme.TEXT_MAIN, font_size=Theme.TITLE_SIZE).to_edge(UP)

    @staticmethod
    def vs_label() -> Text:
        """Standard VS text."""
        return Text("VS", color=Theme.ACCENT, font_size=Theme.VS_SIZE).move_to(DOWN * Theme.SHIFT_DEFAULT)

    @staticmethod
    def bullet(text: str) -> Text:
        """Standard bullet point."""
        return Text(f"• {text}", color=Theme.TEXT_MAIN, font_size=Theme.BULLET_SIZE)

    @staticmethod
    def quote_with_box(text: str):
        """Generates a styled quote and its surrounding box."""
        quote = Text(f'"{text}"', slant=ITALIC, color=Theme.PRIMARY_DARK).scale(Theme.QUOTE_SCALE)
        box = SurroundingRectangle(quote, color=Theme.PRIMARY, buff=Theme.BUFF_DEFAULT)
        return quote, box