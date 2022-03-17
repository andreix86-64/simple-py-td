import math
from enum import Enum
import pygame
import lib.constants as c
from entities.entity import Entity
from world.path_finder import PathFinder

ENEMY = 0
TOWER = 1
PROJECTILE = 2


class GameWorld:
    def __init__(self, engine):
        self.engine = engine
        self.screen = self.engine.screen

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

        # TODO: Replace later with quad-trees
        self._entities = [
            [],  # ENEMY
            [],  # TOWER
            [],  # PROJECTILE
        ]

        # Grid path of the enemy
        self.enemy_grid_path = self.path_finder.get_single_path(self.start[0], self.finish[0])
        self.enemy_screen_path = self.compute_screen_path()

    def cell_color(self, i, j):
        if self.grid[i][j] == 1:
            return 10, 10, 10
        return c.BACKGROUND_COLOR

    def compute_screen_path(self):
        path = []
        for i in range(len(self.enemy_grid_path)):
            a = self.enemy_grid_path[i]

            x1 = a[1] * self.cell_size + self.cell_size / 2
            y1 = a[0] * self.cell_size + self.cell_size / 2

            path.append((x1, y1))

        self.enemy_screen_path = path
        return path

    def get_start_position(self):
        return self.start[0][1] * self.cell_size, self.start[0][0] * self.cell_size

    '''
        Public 'getter' functions
    '''

    def get_all_entities(self):
        return self._entities[ENEMY]

    '''
        Public 'update' functions
    '''

    def add_entity(self, entity: Entity, type_: int):
        self._entities[type_].append(entity)

    def update(self):
        """ Updates the world parameters based on the engine """
        # Update the cell size based on the window height / width
        self.cell_size = math.ceil(self.engine.window_width / self.size)

        # Update the entities
        # TODO: Maybe move to engine?

    ''' 
        Render functions: 
    '''

    def d_render_enemy_path(self):
        for i in range(len(self.compute_screen_path()) - 1):
            a = self.enemy_screen_path[i]
            b = self.enemy_screen_path[i + 1]

            pygame.draw.line(self.screen, c.RED, a, b, 3)

    def render(self):
        """ Renders the grid """
        for x in range(self.size):
            for y in range(self.size):
                pygame.draw.rect(self.screen, self.cell_color(x, y),
                                 pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size))

        # Debugging:
        if c.DEBUG_ENEMY_PATH:
            self.d_render_enemy_path()
