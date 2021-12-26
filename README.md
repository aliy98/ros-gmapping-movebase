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
$ roslaunch final_assignment simulation_gmapping.launch
```
in order to run the movebase node, open a new terminal in the same directory and run the following commands:
```bashscript
$ source devel/setup.bash
$ roslaunch final_assignment move_base.launch
```
For initializing the master node also, in a new terminal run the following commands:
```bashscript
$ source devel/setup.bash
$ roslaunch final_assignment master.launch
```
then you can choose robot's behaviour by inputing the corresponding number


## Pseudocode
```
***
  master node:
  
  main()
  {
    initialize master node
    get user request for selecting robot's behaviour
    send service response to other three nodes to enable the chosen one
  }

  
***
  movebase client node:
  
  while(1)
  {
    initialize movebase client node
    call master node to get if enable response has been sent from user input
    get target point from user
    call movebase node to send target point as an action 
    detect if the target has been reached before timeout
  }

***
  teleop twist keyboard node:
  
  while(1)
  {
    initialize teleop twist keyboard node
    call master node to get if enable response has been sent from user input
    get user command for moving the robot
    publish the corresponding twist to cmd_vel topic
  }
 
 ***
  assisted teleop keyboard node:
  
  while(1)
  {
    initialize assisted teleop keyboard node 
    call master node to get if enable response has been sent from user input
    subscribe laser scan topic to detect obstacles
    get user command for moving the robot
    if there is an obstacle {
      don't move the robot toward it
    } else {
      publish the corresponding twist to cmd_vel topic
    }
  }
```


