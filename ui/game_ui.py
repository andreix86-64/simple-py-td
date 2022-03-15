import game_engine
from ui.widgets.text import *


class GameUI:
    def __init__(self, engine):
        self.engine = engine  # type: game_engine.GameEngine

        self.title = SimpleText(self.engine.screen, 'Simple Tower Defense', font_size=30, center_y=False)
        self.title.set_y(50)

    def render(self):
        self.title.render()
