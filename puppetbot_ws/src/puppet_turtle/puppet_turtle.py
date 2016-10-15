#!/usr/bin/python

import math 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color
from turtlesim.msg import Pose
from hlpr_speech_msgs.msg import StampedString

# Constants
PI        = 3.1415927
WALK_SPD  = 0.8
RUSH_SPD  = 1.0
TWST_SPD  = 1.0

# Global state variables 
######################################################################
# ------------------------ STATE LIST ------------------------------ # 
# IDLE : Stay still
# WALK : Walk ahead
# RUSH : Rush ahead
# ROAM : Move ahead at a tuned speed
# LEFT : Turn left, back to IDLE after finished 
# ARND : Turn back, back to IDLE after finished
# RGHT : Turn right, back to IDLE after finished
# TURN : Keep turning, until a stop signal is received
# ------------------------------------------------------------------ # 
######################################################################
CurState = 'IDLE'
NxtState = 'IDLE'

# Global control variables
TunedSpd = 0.8              # Tuned speed applied in state ROAM
ExitTime = rospy.Time.now() # LEFT/RGHT/ARND timer 

# Speech command subscriber call-back function 
def StateTrans (msg) : 
  global CurState
  global NxtState

  if   (msg.keyphrase == 'WALK AHEAD'  ) : 
    if (CurState == 'IDLE') : 
      NxtState = 'WALK' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'RUSH AHEAD'  ) : 
    if (CurState == 'IDLE') : 
      NxtState = 'RUSH' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'SPEED UP'    ) : 
    if (CurState == 'WALK' or CurState == 'RUSH') : 
      NxtState = 'ROAM' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'SLOW DOWN'   ) : 
    if (CurState == 'WALK' or CurState == 'RUSH') : 
      NxtState = 'ROAM' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'STOP'        ) : 
    if (CurState != 'LEFT' and CurState != 'ARND' and CurState != 'RGHT') : 
      NxtState = 'IDLE'
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'TURN LEFT'   ) : 
    if (CurState == 'IDLE' or CurState == 'WALK' or CurState == 'RUSH' or CurState == 'ROAM') : 
      NxtState = 'LEFT'
    else : 
      NxtState = CurState 

  elif (msg.keyphrase == 'TURN RIGHT'  ) : 
    if (CurState == 'IDLE' or CurState == 'WALK' or CurState == 'RUSH' or CurState == 'ROAM') : 
      NxtState = 'RGHT'
    else : 
      NxtState = CurState 

  elif (msg.keyphrase == 'TURN AROUND' ) : 
    if (CurState == 'IDLE' or CurState == 'WALK' or CurState == 'RUSH' or CurState == 'ROAM') : 
      NxtState = 'ARND'
    else : 
      NxtState = CurState 

  elif (msg.keyphrase == 'KEEP TURNING') : 
    NxtState = 'TURN' 

  else : 
    NxtState = 'IDLE' 
  

# Motion control publisher
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

# Speech command subscriber 
hlpr_speech_sub = rospy.Subscriber('hlpr_speech_commands', StampedString, StateTrans)

# Node initialization
rospy.init_node('puppet_turtle')

# State change rate
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  # State transition 
  CurState = NxtState 

  # LEFT/RGHT/ARND state transition  
  if   (CurState == 'LEFT' or CurState == 'RGHT') : 
    ExitTime = rospy.Time.now() + rospy.Duration(PI/2/TWST_SPD)
  elif (CurState == 'ARND') : 
    ExitTime = rospy.Time.now() + rospy.Duration(PI/TWST_SPD)
  else : 
    ExitTime = rospy.Time.now()

  if ((CurState == 'LEFT' or CurState == 'RGHT' or CurState == 'ARND') and rospy.Time.now() > ExitTime) : 
    CurState = 'IDLE'

  # TODO Speed tuning for ROAM

  # Create a new Twist 
  twist = Twist()

  # Set the speed 
  if   (CurState == 'IDLE') : 
    twist.linear.x  = 0
    twist.angular.z = 0

  elif (CurState == 'WALK') :
    twist.linear.x  = WALK_SPD
    twist.angular.z = 0

  elif (CurState == 'RUSH') :
    twist.linear.x  = RUSH_SPD
    twist.angular.z = 0

  elif (CurState == 'ROAM') :
    twist.linear.x  = TunedSpd
    twist.angular.z = 0

  elif (CurState == 'LEFT') :
    twist.linear.x  = 0
    twist.angular.z = TWST_SPD

  elif (CurState == 'ARND') :
    twist.linear.x  = 0
    twist.angular.z = TWST_SPD

  elif (CurState == 'RGHT') :
    twist.linear.x  = 0
    twist.angular.z = -TWST_SPD

  elif (CurState == 'TURN') :
    twist.linear.x  = 0
    twist.angular.z = TWST_SPD

  else : 
    twist.linear.x  = 0
    twist.angular.z = 0

  # Publish the speed 
  cmd_vel_pub.publish(twist)

  # Wait for the next clock cycle 
  rate.sleep()

