from roboticstoolbox import VehiclePolygon
import numpy as np


class VehiclePolygon2(VehiclePolygon):
    def __init__(self, shape="car", scale=1, **kwargs):
        super().__init__()
        if isinstance(shape, str):

            # consider vehicle at origin, pointing along +ve x-axis
            h = 0.3
            t = 0.8  # start of head taper
            c = 0.5  # centre x coordinate
            w = 1  # width in x direction

        if isinstance(shape, str):
            if shape == "car":
                self._coords = np.array(
                    [
                        [-c, h],
                        [t - c, h],
                        [w - c, 0],
                        [t - c, -h],
                        [-c, -h],
                    ]
                ).T
            elif shape == "box":
                self._coords = np.array(
                    [
                        [-c, h],
                        [w - c, h],
                        [w - c, -h],
                        [-c, -h],
                    ]
                ).T
            elif shape == "triangle":
                self._coords = np.array(
                    [
                        [-c, h],
                        [w, 0],
                        [-c, -h],
                    ]
                ).T
            else:
                raise ValueError("unknown vehicle shape name")

        elif isinstance(shape, np.ndarray) and shape.shape[1] == 2:
            self._coords = shape.T
        else:
            raise TypeError("unknown shape argument")
        self._coords *= scale
        self._args = kwargs