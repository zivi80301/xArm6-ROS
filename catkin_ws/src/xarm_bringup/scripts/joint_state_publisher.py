#!/usr/bin/env python3

#importing various packages
import sys
import os
import rospy
import random
from xarm_bringup.msg import JointStates

sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI

#instantiating xArm6 and connecting to arm with IP=192.168.1.217
arm = XArmAPI('192.168.1.217')

#publisher node. publishes JointStates message containing joint angles to joint_states topic
def talker():
    pub = rospy.Publisher("joint_states", JointStates, queue_size=10)
    rospy.init_node("joint_state_pub", anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        jointStates = JointStates()

        angles = arm.last_used_angles

        jointStates.j1 = int(angles[0])
        jointStates.j2 = int(angles[1])
        jointStates.j3 = int(angles[2])
        jointStates.j4 = int(angles[3])
        jointStates.j5 = int(angles[4])

        pub.publish(jointStates)

        rate.sleep()

#running publisher in main
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass