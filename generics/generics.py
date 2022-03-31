from abc import ABC


class RenderableInterface:
    def render(self):
        raise NotImplementedError()


class RenderableObject(RenderableInterface, ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class Notifier:
    def __init__(self):
        self._listeners = {}

    def listen(self, event_name, fn):
        if event_name not in self._listeners:
            self._listeners[event_name] = []

        if fn not in self._listeners[event_name]:
            self._listeners[event_name].append(fn)
            print(self._listeners)

    def remove_listener(self, event_name, fn):
        listeners = self._listeners.get(event_name, [])
        listeners.remove(fn)

    def has_listeners(self, event_name):
        return len(self._listeners.get(event_name, [])) > 0

    def notify(self, event_name, args):
        listeners = self._listeners.get(event_name, [])
        for callback in listeners:
            callback(args)


class GameEvent:
    def __init__(self):
        pass
