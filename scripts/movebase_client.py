#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_srvs.srv import *

"""
    movebase client Node:
        gets desired position from user and sends it to movebase node using 
        actionlib and if the goal is not reached before timeout cancels it
"""
active_ = False

# enables movebase client node if user has chosen it in master node
def movebase_client_switch(req):
    global active_
    active_ = req.data
    res = SetBoolResponse()
    res.success = True
    res.message = 'Done!'
    return res

def movebase_clinet():
    # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # Gets goal position from user
    print("Set new goal point:")
    goal.target_pose.pose.position.x = float(input("Enter goal x position: "))
    goal.target_pose.pose.position.y = float(input("Enter goal y position: "))

    # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0
    # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()
    # Sends the goal to the action server.
    client.send_goal(goal)
    finished_before_timeout = client.wait_for_result(timeout=rospy.Duration(30))
    # detects if the target is reached before timeout
    if finished_before_timeout:
        print("Target reached!")
        return client.get_result()
    else:
        print("Action did not finish before time out!")
        client.cancel_all_goals()

def main():
    global active_
    rospy.init_node('movebase_client')
    srv = rospy.Service('movebase_client_switch', SetBool, movebase_client_switch)
    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        if not active_:
            rate.sleep()
            continue
        else:
            movebase_clinet()
        rate.sleep()

if __name__ == '__main__':
    main()


