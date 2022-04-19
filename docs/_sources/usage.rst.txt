Usage
=====

Installation
------------

Here is the instruction for installing the package:

.. code-block:: console

   $ mkdir -p catkin_ws/src
   $ cd catkin_ws/src
   $ git clone https://github.com/aliy98/ros_gmapping_movebase
   $ cd ..
   $ source /opt/ros/<distro>/setup.bash
   $ catkin_make

This rospackage also uses konsole for having multiple command shells. It can be installed with this command:

.. code-block:: console

   $ sudo apt install konsole

Running
--------

Now you can initialize the simulation environment in gazebo and run rviz in the same time using the commands below

.. code-block:: console

   $ source devel/setup.bash
   $ roslaunch final_assignment simulation_gmapping.launch

In order to run the movebase node, open a new terminal in the same directory and run the following commands:

.. code-block:: console

   $ source devel/setup.bash
   $ roslaunch final_assignment move_base.launch

For initializing the master node also, in a new terminal run the following commands:

.. code-block:: console
   
   $ source devel/setup.bash
   $ roslaunch final_assignment master.launch

then you can choose robot's behaviour by inputing the corresponding number
