import pygame
from entity import StationaryEntity


class Tower(StationaryEntity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)


class Bullet(StationaryEntity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)
