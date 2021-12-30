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

## Software Architecture
![Slide1](https://user-images.githubusercontent.com/65722399/147779264-a4f65968-3760-4857-8270-8b281d62693d.JPG)
Software architecture in this project is based on three node:
1. Master Node: gets user request to choose robot behaviour
        using robot_state rosparam
2. Movebase Client Node: gets desired position from user and sends it to movebase node using 
        actionlib and if the goal is not reached before timeout cancels it
3. Teleop Twist Keyboard Node: it has can implement two behaviours on robot:
        1: moving without obstacle avoidance:
            user can move the robot using keys it publishes the desired movements
            to cmd_vel topic
        2: moveing with obstacle avoidance:
            subscribes scan topic and uses it to detect obstacles. user 
            can move the robot using keys and it also avoids the robot
            from colliding the obstacles


## Pseudocode
```
***
  master node:
  
  main()
  {
        set the initial state of robot_state rosparam as 0 (master node)
        initialize the master node
        while (1)
        {
              if robot_state is 0 (master node)
              {
                    get user request for selecting the robot behaviour
                    set robot_state rosparam as the chosen robot behaviour to enable the corresponding node
              } 
              else 
              {
                    wait for other nodes' response 
              }
        }
  }

  
***
  movebase client node:
  
  main()
  {
        initialize movebase client node
        while(1)
        {
              get robot_state rosparam to detect user choice
              if robot_state is 1 (movebase_client node)
              {
                    get target point from user
                    call movebase node to send target point as an action 
                    detect if the target has been reached before timeout
              } 
              else 
              {
                    wait for master node's response
              }
        }
  }

***
  teleop twist keyboard node:
  
  main()
  {
        initialize teleop twist keyboard node
        while(1)
        {
              get robot_state rosparam to detect user choice
              if robot_state is 2 (manual teleop twist keyboard)
              {
                    get user command for moving the robot
                    publish the corresponding twist to cmd_vel topic
              } 
              else if  robot_state is 3 (assisted teleop twist keyboard)
              {
                    subscribe laser scan topic to detect obstacles
                    get user command for moving the robot
                    if there is an obstacle 
                    {
                          don't move the robot toward it
                    } 
                    else 
                    {
                          publish the corresponding twist to cmd_vel topic
                    }
              } 
              else 
              {
                    wait for master node's response
              }
        }
  }
 
```


