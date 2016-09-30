#!/usr/bin/python

import sys
import rospy
from turtlesim.srv import Spawn

#---------------------------------------------------------------------- 
# Comments on Turtlesim Canvas: 
# PosX : 0 ~ 11
# PosY : 0 ~ 11
# Theta: (---> 0 rad) (<--- pi rad) 
#---------------------------------------------------------------------- 

PI = 3.1415927

rospy.init_node('spawn_turtles') 
rospy.wait_for_service('spawn') 

TurtleSpawn = rospy.ServiceProxy('spawn', Spawn)

Turtles = { \
  'Alex'    : [0.5, 0.5, PI/4], \
  'Bob'     : [8, 8, PI/4    ], \
# 'Charlie' : [5.5, 8, 0     ], \
  'Deb'     : [3, 8, PI/4    ], \
# 'Emma'    : [3, 5.5, 0     ], \
  'Frank'   : [3, 3, PI/4    ], \
# 'George'  : [5.5, 3, 0     ], \
  'Hellen'  : [8, 3, PI/4    ]  \
# 'Isac'    : [8, 5.5, 0     ]  \
}

for key, val in Turtles.items(): 
  TurtleName = TurtleSpawn(val[0], val[1], val[2], key) 

 

