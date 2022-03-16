import math

import pygame
import lib.constants as c
from world.path_finder import PathFinder


class GameWorld:
    def __init__(self, engine):
        self.engine = engine
        self.size = 15
        self.cell_size = 20

        self.start = [(0, 2)]
        self.finish = [(11, 14)]

        self.grid = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.path_finder = PathFinder(self.grid)

        # Grid path of the enemy
        self.enemy_grid_path = self.path_finder.get_single_path(self.start[0], self.finish[0])

    def cell_color(self, i, j):
        if self.grid[i][j] == 1:
            return 10, 10, 10
        return c.BACKGROUND_COLOR

    def update(self):
        """ Updates the world parameters based on the engine """
        # Update the cell size based on the window height / width
        self.cell_size = math.ceil(self.engine.window_width / self.size)

    def render_enemy_path(self):
        pass

    def render_grid(self):
        """ Renders the grid """
        for x in range(self.size):
            for y in range(self.size):
                pygame.draw.rect(self.engine.screen, self.cell_color(x, y),
                                 pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size))

        # Debugging:
        if c.DEBUG_ENEMY_PATH:
            self.render_enemy_path()
