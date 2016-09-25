#!/usr/bin/python

import math 
import random
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color
from turtlesim.msg import Pose

PI        = 3.1415927
DIST_THRS = 1.1
FWD_TIME  = 8
TWST_TIME = 1
FWD_SPD   = 0.4
TWST_SPD  = 0.5

Turtles = { \
  'Alex'    : [0.5, 0.5, PI/4], \
  'Bob'     : [8, 8, 0       ], \
  'Charlie' : [5.5, 8, 0     ], \
  'Deb'     : [3, 8, 0       ], \
  'Emma'    : [3, 5.5, 0     ], \
  'Frank'   : [3, 3, 0       ], \
  'George'  : [5.5, 3, 0     ], \
  'Hellen'  : [8, 3, 0       ], \
  'Isac'    : [8, 5.5, 0     ]  \
}

myPose   = Pose()
distList = [10, 10, 10, 10, 10, 10, 10, 10, 10]
anglList = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
# Min distance
minDist  = 20 
# Angle corresponding to the min distance
minAngl  = 0

def nearBorder(p): 
  return p.x < 0.5 or p.x > 10.5 or p.y < 0.5 or p.y > 10.5 

def calcAngl(p1, p2): 
  dy = p1.y - p2.y 
  dx = p1.x = p2.x
  return math.atan2(dy, dx)

def calcDist(p1, p2): 
  tx =  math.pow((p1.x - p2.x), 2)
  ty =  math.pow((p1.y - p2.y), 2)
  return math.sqrt(tx + ty)

def poseA_cb(msg): 
  global myPose 
  myPose = msg

def poseB_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[0] = calcDist(msg, myPose) 
  anglList[0] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseC_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[1] = calcDist(msg, myPose) 
  anglList[1] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseD_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[2] = calcDist(msg, myPose) 
  anglList[2] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseE_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[3] = calcDist(msg, myPose) 
  anglList[3] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseF_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[4] = calcDist(msg, myPose) 
  anglList[4] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseG_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[5] = calcDist(msg, myPose) 
  anglList[5] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseH_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[6] = calcDist(msg, myPose) 
  anglList[6] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseI_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[7] = calcDist(msg, myPose) 
  anglList[7] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

def poseT_cb(msg): 
  global distList 
  global myPose
  global minDist
  distList[8] = calcDist(msg, myPose) 
  anglList[8] = calcAngl(msg, myPose)
  minDist = min(distList)
  minAngl = anglList[distList.index(min(distList))] 

cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

poseA_sub = rospy.Subscriber('poseA', Pose, poseA_cb)
poseB_sub = rospy.Subscriber('poseB', Pose, poseB_cb)
poseC_sub = rospy.Subscriber('poseC', Pose, poseC_cb)
poseD_sub = rospy.Subscriber('poseD', Pose, poseD_cb)
poseE_sub = rospy.Subscriber('poseE', Pose, poseE_cb)
poseF_sub = rospy.Subscriber('poseF', Pose, poseF_cb)
poseG_sub = rospy.Subscriber('poseG', Pose, poseG_cb)
poseH_sub = rospy.Subscriber('poseH', Pose, poseH_cb)
poseI_sub = rospy.Subscriber('poseI', Pose, poseI_cb)
poseT_sub = rospy.Subscriber('poseT', Pose, poseT_cb)

rospy.init_node('social_navi')
state_change_time = rospy.Time.now() + rospy.Duration(2)
rate = rospy.Rate(10)
driving_forward = True
twistFlag = 0
force_fwd = False

while not rospy.is_shutdown():
  # State transition between moving forward and turning around
  if driving_forward :
    # If there is some obstacles closly ahead, or it has been moving 
    # forward for a relatively long time, then stop moving forward
    print "[Merry Alex] Minimum distance: " + str(minDist)

    if (nearBorder(myPose) or minDist < DIST_THRS or rospy.Time.now() > state_change_time ):
      if (not force_fwd ) :
        # Stop moving forward and start turning around
        driving_forward = False
        # Change the direction of twisting
        twistFlag = 1 - twistFlag
      else : 
        force_fwd = False 

      if (minDist < DIST_THRS) :
        mutualAngl = myPose.theta - minAngl
        if (math.fabs(mutualAngl) < 2*PI/3) :
          if mutualAngl > 0 : 
            spin_angl = 2*PI/3 - mutualAngl
            twistFlag = 1
          else :
            spin_angl = 2*PI/3 + mutualAngl
            twistFlag = 0

        state_change_time = rospy.Time.now() + rospy.Duration(spin_angl/TWST_SPD)
        # Set the force_fwd flag so that the next state is forced to be 
        # moving forward. Otherwise the turtle would spin back and force
        force_fwd = True

      elif (nearBorder(myPose)) :  
        spin_angl = 2*PI/3; 
        state_change_time = rospy.Time.now() + rospy.Duration(spin_angl/TWST_SPD)
        force_fwd = True

      else :
        state_change_time = rospy.Time.now() + rospy.Duration(random.random()*PI/TWST_SPD)

  else: # not driving_forward
    # If it has been turning around for a relatively long time, then stop turning 
    if rospy.Time.now() > state_change_time:
      # Stop turning around and start moving forward 
      driving_forward = True 
      state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME)

  # Set the speeds for Twist 
  twist = Twist()
  if driving_forward :
    # Moving forward at speed 1
    twist.linear.x = FWD_SPD
  else:
    # Turning around at speed 1
    if twistFlag :
      twist.angular.z = TWST_SPD
    else : 
      twist.angular.z = -TWST_SPD

  cmd_vel_pub.publish(twist)
  rate.sleep()
