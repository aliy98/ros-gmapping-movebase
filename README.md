# ros_gmapping_movebase
This ROS package provides three behaviors for controlling  a simulated mobile robot using gmapping and movebase rospackages.
## Installing and runnning 
Here is the instruction for using the package:
```bashscript
$ mkdir -p catkin_ws/src
$ cd catkin_ws/src
$ git clone https://github.com/aliy98/ros_gmapping_movebase
$ cd ..
$ source /opt/ros/<distro>/setup.bash
$ catkin_make
$ source devel/setup.bash
$ roslaunch final_assignment master.launch
