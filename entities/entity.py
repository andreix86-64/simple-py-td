import pygame
from game_engine import GameEngine
import lib.constants as c


class Entity:
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        """
        :param x:
        :type x: float
        :param y:
        :type y: float
        :param width:
        :type width: float
        :param height:
        :type height: float
        :param background_color:
        :type background_color:
        :param engine:
        :type engine: GameEngine
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.background_color = background_color
        self.engine = engine  # type: GameEngine

        # Init the rectangle
        self.rect = pygame.Rect(x, y, self.width, self.height)  # type: pygame.Rect

    def set_position(self, x, y):
        """ Sets/Updates the position of the entity
        :param x: X-Coordinate
        :type x: float
        :param y: Y-Coordinate
        :type y: float
        """
        self.x = x
        self.y = y

        # Move the rectangle to the x / y position
        self.rect.move_ip(x, y)

    def render(self):
        """ Renders the entity """
        pygame.draw.rect(self.engine.screen, c.BLUE, self.rect)


class MovingEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)


class StationaryEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)