# # State transition between moving forward and turning around
# if driving_forward :
#   # If there is some obstacles closly ahead, or it has been moving 
#   # forward for a relatively long time, then stop moving forward
#   print "[Merry Dol!] Minimum distance: " + str(minDist)

#   collideBorder = nearBorder(myPose) 
#   collideOthers = minDist < DIST_THRS 
#   timeExceedLmt = rospy.Time.now() > state_change_time

#   if ( collideBorder or collideOthers or timeExceedLmt ):

#     if ( force_fwd_border and collideBorder and not (collideOthers or timeExceedLmt) ) :
#       force_fwd_border = False
#       state_time_ovrid = True
#       state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME/20)
#     elif ( force_fwd_collis and collideOthers and not (collideBorder or timeExceedLmt) ) : 
#       force_fwd_collis = False 
#       state_time_ovrid = True
#       state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME/10)
#     else : 
#       force_fwd_border = False
#       force_fwd_collis = False 
#       state_time_ovrid = False
#       # Stop moving forward and start turning around
#       driving_forward = False
#       # Change the direction of twisting
#       twistFlag = 1 - twistFlag

#     if (collideOthers) :
#       # mutualAngl = rmTwoPI(myPose.theta - minAngl)
#       # if (math.fabs(mutualAngl) < 3*PI/4) :
#       #   if mutualAngl > 0 : 
#       #     spin_angl = rmTwoPI(3*PI/4 - mutualAngl)
#       #     twistFlag = 1
#       #   else :
#       #     spin_angl = rmTwoPI(3*PI/4 + mutualAngl)
#       #     twistFlag = 0
#       # else: 
#       #   spin_angl = 0 
#       # Simply turn around 
#       spin_angl = PI

#       if ( not state_time_ovrid ) :
#         state_change_time = rospy.Time.now() + rospy.Duration(math.fabs(spin_angl)/TWST_SPD)

#       # Set the force_fwd flag so that the next state is forced to be 
#       # moving forward. Otherwise the turtle would spin back and force
#       force_fwd_collis = True

#     elif (collideBorder) :  
#       # Reflect on border
#       if (collideBorder == 1): # Left
#         # Check if the turtle is heading toward the border 
#         # If so, reflect
#         # Otherwise, keep going 
#         if (math.fabs(rmTwoPI(myPose.theta)) > PI/2):
#           spin_angl = rmTwoPI(PI - myPose.theta - myPose.theta) 
#         else: 
#           spin_angl = 0
#       if (collideBorder == 2): # Down
#         if (rmTwoPI(myPose.theta) < 0):
#           spin_angl = rmTwoPI(0 - myPose.theta - myPose.theta) 
#         else: 
#           spin_angl = 0
#       if (collideBorder == 3): # Right
#         if (math.fabs(rmTwoPI(myPose.theta)) < PI/2):
#           spin_angl = rmTwoPI(PI - myPose.theta - myPose.theta) 
#         else: 
#           spin_angl = 0
#       if (collideBorder == 4): # Up
#         if (rmTwoPI(myPose.theta) > 0):
#           spin_angl = rmTwoPI(0 - myPose.theta - myPose.theta) 
#         else: 
#           spin_angl = 0

#       if (spin_angl > 0): 
#         twistFlag = 1
#       else:
#         twistFlag = 0 

#       if ( not state_time_ovrid ) :
#         state_change_time = rospy.Time.now() + rospy.Duration(math.fabs(spin_angl)/TWST_SPD)
#       force_fwd_border = True

#     else :
#       if ( not state_time_ovrid ) :
#         state_change_time = rospy.Time.now() + rospy.Duration(random.random()*PI/2/TWST_SPD)

# else: # not driving_forward
#   # If it has been turning around for a relatively long time, then stop turning 
#   if rospy.Time.now() > state_change_time:
#     # Stop turning around and start moving forward 
#     driving_forward = True 
#     state_change_time = rospy.Time.now() + rospy.Duration(FWD_TIME)
