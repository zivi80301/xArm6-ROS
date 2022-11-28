#!/usr/bin/env python3

#importing various packages
import sys
import os
import math
import rospy
from tf.transformations import euler_from_quaternion
from xarm_bringup.msg import PosRot

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

#Instantiating xArm6 object and connecting to arm with IP=192.168.1.217
arm = XArmAPI('192.168.1.217')

#enabling arm joints, setting control mode to 0, setting state to 0 (see documentation for codes)
#and resetting position at node start
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
arm.move_gohome(wait=True)

#subscriber callback. call set_position function when position and rotation message is recieved with 
#the position and rotation values from said message. Rotation data converted from quaternion to rpy.
def pos_rot_callback(data):
    rospy.loginfo(data)

    (roll_c,pitch_c,yaw_c) = euler_from_quaternion([data.rot_x,data.rot_y,data.rot_z,data.rot_w])

    arm.set_position(x=1000*data.pos_x+207, y=1000*data.pos_z, z=1000*data.pos_y+112+178, roll=-roll_c+math.pi, pitch=-yaw_c, yaw=pitch_c, speed=100, wait=False, is_radian=True, radius=1000)

#main function. Initiate subscriber node
if __name__ == '__main__':

    rospy.init_node("pos_rot_sub")
    rospy.Subscriber("/pos_rot", PosRot, pos_rot_callback)
    rospy.spin()