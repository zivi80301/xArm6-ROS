#!/usr/bin/env python3

#importing various packages
import sys
import os
import math
import time
import rospy
from tf.transformations import euler_from_quaternion
from xarm_bringup.msg import PosRot

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

#Instantiating xArm6 object and connecting to arm with IP=192.168.1.217
arm = XArmAPI('192.168.1.217')

global prev_pose
prev_pose = arm.get_position()[1]

#enabling arm joints, setting control mode to 0, setting state to 0 (see documentation for codes)
#and resetting position at node start
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)
arm.move_gohome(wait=True)

#subscriber callback. call set_position function when position and rotation message is recieved with 
#the position and rotation values from said message. Rotation data converted from quaternion to rpy.
def pos_rot_callback(data):

    arm.set_mode(0)
    arm.set_state(0)

    (roll_c,pitch_c,yaw_c) = euler_from_quaternion([data.rot_x,data.rot_y,data.rot_z,data.rot_w])

    #current_pos = arm.get_position(is_radian=False)[1]
    new_pose = [1000*data.pos_x + 207, 1000*data.pos_z, 1000*data.pos_y + 112+178, -roll_c+math.pi, -yaw_c, pitch_c]
    
    #current_pose = arm.get_position()[1]
    #int_pose = (new_pose + current_pose)
    #print("Unity pose: " + str(new_pose))
    #print("Real pose: " + str(current_pose))
    #arm.move_arc_lines([int_pose, new_pose],speed=60)

    #arm.set_position(x=1000*data.pos_x+207, y=1000*data.pos_z, z=1000*data.pos_y+112+178, roll=-roll_c+math.pi, pitch=-yaw_c, yaw=pitch_c, speed=100, wait=False, is_radian=True, radius=1000)
    #arm.set_position(int_pose[0], int_pose[1], int_pose[2], int_pose[3], int_pose[4], int_pose[5], speed=100, wait=False, is_radian=True, radius=1000)
    #time.sleep(0.05)
    arm.set_position(new_pose[0], new_pose[1], new_pose[2], new_pose[3], new_pose[4], new_pose[5], speed=100, wait=False, is_radian=True, radius=1000)


#main function. Initiate subscriber node
if __name__ == '__main__':

    rospy.init_node("pos_rot_sub")
    rospy.Subscriber("/pos_rot", PosRot, pos_rot_callback)
    rospy.spin()