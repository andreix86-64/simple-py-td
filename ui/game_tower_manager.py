from abc import ABC

import pygame

from generics.generics import RenderableInterface, EventListener
from ui.game_mouse_observer import GameMouseObserverEvent, GameMouseObserver
from entities.entity import Entity
from world.game_world import GameWorld, TOWER

SHAKE_DURATION = 100


class GameTowerManager(EventListener, RenderableInterface, ABC):
    def __init__(self, engine):
        self.engine = engine
        self.world = engine.world  # type: GameWorld
        self.game_mouse_observer = engine.game_mouse_observer  # type: GameMouseObserver

        # Placement
        self.tower_to_place = None  # type: Entity

        # Shaking animation
        # TODO: Create specialized class for general entities
        self.is_shaking = False
        self.shake_duration = SHAKE_DURATION
        self.shake_range = 10
        self.shake_speed = 1
        self.shake_offset = 0
        self.shake_direction = 1

        # Init the listener
        self.game_mouse_observer.listen(pygame.MOUSEBUTTONUP, self._handle_mouse_click)
        self.game_mouse_observer.listen(pygame.MOUSEMOTION, self._handle_mouse_motion)

    '''
        Handlers
    '''

    def _handle_mouse_click(self, args: GameMouseObserverEvent):
        print(args)
        if self.tower_to_place is not None:
            if len(self.world.get_collision_with_entity(self.tower_to_place)) == 0:
                self.world.add_entity(self.tower_to_place, TOWER)
                self.stop_tower_placement()
            else:
                self._shake(self.tower_to_place)

    def _handle_mouse_motion(self, args: GameMouseObserverEvent):
        if self.tower_to_place is not None:
            x = self.game_mouse_observer.mouse_x - self.tower_to_place.width / 2
            y = self.game_mouse_observer.mouse_y - self.tower_to_place.height / 2
            self.tower_to_place.set_position(x, y)

    def _shake(self, entity: Entity):
        self.is_shaking = True
        self.shake_direction = SHAKE_DURATION
        self.shake_offset = 0

    def _stop_shaking(self):
        self.is_shaking = False
        self.shake_duration = SHAKE_DURATION

    def _update_shake(self):
        if self.tower_to_place is not None:
            if abs(self.shake_offset) >= self.shake_range:
                self.shake_speed = self.shake_speed * -1

            self.shake_offset += self.shake_speed
            self.shake_duration -= 1
            self.tower_to_place.move(self.shake_speed, 0)

            if self.shake_duration <= 0:
                self._stop_shaking()

    '''
        Public functions
    '''

    def stop_tower_placement(self):
        self.tower_to_place = None

    def start_tower_placement(self, tower: Entity):
        self.tower_to_place = tower

    def render(self):
        # Render the tower that has to be placed (if it exists)
        if self.tower_to_place is not None:
            if self.is_shaking:
                self._update_shake()
            self.tower_to_place.render()
