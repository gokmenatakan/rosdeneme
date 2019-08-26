#!/usr/bin/env python
import rospy
from rosserial_arduino.msg import *
import math
import time
from std_srvs.srv import Empty
import numpy as np
from magnet_moment import magnet
def callback(adc_message):

    b=adc_message.adc0
    vcupe=1
    vcylindir=1.0602875205866*(10**-8)
    dd=magnet(0.0015,0.002)#d=heiht,z=distancce from a pole face
    #md1= dd.cupe_dipole_moment(0.01,0.01,b,vcupe)#w=width,l=length,
    md2= dd.cylindir_dipole_moment(0.0015,b,vcylindir)#r=radius of cylindir
    loop_rate = rospy.Rate(10)
    loop_rate.sleep()
    print ('magneticdipolemoment = {}'.format(md2),"A/m^2") #new in python 3

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    analog_topic='/adc'
    rospy.Subscriber(analog_topic,Adc, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()


              
            
