import pygame

from camera import Camera
from gameobject import GameObject
from scene import Scene
from mesh import load_obj


class App:
    def __init__(self) -> None:
        # State
        self._running = False
        self._display_surf = None
        self._fps_clock = pygame.time.Clock()

        self.current_scene = Scene()

        # Options / Constants
        self._title = "3d renderer"
        self._win_opts = pygame.RESIZABLE
        self._fps = 60
        self._size = self._width, self._height = 640, 400

    def on_init(self) -> bool:
        pygame.init()
        self._display_surf = pygame.display.set_mode(self._size, self._win_opts)
        pygame.display.set_caption(self._title)

        self.camera = Camera(pygame.display.get_surface(), position=(0, -79.03/2, -200))
        self.current_scene.add_game_object(self.camera)
        self.fox = GameObject(mesh=load_obj("fox.obj"))
        self.current_scene.add_game_object(self.fox)

        return True

    def on_event(self, event) -> None:
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self) -> None:
        self.current_scene.on_loop()
        self.fox.rotation[1] += 0.03

    def on_render(self) -> None:
        self.current_scene.on_render()
        pygame.display.flip()
        self._fps_clock.tick(self._fps)

    def on_cleanup(self) -> None:
        pygame.quit()

    def execute(self):
        if self.on_init():
            self._running = True

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
