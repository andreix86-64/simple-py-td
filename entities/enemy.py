import pygame
from entity import MovingEntity


class Enemy(MovingEntity):
    def __init__(self, x, y, width, height, background_color=None):
        super().__init__(x, y, width, height, background_color)
