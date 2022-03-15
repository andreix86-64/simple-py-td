import pygame
import pygame.freetype
import lib.constants as c
from generics.generics import RenderableObject
from ui.widgets.text import SimpleText


class SimpleButton(RenderableObject):
    def __init__(self, surface, text, x=0, y=0, padding=(10, 10, 10, 10), background_color=c.BACKGROUND_COLOR,
                 callback=None):
        super().__init__(x, y)
        self.background = None
        self.surface = surface
        self.background_color = background_color

        self.text = SimpleText(self.surface, text, x=x, y=y, font_size=20,
                               font_family=c.HEADER_FONT, font_color=c.RED)

        self.callback = callback

    def render(self):
        """renders the button"""
        size = self.text.get_size()
        pos = self.text.get_position()
        self.background = pygame.Rect(pos[0], pos[1], size[0], size[1])

        # Render the background
        pygame.draw.rect(self.surface, self.background_color, self.background)

        # Render the text
        self.text.render()
