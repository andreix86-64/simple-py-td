import math
from enum import Enum
import pygame
import lib.constants as c
import entities.entity as ent
from world.path_finder import PathFinder

GRID = 0
ENEMY = 1
TOWER = 2
PROJECTILE = 3


class GameWorld:
    def __init__(self, engine):
        self.engine = engine
        self.screen = self.engine.screen

        self.size = 15
        self.cell_size = 20
        self._update_cell_size()

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
            [],  # GRID
            [],  # ENEMY
            [],  # TOWER
            [],  # PROJECTILE
        ]

        # Grid path of the enemy
        self.enemy_grid_path = self.path_finder.get_single_path(self.start[0], self.finish[0])
        self.enemy_screen_path = self._compute_screen_path()
        self._generate_grid_path_entities()

    def cell_color(self, i, j):
        if self.grid[i][j] == 1:
            return 10, 10, 10
        return c.BACKGROUND_COLOR

    def _generate_grid_path_entities(self):
        """
            Generates entities for the path on the grid
            Used for collision
        """

        # Reset the entities
        grid_entities = []
        for point in self.enemy_grid_path:
            x = point[1] * self.cell_size
            y = point[0] * self.cell_size

            grid_entities.append(
                ent.Entity(x, y, self.cell_size, self.cell_size, engine=self.engine, background_color=c.BLACK))

        self._entities[GRID] = grid_entities

    def _compute_screen_path(self):
        print('Computing screen path ...')
        path = []
        for i in range(len(self.enemy_grid_path)):
            a = self.enemy_grid_path[i]

            x1 = a[1] * self.cell_size + self.cell_size / 2
            y1 = a[0] * self.cell_size + self.cell_size / 2

            path.append((x1, y1))

        self.enemy_screen_path = path
        return path

    def _update_cell_size(self):
        self.cell_size = math.ceil(self.engine.window_width / self.size)

    '''
        Public 'getter' functions
    '''

    def get_start_position(self):
        return self.start[0][1] * self.cell_size, self.start[0][0] * self.cell_size

    def get_collision_with_point(self, point):
        entities_ = self.get_all_entities()
        collision = []

        # Entity collision
        for entity in entities_:
            if entity.collides_with_point(point):
                collision.append(entity)

        return collision

    def get_collision_with_entity(self, entity: ent.Entity):
        entities_ = self.get_all_entities()
        collision = []

        # Entity collision
        for entity_ in entities_:
            if entity_.collides_with_entity(entity):
                collision.append(entity_)

        return collision

    def get_all_entities(self):
        return [*self._entities[GRID], *self._entities[ENEMY], *self._entities[TOWER]]

    '''
        Public 'update' functions
    '''

    def add_entity(self, entity: ent.Entity, type_: int):
        self._entities[type_].append(entity)

    def update(self):
        """ Updates the world parameters based on the engine """
        # Update the cell size based on the window height / width
        self._update_cell_size()

        # Update the entities
        # TODO: Maybe move to engine?

    ''' 
        Render functions: 
    '''

    def d_render_enemy_path(self):
        for i in range(len(self.enemy_screen_path) - 1):
            a = self.enemy_screen_path[i]
            b = self.enemy_screen_path[i + 1]

            pygame.draw.line(self.screen, c.RED, a, b, 3)

    def render(self):
        """ Renders the grid """
        for x in range(self.size):
            for y in range(self.size):
                pygame.draw.rect(self.screen, self.cell_color(x, y),
                                 pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size))

        # Render the entities
        entities = self.get_all_entities()
        for entity in entities:
            entity.render()

        # Debugging:
        if c.DEBUG_ENEMY_PATH:
            self.d_render_enemy_path()
