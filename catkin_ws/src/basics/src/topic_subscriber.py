#!/usr/bin/python 

import rospy 
# from std_msgs.msg import Int32 
from basics.msg import Complex 
from random     import random 

def callback ( msg ) : 
  print 'Real: ', msg.real 
  print 'Imaginary: ', msg.imaginary 

rospy.init_node ( 'topic_subscriber' ) 

sub = rospy.Subscriber( 'counter', Complex, callback ) 

rospy.spin () 
