#!/usr/bin/env python
import rospy
from rosserial_arduino.msg import Adc
import math
import time
from std_srvs.srv import Empty
def callback(adc_message):
    print ('Adc0 = {}'.format(adc_message)) #new in python 3

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/adc',Adc, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
