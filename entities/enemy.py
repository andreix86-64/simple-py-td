import pygame
from entities.entity import MovingEntity
import lib.constants as c


class Enemy(MovingEntity):
    def __init__(self, x, y, width, height, background_color=c.RED, engine=None):
        super().__init__(x, y, width, height, background_color, engine=engine)
