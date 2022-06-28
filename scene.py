from typing import List, Optional

from camera import Camera
from gameobject import GameObject
from monobehaviour import MonoBehaviour


class Scene(MonoBehaviour):
    def __init__(self) -> None:
        # State
        self._main_camera: Optional[Camera] = None
        self._game_objects: List[GameObject] = []

        # Options / Constants
        self.skybox_color = (0, 0, 0)

    @property
    def main_camera(self) -> Camera:
        if self._main_camera is not None:
            return self._main_camera
        else:
            raise RuntimeError("Main camera does not exist")

    def _add_main_camera(self, camera: Camera):
        if camera.is_display_surface():
            self._main_camera = camera

    def add_game_object(self, object: GameObject) -> None:
        if isinstance(object, Camera):
            self._add_main_camera(object)
        self._game_objects.append(object)

    def on_init(self):
        pass

    def on_event(self, _):
        pass

    def on_loop(self):
        for game_object in self._game_objects:
            game_object.on_loop()

    def on_render(self):
        if self.main_camera is None:
            return

        self.main_camera.surface.fill(self.skybox_color)

        for game_object in self._game_objects:
            game_object_mesh = game_object.mesh
            if game_object_mesh is not None:
                self.main_camera.render_mesh(game_object_mesh)

    def on_cleanup(self):
        pass
