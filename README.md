# Differential Steering Examples

This repository includes some simple simulation examples of mobile Differential Robotics platform on [Python Robotics ToolBox](https://pythonrobotics.io/). 

The robot model receive the speed of each side of the platform:

$$
v_l(t)
$$

$$
v_r(t)
$$

and return the position and direction of the robot:

$$
X(t) = \left[ x(t), \ y(t), \ \theta(t) \right]
$$

You can see the complete documentation in [ Robotics Toolbox for Python, Differential steering](https://petercorke.github.io/robotics-toolbox-python/mobile-vehicle-diffsteer.html)

### Installing Python robotics toolbox
Python robotics toolbox require numpy 1.2x

```
pip install numpy==1.26.4 roboticstoolbox-python
```