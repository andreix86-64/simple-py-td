import pygame
from world.game_world import GameWorld
from ui.game_ui import GameUI
import lib.constants as c


class GameEngine:
    def __init__(self):
        self.window_height = 800
        self.window_width = 800

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))  # type: pygame.Surface

        self.world = GameWorld(self)
        self._game_ui = GameUI(self)

    def update(self):
        self.world.update()

    def render(self):
        self.screen.fill(c.BACKGROUND_COLOR)

        # Render the grid
        self.world.render_grid()

        # Render the UI elements
        self._game_ui.render()

        # Draw the screen
        pygame.display.update()

    def start(self):
        # Game loop
        while self.running:
            # Parse the events
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
                    pass

            self.update()
            self.render()

        pygame.quit()
