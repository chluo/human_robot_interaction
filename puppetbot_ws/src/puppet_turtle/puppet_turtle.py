#!/usr/bin/python

import math 
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Color
from turtlesim.msg import Pose
from hlpr_speech_msgs.msg import StampedString

######################################################################
# ------------------------------------------------------------------ #
# Puppet Turtle Motion Control Node 
# 
#                       ---------------
#  Speech commands ---> | Motion Ctrl | ---> Turtle motion signals
#                       ---------------
# 
# Author         Chunheng Luo
# ------------------------------------------------------------------ #
######################################################################

# Constants
PI        = 3.1415927
WALK_SPD  = 0.7          # Moving speed in WALK state
RUSH_SPD  = 1.2          # Moving speed in RUSH state 
TWST_SPD  = 1.0          # Turning speed 

# Node initialization
rospy.init_node('puppet_turtle')

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
SpeedInc = 0                # Speed change on SPEED_UP/SLOW_DOWN command

# Speech command subscriber call-back function 
def StateTrans (msg) : 
  global CurState
  global NxtState
  global SpeedInc
  global SpeedDec

  if   (msg.keyphrase == 'WALK AHEAD'  ) : 
    if (CurState != 'WALK') : 
      NxtState = 'WALK' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'RUSH AHEAD'  ) : 
    if (CurState != 'RUSH') : 
      NxtState = 'RUSH' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'SPEED UP'    ) : 
    SpeedInc = 0.1
    if (CurState == 'WALK' or CurState == 'RUSH') : 
      NxtState = 'ROAM' 
    else : 
      NxtState = CurState

  elif (msg.keyphrase == 'SLOW DOWN'   ) : 
    SpeedInc = -0.1
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

# State change rate
rate = rospy.Rate(10)

while not rospy.is_shutdown():
  # State transition 
  PreState = CurState
  CurState = NxtState 

  # LEFT/RGHT/ARND state transition  
  if   ((CurState == 'LEFT' and PreState != 'LEFT') or (CurState == 'RGHT' and PreState != 'RGHT')) : 
    ExitTime = rospy.Time.now() + rospy.Duration(PI/2/TWST_SPD)
  elif (CurState == 'ARND' and PreState != 'ARND') : 
    ExitTime = rospy.Time.now() + rospy.Duration(PI/TWST_SPD)

  if ((CurState == 'LEFT' or CurState == 'RGHT' or CurState == 'ARND') and rospy.Time.now() > ExitTime) : 
    CurState = 'IDLE'
    NxtState = 'IDLE'

  # Speed tuning for ROAM
  if (CurState == 'ROAM') : 
    if   (PreState == 'WALK') : 
      TunedSpd = WALK_SPD + SpeedInc 
    elif (PreState == 'RUSH') : 
      TunedSpd = RUSH_SPD + SpeedInc 
    elif (PreState == 'ROAM') : 
      # Set low/high speed limit 
      if (not ((TunedSpd > 2 and SpeedInc > 0) or (TunedSpd < 0.5 and SpeedInc < 0))) : 
        TunedSpd = TunedSpd + SpeedInc

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

