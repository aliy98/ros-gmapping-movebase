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
    
  }

  
***
  movebase node:
  
  while(1)
  {

  }

***
  teleop twist keyboard node:
  
  while(1)
  {

  }
 
 ***
  assisted teleop keyboard node:
  
  while(1)
  {

  }
```


