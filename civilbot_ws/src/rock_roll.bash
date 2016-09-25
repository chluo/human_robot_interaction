#!/bin/bash 

rosservice call reset
./spawn_turtles.py 
./social_navi.py \
  cmd_vel:=/Alex/cmd_vel \
  poseA:=/Alex/pose \
  poseB:=/Bob/pose \
  poseC:=/Charlie/pose \
  poseD:=/Deb/pose \
  poseE:=/Emma/pose \
  poseF:=/Frank/pose \
  poseG:=/George/pose \
  poseH:=/Hellen/pose \
  poseI:=/Isac/pose
