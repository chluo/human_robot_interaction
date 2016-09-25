#!/usr/bin/python 

import rospy 
import sys 

from basics.srv import WordCount 

# Node initialization 
rospy.init_node ( 'service_client' ) 

# A service client cannot use a certain service until the server advertises it 
rospy.wait_for_service ( 'word_count' ) 

# An object of rospy.ServiceProxy is like a function object 
# that takes the input arguments we defined in the .srv file 
word_counter = rospy.ServiceProxy ( 'word_count', WordCount ) 

# Get words to be processed by the server from the command line arguments 
# Use a white space to join the command line arguments
words = ' '.join ( sys.argv[1:] ) 

# Use the function object 
# It "returns" a WordCountResponse type object
word_count = word_counter ( words ) 

# Print the result got from the server 
print words, ' -> ', word_count.count 
