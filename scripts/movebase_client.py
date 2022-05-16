#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import time
from std_msgs.msg import String

"""
    movebase client Node:
        gets desired position from user and sends it to movebase node using 
        actionlib and if the goal is not reached before timeout cancels it
"""

goal_x = 0
goal_y = 0
reached_targets = 0
not_reached_targets = 0

def callback_movebase_client_goal(data):
    global goal_x
    global goal_y
    goal = data.data
    goal_list = goal.split(',')
    goal_x = goal_list[0]
    goal_y = goal_list[1]


def movebase_clinet():
    global goal_x
    global goal_y
    global reached_targets 
    global not_reached_targets 
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # Gets goal position from user
    goal.target_pose.pose.position.x = float(goal_x)
    goal.target_pose.pose.position.y = float(goal_y)
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
        reached_targets += 1
        rospy.set_param('reached_targets', reached_targets)
        time.sleep(3)
        return client.get_result()
    else:
        print("Action did not finish before time out!")
        not_reached_targets += 1
        rospy.set_param('not_reached_targets', not_reached_targets)
        time.sleep(3)
        client.cancel_all_goals()


def main():
    rospy.init_node('movebase_client')
    rospy.Subscriber("movebase_client_goal", String, callback_movebase_client_goal)
    rospy.set_param('robot_state', '0')
    rospy.set_param('input_target', '0')
    rospy.set_param('reached_targets', reached_targets)
    rospy.set_param('not_reached_targets', not_reached_targets)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if rospy.get_param('robot_state')=='1' and rospy.get_param('input_target')=='1':
            rospy.set_param('input_target', '0')
            movebase_clinet()
            
        else:
            rate.sleep()
            continue
        rate.sleep()

if __name__ == '__main__':
    main()
