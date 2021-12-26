#!/usr/bin/env python
import rospy
from std_srvs.srv import *
import time

"""
    master node:
        gets user request to choose robot behaviour
        using the following services
"""
srv_client_movebase_client_ = None
srv_client_teleop_keyboard_ = None
srv_client_assisted_teleop_ = None
state_desc_ = ['movebase client', 'teleop keyboard', 'assisted teleop']
state_ = 0
# 0 - movebase client
# 1 - teleop keyboard
# 2 - assisted teleop

# selects robot's behaviour and sends the corresponding response to other three nodes
def select_state(state):
    global state_, state_desc_
    global srv_client_movebase_client_, srv_client_teleop_keyboard_, srv_client_assisted_teleop_
    state_ = state
    print("state selected: %s"  % state_desc_[state])
    if state_ == 0:
        resp = srv_client_movebase_client_(True)
        resp = srv_client_teleop_keyboard_(False)
        resp = srv_client_assisted_teleop_(False)
    if state_ == 1:
        resp = srv_client_movebase_client_(False)
        resp = srv_client_teleop_keyboard_(True)
        resp = srv_client_assisted_teleop_(False)
    if state_ == 2:
        resp = srv_client_movebase_client_(False)
        resp = srv_client_teleop_keyboard_(False)
        resp = srv_client_assisted_teleop_(True)

def main():
    time.sleep(2)
    global srv_client_movebase_client_, srv_client_teleop_keyboard_, srv_client_assisted_teleop_
    rospy.init_node('master')
    srv_client_movebase_client_ = rospy.ServiceProxy(
        '/movebase_client_switch', SetBool)
    srv_client_teleop_keyboard_ = rospy.ServiceProxy(
        '/teleop_keyboard_switch', SetBool)
    srv_client_assisted_teleop_ = rospy.ServiceProxy(
        '/assisted_teleop_switch', SetBool)

    # gets robot behaviour from user
    x = input('''Choose robot behaviour:
    1. reach point(x,y) autonomously
    2. drive with keyboard
    3. drive robot with collision avoidance
    ''')

    if x == '1':
        select_state(0)
    elif x == '2':
        select_state(1)
    elif x == '3':
        select_state(2)

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    main()



