import pygame
from entity import StationaryEntity, MovingEntity
import lib.constants as c


class Tower(StationaryEntity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)


class Bullet(MovingEntity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)


class SimpleBulletTower(Tower):
    def __init__(self, x, y, engine):
        super().__init__(x, y, 20, 20, background_color=c.BLUE, engine=engine)