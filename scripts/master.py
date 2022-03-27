#!/usr/bin/env python
"""
.. module:: master
    :platform: Unix
    :synopsis: the main python script in ros_gmapping_movebase package

.. moduleauthor:: Ali Yousefi <aliyousef98@outlook.com>

Uses rosparam:
    /robot_state

The node gets user request to choose robot behaviour using robot_state rosparam

"""

import rospy
from std_srvs.srv import *
import os

# 1 - movebase client
# 2 - teleop keyboard
# 3 - assisted teleop

def change_state():
    """
    Function for changing robot's behaviour and sending the corresponding response to other three nodes

    """
    os.system('cls||clear')
    print("** MASTER NODE **\n")
    # gets robot behaviour from user
    x = input('''Choose robot behaviour:
    1. reach point(x,y) autonomously
    2. drive with keyboard
    3. drive robot with collision avoidance\n
    input: ''')

    if x == '1':
        rospy.set_param('robot_state', '1')
        print("\nstate changed: movebase client")
    elif x == '2':
        rospy.set_param('robot_state', '2')
        print("\nstate changed: teleop keyboard")
    elif x == '3':
        rospy.set_param('robot_state', '3')
        print("\nstate changed: assisted teleop")


def main():
    rospy.init_node('master')
    rospy.set_param('robot_state', '0')
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if rospy.get_param('robot_state')=='0':
            change_state()
        else:
            rate.sleep()
            continue
        rate.sleep()

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    main()



