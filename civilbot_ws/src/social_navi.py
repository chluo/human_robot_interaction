#!/usr/bin/python

import math 
import random
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color
from turtlesim.msg import Pose

# Constants
PI        = 3.1415927
DIST_THRS = 1.5
FWD_TIME  = 2
TWST_TIME = 0.5
FWD_SPD   = 0.8
TWST_SPD  = 1

myPose   = Pose()
distList = [10, 10, 10, 10, 10, 10, 10, 10, 10]
anglList = [0, 0, 0, 0, 0, 0, 0, 0, 0] 
# Min distance
minDist  = 20 
# Angle corresponding to the min distance
minAngl  = 0

# Misc calculation functions 
def rmTwoPI (ang): 
  ang_res = ang
  while (math.fabs(ang_res) > PI): 
    if (ang_res < 0): 
      ang_res = ang_res + 2* PI 
    else: 
      ang_res = ang_res - 2* PI 
  return ang_res 
      
def nearBorder(p): 
  if ( p.x < 0.5 ) :
    return 1 # left
  if ( p.y < 0.5 ) :
    return 2 # down
  if ( p.x > 10.5 ) :
    return 3 # right
  if ( p.y > 10.5 ) :
    return 4 # up

  return 0

def calcAngl(p1, p2): 
  dy = p1.y - p2.y 
  dx = p1.x = p2.x
  return math.atan2(dy, dx)

def calcDist(p1, p2): 
  tx =  math.pow((p1.x - p2.x), 2)
  ty =  math.pow((p1.y - p2.y), 2)
  return math.sqrt(tx + ty)

# Subscriber call-back functions 
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

# Turtle position subscribers 
poseA_sub = rospy.Subscriber('poseA', Pose, poseA_cb)
poseB_sub = rospy.Subscriber('poseB', Pose, poseB_cb)
poseD_sub = rospy.Subscriber('poseD', Pose, poseD_cb)
poseF_sub = rospy.Subscriber('poseF', Pose, poseF_cb)
poseH_sub = rospy.Subscriber('poseH', Pose, poseH_cb)
# poseC_sub = rospy.Subscriber('poseC', Pose, poseC_cb)
# poseE_sub = rospy.Subscriber('poseE', Pose, poseE_cb)
# poseG_sub = rospy.Subscriber('poseG', Pose, poseG_cb)
# poseI_sub = rospy.Subscriber('poseI', Pose, poseI_cb)
# poseT_sub = rospy.Subscriber('poseT', Pose, poseT_cb)

rospy.init_node('social_navi')
state_change_time = rospy.Time.now() + rospy.Duration(2)
rate = rospy.Rate(10)
driving_forward = True
twistFlag = 0
force_fwd_border = False
force_fwd_collis = False
state_time_ovrid = False

while not rospy.is_shutdown():
  # State transition between moving forward and turning around
  if driving_forward :
    # If there is some obstacles closly ahead, or it has been moving 
    # forward for a relatively long time, then stop moving forward
    print "[Merry Dol!] Minimum distance: " + str(minDist)

    collideBorder = nearBorder(myPose) 
    collideOthers = minDist < DIST_THRS 
    timeExceedLmt = rospy.Time.now() > state_change_time

    if ( collideBorder or collideOthers or timeExceedLmt ):

      if ( force_fwd_border and collideBorder and not (collideOthers or timeExceedLmt) ) :
        force_fwd_border = False
        state_time_ovrid = True
        state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME/20)
      elif ( force_fwd_collis and collideOthers and not (collideBorder or timeExceedLmt) ) : 
        force_fwd_collis = False 
        state_time_ovrid = True
        state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME/10)
      else : 
        force_fwd_border = False
        force_fwd_collis = False 
        state_time_ovrid = False
        # Stop moving forward and start turning around
        driving_forward = False
        # Change the direction of twisting
        twistFlag = 1 - twistFlag

      if (collideOthers) :
        # mutualAngl = rmTwoPI(myPose.theta - minAngl)
        # if (math.fabs(mutualAngl) < 3*PI/4) :
        #   if mutualAngl > 0 : 
        #     spin_angl = rmTwoPI(3*PI/4 - mutualAngl)
        #     twistFlag = 1
        #   else :
        #     spin_angl = rmTwoPI(3*PI/4 + mutualAngl)
        #     twistFlag = 0
        # else: 
        #   spin_angl = 0 
        # Simply turn around 
        spin_angl = PI

        if ( not state_time_ovrid ) :
          state_change_time = rospy.Time.now() + rospy.Duration(math.fabs(spin_angl)/TWST_SPD)

        # Set the force_fwd flag so that the next state is forced to be 
        # moving forward. Otherwise the turtle would spin back and force
        force_fwd_collis = True

      elif (collideBorder) :  
        # Reflect on border
        if (collideBorder == 1): # Left
          # Check if the turtle is heading toward the border 
          # If so, reflect
          # Otherwise, keep going 
          if (math.fabs(rmTwoPI(myPose.theta)) > PI/2):
            spin_angl = rmTwoPI(PI - myPose.theta - myPose.theta) 
          else: 
            spin_angl = 0
        if (collideBorder == 2): # Down
          if (rmTwoPI(myPose.theta) < 0):
            spin_angl = rmTwoPI(0 - myPose.theta - myPose.theta) 
          else: 
            spin_angl = 0
        if (collideBorder == 3): # Right
          if (math.fabs(rmTwoPI(myPose.theta)) < PI/2):
            spin_angl = rmTwoPI(PI - myPose.theta - myPose.theta) 
          else: 
            spin_angl = 0
        if (collideBorder == 4): # Up
          if (rmTwoPI(myPose.theta) > 0):
            spin_angl = rmTwoPI(0 - myPose.theta - myPose.theta) 
          else: 
            spin_angl = 0

        if (spin_angl > 0): 
          twistFlag = 1
        else:
          twistFlag = 0 

        if ( not state_time_ovrid ) :
          state_change_time = rospy.Time.now() + rospy.Duration(math.fabs(spin_angl)/TWST_SPD)
        force_fwd_border = True

      else :
        if ( not state_time_ovrid ) :
          state_change_time = rospy.Time.now() + rospy.Duration(random.random()*PI/2/TWST_SPD)

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
