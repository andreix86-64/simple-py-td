import pygame
from generics.generics import EventListener, Notifier
import game_engine
from datetime import datetime


class GameMouseObserverEvent:
    def __init__(self, event: pygame.event.Event, point_collisions):
        self.pygame_event = event
        self.point_collisions = point_collisions


class GameMouseObserver(EventListener, Notifier):
    def __init__(self, engine):
        super(GameMouseObserver, self).__init__()

        self.mouse_x = 0
        self.mouse_y = 0

        self.mouse_button_down = False
        self.mouse_button_down_pos = (0, 0)
        self.mouse_button_down_time = 0

        self.mouse_button_up = False
        self.mouse_button_up_pos = (0, 0)
        self.mouse_button_up_time = 0

        self.engine = engine  # type: game_engine.GameEngine
        self.game_world = self.engine.world

    def _handle_mouse_move(self, event: pygame.event.Event):
        self.mouse_x = event.pos[0]
        self.mouse_y = event.pos[1]

    def _handle_mouse_up(self, event: pygame.event.Event):
        self.mouse_button_up_time = datetime.now()

        self.mouse_button_up = True
        self.mouse_button_down = False

        self.mouse_button_down_pos = event.pos

    def _handle_mouse_down(self, event: pygame.event.Event):
        self.mouse_button_down_time = datetime.now()

        self.mouse_button_down = True
        self.mouse_button_up = True

        self.mouse_button_up_pos = event.pos

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            self._handle_mouse_up(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_mouse_down(event)
        elif event.type == pygame.MOUSEMOTION:
            self._handle_mouse_move(event)

        # Inform the listeners that an event has happened
        if hasattr(event, 'pos'):
            point_collision = self.game_world.get_collision_with_point(event.pos)
            self.notify(event.type, GameMouseObserverEvent(event, point_collision))
