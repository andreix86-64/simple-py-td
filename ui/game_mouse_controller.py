import pygame
from generics.generics import EventListener
import game_engine


class GameMouseController(EventListener):
    def __init__(self, engine):
        self.engine = engine  # type: game_engine.GameEngine
        self.game_world = self.engine.world

    def on_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            collision = self.game_world.get_collision_with_point(event.pos)
            print('press detected', event)
            print('collision', collision)