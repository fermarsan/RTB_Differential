import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import numpy as np

robot = rtb.DiffSteer(x0=(0, 0, np.pi/2))
robot

vl = [2, 4, 2]
vr = [2, -4, 2]

times = 5

for _ in range(times):
    for vl_i, vr_i in zip(vl, vr):
        robot.step((vl_i, vr_i))

print(robot.x_hist)

x = np.insert(robot.x_hist[:,0], 0, robot.x0[0])
y = np.insert(robot.x_hist[:,1], 0, robot.x0[1])

plt.plot(x, y, marker='.')
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Robot location')

plt.show()