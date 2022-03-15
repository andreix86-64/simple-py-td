import game_engine
from ui.widgets.text import *
from ui.widgets.buttons import *
from generics.generics import RenderableObject


class GameUI:
    def __init__(self, engine):
        self.engine = engine  # type: game_engine.GameEngine

        self.render_list = []  # type: List[RenderableObject]

        self.title = SimpleText(self.engine.screen, 'Simple Tower Defense', font_size=30, center_y=False)
        self.quit_button = SimpleButton(self.engine.screen, 'Pls work', background_color=c.BLUE)
        self.title.set_y(50)

        # Add the UI elements to the render queue
        self.add_to_render(self.title)
        self.add_to_render(self.quit_button)

        print(self.title.get_size())

    def add_to_render(self, r_object):
        """

        :type r_object: RenderableObject
        """
        self.render_list.append(r_object)

    def render(self):
        for r_object in self.render_list:
            r_object.render()
