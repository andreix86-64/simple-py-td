import pygame
from world.game_world import GameWorld
import lib.constants as c


class GameEngine:
    def __init__(self):
        self.window_height = 800
        self.window_width = 800

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        self.world = GameWorld(self)

    def update(self):
        self.world.update()

    def render(self):
        self.screen.fill(c.BACKGROUND_COLOR)

        # Render the grid
        self.world.render_grid()

        # Draw the screen
        pygame.display.update()

    def start(self):
        # Game loop
        while self.running:
            # Parse the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
            self.render()

        pygame.quit()
