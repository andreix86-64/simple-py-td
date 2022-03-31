import pygame

from entities.enemy import Enemy
import world.game_world as gw
import ui.game_ui as ui
import ui.game_mouse_controller as gms
import lib.constants as c


class GameEngine:
    def __init__(self):
        self.window_height = 800
        self.window_width = 800

        self.running = True

        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))  # type: pygame.Surface
        self.world = gw.GameWorld(self)

        self._game_mouse_controller = gms.GameMouseController(self)
        self._game_ui = ui.GameUI(self)

    def update(self):
        self.world.update()

        entities = self.world.get_all_entities()
        for entity in entities:
            entity.update()

    def render(self):
        self.screen.fill(c.BACKGROUND_COLOR)

        # Render the grid
        self.world.render()

        # Render the entities
        entities = self.world.get_all_entities()
        for entity in entities:
            entity.render()

        # Render the UI elements
        self._game_ui.render()

        # Draw the screen
        pygame.display.update()

    def start(self):
        # Game loop
        while self.running:
            # Parse the events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYUP:
                    # Debug
                    if event.unicode == 'm':
                        print('move...')
                        entities = self.world.get_all_entities()
                        for entity in entities:
                            entity.update()

                    elif event.unicode == 's':
                        print('spawn...')

                        start = self.world.get_start_position()
                        enemy = Enemy(start[0], start[1], 20, 20, engine=self)
                        enemy.set_path_to_follow(self.world.enemy_screen_path)

                        self.world.add_entity(enemy, gw.ENEMY)

                elif event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
                    pass

                # Pass the events ...
                self._game_mouse_controller.on_event(event)

            self.update()
            self.render()

        pygame.quit()
