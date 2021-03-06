from typing import List
import pygame
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

        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        """ Sets/Updates the position of the entity
        :param dx: X-Coordinate
        :type dx: float
        :param dy: Y-Coordinate
        :type dy: float
        """
        # Move the rectangle to the x / y position

        self.rect.move_ip(dx, dy)

        self.x = self.rect.x
        self.y = self.rect.y

    def collides_with_entity(self, entity):
        """
        Return True if there is a collision
        :param entity:
        :type entity: Entity
        :return:
        :rtype: bool
        """
        return entity.rect.colliderect(self.rect)

    def collides_with_point(self, point):
        return self.rect.collidepoint(point[0], point[1])

    def render(self):
        """ Renders the entity """
        pygame.draw.rect(self.engine.screen, self.background_color, self.rect)

    def update(self):
        pass


class MovingEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine=engine)

        self._path_to_follow = []  # type: List[(int, int)]
        self._current_path_target_index = -1  # type: int
        self._speed = [0, 0]

        self.tolerance = 3  # type: int
        self.velocity = 0.25  # type: float

    def set_path_to_follow(self, path):
        self._current_path_target_index = 0
        self._path_to_follow = path

    def update(self):
        if self._current_path_target_index != -1:
            # We finished following the path
            if self._current_path_target_index >= len(self._path_to_follow):
                self._current_path_target_index = -1
            else:
                # Follow the path
                position = self._path_to_follow[self._current_path_target_index]
                # print(position)

                # Calculate the new position
                target_x = position[0] - self.width / 2
                target_y = position[1] - self.height / 2

                dx = self.x - target_x
                dy = self.y - target_y

                if dx != 0:
                    dx = +self.velocity if dx < 0 else -self.velocity

                if dy != 0:
                    dy = +self.velocity if dy < 0 else -self.velocity

                self._speed[0] += dx
                self._speed[1] += dy

                # print(self.x, self.y)

                self.move(self._speed[0], self._speed[1])

                if self._speed[0] >= 1:
                    self._speed[0] -= int(self._speed[0])
                if self._speed[1] >= 1:
                    self._speed[1] -= int(self._speed[1])

                # self.set_position(position[0], position[1])
                # Go to the next position
                if self.collides_with_point(position):
                    self._current_path_target_index += 1


class StationaryEntity(Entity):
    def __init__(self, x, y, width, height, background_color=None, engine=None):
        super().__init__(x, y, width, height, background_color, engine)
