import pygame
import pygame.freetype
import lib.constants as c
from generics.generics import RenderableObject


class SimpleText(RenderableObject):
    def __init__(self, surface, text, x=0, y=0, font_size=20, center_x=True, center_y=True, font_family=c.HEADER_FONT):
        super().__init__(x, y)

        self.surface = surface  # type: pygame.Surface
        self.text = text  # type: str
        self.font_size = font_size  # type: int
        self.center_x = center_x  # type: bool
        self.center_y = center_y  # type: bool

        self.font = pygame.freetype.SysFont(font_family, 0)  # type: pygame.freetype.Font

    def set_text(self, text):
        self.text = text

    def render(self):
        """ Renders the text """
        # TODO: Cache the text_rect
        text_rect = self.font.get_rect(self.text, size=self.font_size)
        text_rect.x = self.x
        text_rect.y = self.y

        # Check to see if we have to center the text
        if self.center_x:
            text_rect.centerx = self.surface.get_rect().centerx
        if self.center_y:
            text_rect.centery = self.surface.get_rect().centery

        self.font.render_to(self.surface, text_rect, self.text, c.BLUE, size=self.font_size)
