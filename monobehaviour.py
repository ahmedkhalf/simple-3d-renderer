from abc import ABC


class MonoBehaviour(ABC):
    def on_init(self):
        pass

    def on_event(self, _):
        pass

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pass
