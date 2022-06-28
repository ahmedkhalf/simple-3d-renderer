from typing import Tuple

import numpy as np
import pygame

from gameobject import GameObject
from mesh import Mesh


class Camera(GameObject):
    def __init__(
        self,
        surface: pygame.surface.Surface,
        position: Tuple[float, float, float] = (0, 0, 0),
        rotation: Tuple[float, float, float] = (0, 0, 0),
    ) -> None:
        super().__init__(position, rotation)
        self.surface = surface

    def is_display_surface(self) -> bool:
        return self.surface == pygame.display.get_surface()

    def render_mesh(self, mesh: Mesh) -> None:
        width, height = self.surface.get_size()

        rotation = self._get_rotation_matrix()
        transformed_verts = (rotation @ (mesh.verts - self.position).T).T
        screen_pos = height * transformed_verts[:, :2] / transformed_verts[:, 2, np.newaxis]
        screen_pos = screen_pos + np.array([[width / 2, height / 2]])

        for triangle in screen_pos[mesh.tris]:
            floor_triangle = triangle.astype(int).tolist()
            pygame.draw.lines(self.surface, (255, 255, 255), False, floor_triangle)
