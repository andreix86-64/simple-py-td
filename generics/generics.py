class RenderableObject:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self):
        raise NotImplementedError()

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class EventListener:
    def on_event(self, event):
        raise NotImplementedError()


class GameEvent:
    def __init__(self):
        pass
