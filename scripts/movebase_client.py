#!/usr/bin/env python
"""
.. module:: movebase_client
    :platform: Unix
    :synopsis: implements an autonomous behaviour on robot in ros_gmapping_movebase package

.. moduleauthor:: Ali Yousefi <aliyousef98@outlook.com>

Subscribes to:
    /move_base/status

Publishes to:
    /move_base/goal

The node gets desired position from user and sends it to movebase node using actionlib and if the goal is not reached before timeout cancels it

"""
from time import sleep
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import os
import time

def movebase_clinet():
    """
    Function for initializing a client that sends the goal point to movebase actionlib server and requests robot status from it

    """
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    os.system('cls||clear')
    print("** MOVEBASE CLIENT NODE **\n")
    # Gets goal position from user
    print("\nSet new goal point:")
    x = input("Enter goal x position or q to change robot behaviour: ")
    if x == 'q':
        rospy.set_param('robot_state', '0')
        print("\nchoose robot behaviour in master node")
        time.sleep(5)
        os.system('cls||clear')
        print("** MOVEBASE CLIENT NODE **\n")
        print("waiting for master node response...\n")
    else:
        goal.target_pose.pose.position.x = float(x)
        goal.target_pose.pose.position.y = float(input("Enter goal y position: "))
        # No rotation of the mobile base frame w.r.t. map frame
        goal.target_pose.pose.orientation.w = 1.0
        # Waits until the action server has started up and started listening for goals.
        client.wait_for_server()
        # Sends the goal to the action server.
        client.send_goal(goal)
        print("waiting for robot to reach the target wihthin 30 seconds")
        finished_before_timeout = client.wait_for_result(timeout=rospy.Duration(30))
        # detects if the target is reached before timeout
        if finished_before_timeout:
            print("Target reached!")
            time.sleep(3)
            return client.get_result()
        else:
            print("Action did not finish before time out!")
            time.sleep(3)
            client.cancel_all_goals()


def main():
    rospy.init_node('movebase_client')
    rospy.set_param('robot_state', '0')
    os.system('cls||clear')
    print("** MOVEBASE CLIENT NODE **\n")
    print("waiting for master node response...\n")
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if rospy.get_param('robot_state')=='1':
            movebase_clinet()
        else:
            rate.sleep()
            continue
        rate.sleep()

if __name__ == '__main__':
    main()