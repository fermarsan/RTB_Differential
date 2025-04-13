import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np
from DiffSteer2 import DiffSteer2


# load the map
map2 = np.load('map2.npy')

plt.imshow(map2, cmap='binary')
plt.grid(False)

a = rtb.VehicleIcon("diff_rays.png", scale=100)

robot = DiffSteer2(x0=(25, 75, 0), 
                   animation=a,
                   workspace=[0, map2.shape[1], 0, map2.shape[0]])

robot.control = (50, 50.1)


robot.run(animate=True)