#!/bin/bash 

rosservice call reset

./spawn_turtles.py 
rosservice call kill turtle1
