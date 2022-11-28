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

#Service callback, executed on service call. Enables joints, sets mode and state to 0 and homes robot arm
def callback(req):
    print("Resetting xArm")
    arm.motion_enable(True,8)
    arm.set_mode(mode=0)
    arm.set_state(state=0)
    arm.reset(wait=True, is_radian=False, speed = 7.5)

    return []

#Initiates reset server node and executes callback on service call
def reset_server():
    rospy.init_node('reset_server')
    s = rospy.Service('reset_srv', Empty, callback)
    rospy.spin()

if __name__ == '__main__':
    reset_server()