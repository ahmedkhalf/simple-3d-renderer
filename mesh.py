from dataclasses import dataclass

import numpy as np
from numpy import typing as npt


@dataclass
class Mesh:
    verts: npt.NDArray[np.float_]
    tris: npt.NDArray[np.int_]


def load_obj(filename: str) -> Mesh:
    verts = []
    tris = []

    with open(filename, 'r') as file:
        for line in file:
            match line.split():
                case ["v", x, y, z]:
                    verts.append([float(x), -float(y), -float(z)])
                case ["f", v1, v2, v3]:
                    tri = []
                    for v in (v1, v2, v3):
                        tri.append(int(v.partition("/")[0]) - 1)
                    tris.append(tri)

    verts = np.array(verts, dtype=np.float64)
    tris = np.array(tris, dtype=np.int64)
    return Mesh(verts, tris)
