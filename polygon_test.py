import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np
from DiffSteer2 import DiffSteer2
from VehiclePolygon2 import VehiclePolygon2

def cir2poly(radius=1, num_points=25):
    # Generate angles
    theta = np.linspace(0, 2 * np.pi, num_points+1)
    # Calculate x and y coordinates
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    # Combine x and y into a single array of points
    return np.vstack((x[:-1], y[:-1])).T

print(cir2poly(radius=20, num_points=8))

# load the map
map2 = np.load('map2.npy')
plt.imshow(map2, cmap='binary')

a = VehiclePolygon2(shape=cir2poly(radius=20, num_points=8), color="orange")

robot = DiffSteer2(x0=(50, 150, 0), 
                   animation=a,
                   workspace=[0, map2.shape[1], 0, map2.shape[0]])
robot.control = (25, 25)
robot.run(animate=True)