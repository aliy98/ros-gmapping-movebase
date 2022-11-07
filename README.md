## Jupyter Notebook
To perform a more convenient user interface for this rospackage a [jupyter notebook](https://github.com/aliy98/ros_gmapping_movebase/blob/jupyter_notebook/notebook/ros-gmapping-movebase.ipynb) is also created. With the widgets provided for jupyter notebook, you can:
1. change robot behaviour
2. set goal point for the first behaviour
3. input direction commands for the second and third behaviour
4. see the robot position and obstacles around it

### Usage
Here is the instruction for using the package:
```bashscript
$ mkdir -p catkin_ws/src
```
```bashscript
$ cd catkin_ws/src
```
```bashscript
$ git clone -b jupyter_notebook https://github.com/aliy98/ros_gmapping_movebase
```
```bashscript
$ cd ..
```
```bashscript
$ source /opt/ros/<distro>/setup.bash
```
```bashscript
$ catkin_make
```
```bashscript
$ source devel/setup.bash
```
```bashscript
$ roslaunch final_assignment simulation_gmapping.launch
```
in order to run the movebase node, open a new terminal in the same directory and run the following commands:
```bashscript
$ source devel/setup.bash
```
```bashscript
$ roslaunch final_assignment move_base.launch
```
For initializing the master node also, in a new terminal run the following commands:
```bashscript
$ source devel/setup.bash
```
```bashscript
$ roslaunch final_assignment master.launch
```
then you can run the [jupyter notebook](https://github.com/aliy98/ros_gmapping_movebase/blob/jupyter_notebook/notebook/ros_gmapping_movebase.ipynb) to use the interface.


