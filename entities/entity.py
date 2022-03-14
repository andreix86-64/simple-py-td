import pygame


class Entity:
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.background_color = background_color
        self.engine = engine


class MovingEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)


class StationaryEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)
