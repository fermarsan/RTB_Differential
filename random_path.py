import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np
from DiffSteer2 import DiffSteer2

robot = DiffSteer2(x0=(0, 0, np.pi/2))

robot.control = rtb.RandomPath(1)

robot.run()

# Add the initial point to the resultant path
x = np.insert(robot.x_hist[:, 0], 0, robot.x0[0])
y = np.insert(robot.x_hist[:, 1], 0, robot.x0[1])

plt.plot(x, y, marker='.')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Robot location')

plt.savefig('random_path.png')