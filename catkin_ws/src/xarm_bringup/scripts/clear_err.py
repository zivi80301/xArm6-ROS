#!/usr/bin/env python3

#importing various packages
from __future__ import print_function

import rospy
import sys
import os

from std_srvs.srv import Empty

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

#Instantiating xArm6 object and connecting to arm with IP=192.168.1.217
arm = XArmAPI('192.168.1.217')

#Service callback, executed on service call. Enables joints, sets mode and state to 0 without homing robot
def callback(req):
    print("Clearing Errors")
    arm.motion_enable(True,8)
    arm.set_mode(mode=0)
    arm.set_state(state=0)

    return []

#Initiates reset server node and executes callback on service call
def clear_error_server():
    rospy.init_node('clear_error_server')
    s = rospy.Service('clear_error_srv', Empty, callback)
    print("debug?")
    rospy.spin()

if __name__ == '__main__':
    clear_error_server()