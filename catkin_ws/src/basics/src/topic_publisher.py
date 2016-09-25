#!/usr/bin/python 

import rospy 

# from std_msgs.msg import Int32 

from basics.msg import Complex 
from random     import random 

rospy.init_node('topic_publisher') 

pub = rospy.Publisher('counter', Complex ) 

rate = rospy.Rate(2) 

# count = 0 
while not rospy.is_shutdown(): 
  msg = Complex () 
  msg.real = random () 
  msg.imaginary = random () 
  pub.publish ( msg ) 
   
  # pub.publish(count) 
  # count += 1 

  rate.sleep() 
