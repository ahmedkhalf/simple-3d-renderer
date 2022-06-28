from math import cos, sin
from typing import Optional, Tuple

import numpy as np
from numpy import typing as npt

from mesh import Mesh
from monobehaviour import MonoBehaviour


class GameObject(MonoBehaviour):
    def __init__(
        self,
        position: Tuple[float, float, float] = (0, 0, 0),
        rotation: Tuple[float, float, float] = (0, 0, 0),
        mesh: Optional[Mesh] = None,
    ) -> None:
        self.position: npt.NDArray[np.float_] = np.array(position, dtype=np.float64)
        self.rotation: npt.NDArray[np.float_] = np.array(rotation, dtype=np.float64)
        self._mesh: Mesh | None = mesh

    @property
    def mesh(self) -> Mesh | None:
        if self._mesh is None:
            return
        rotation = self._get_rotation_matrix()
        transformed_verts = (rotation @ self._mesh.verts.T).T
        return Mesh(transformed_verts, self._mesh.tris)

    def _get_rotation_x(self) -> npt.NDArray[np.float_]:
        xrot = self.rotation[0]
        sin_xrot = sin(xrot)
        cos_xrot = cos(xrot)
        return np.array(
            [[1, 0, 0], [0, cos_xrot, sin_xrot], [0, sin_xrot, cos_xrot]],
            dtype=np.float64,
        )

    def _get_rotation_y(self) -> npt.NDArray[np.float_]:
        yrot = self.rotation[1]
        sin_yrot = sin(yrot)
        cos_yrot = cos(yrot)
        return np.array(
            [[cos_yrot, 0, -sin_yrot], [0, 1, 0], [sin_yrot, 0, cos_yrot]],
            dtype=np.float64,
        )

    def _get_rotation_z(self) -> npt.NDArray[np.float_]:
        zrot = self.rotation[2]
        sin_zrot = sin(zrot)
        cos_zrot = cos(zrot)
        return np.array(
            [[cos_zrot, sin_zrot, 0], [-sin_zrot, cos_zrot, 0], [0, 0, 1]],
            dtype=np.float64,
        )

    def _get_rotation_matrix(self):
        return self._get_rotation_x() @ self._get_rotation_y() @ self._get_rotation_z()
