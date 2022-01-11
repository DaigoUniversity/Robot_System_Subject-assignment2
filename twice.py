#!/user/bin/env python3
#SPDX-License-Indentifier: GPL-3.0
#Copyright (C) 2021 Ryuichi Ueda. All rights reserved.
import rospy
from std_msgs_msg import Int32

n = 0

def cb(message):
    global n
    n = message.data*2

if __name__== '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
~                            
