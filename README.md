# xArm6-ROS
The catkin workspace used to control the xArm6 with Unity @ HRL

This must be placed in the home folder of your Ubuntu 20.04 subsystem. Navigate to the catkin_ws directory in your Ubuntu terminal and build the catkin workspace with 
```
catkin_make
```
Then source it automatically through your .bashrc by adding
```
source ~/ catkin_ws / devel / setup . bash
```
to the very end of your .bashrc file, which can be found in the home directory of your Ubuntu subsystem.

To launch the TCP-Endpoint, coppy the following command to your terminal:
```
roslaunch ros_tcp_endpoint endpoint.launch
```
