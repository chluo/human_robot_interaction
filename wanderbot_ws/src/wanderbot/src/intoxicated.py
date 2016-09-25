#!/usr/bin/python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

# Determine the distance to the closest object ahead
# based on the laser scan information
def scan_callback(msg):
  global g_range_ahead
  g_range_ahead = min(msg.ranges)

g_range_ahead = 1 

scan_sub = rospy.Subscriber('scan', LaserScan, scan_callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

rospy.init_node('intoxicated')
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  # State transition between moving forward and turning around
  if driving_forward:
    # If there is some obstacles closly ahead, or it has been moving 
    # forward for a relatively long time, then stop moving forward
    if (g_range_ahead < 0.8 or rospy.Time.now() > state_change_time):
      # Stop moving forward and start turning around
      driving_forward = False
      state_change_time = rospy.Time.now() + rospy.Duration(3)

  else: # not driving_forward
    # If it has been turning around for a relatively long time, then stop turning 
    if rospy.Time.now() > state_change_time:
      # Stop turning around and start moving forward 
      driving_forward = True 
      state_change_time = rospy.Time.now() + rospy.Duration(5)

  # Set the speeds for Twist 
  twist = Twist()
  if driving_forward:
    # Moving forward at speed 1
    twist.linear.x = 1
  else:
    # Turning around at speed 1
    twist.angular.z = 1

  cmd_vel_pub.publish(twist)
  rate.sleep()
