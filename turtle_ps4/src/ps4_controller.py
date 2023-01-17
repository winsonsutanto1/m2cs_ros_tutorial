#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from std_srvs.srv import Empty
from Ps4Data.msg import Ps4Data

# hint: some imports are missing

old_data = Ps4Data()

def callback(data):
    global old_data
    
    # you should publish the velocity here!
    velocity = Twist()
    aggressiveness = [1,1.2,1.4,1.6,1.8]
    currentAggressiveness = 0
    
    velocity.angular.z = aggressiveness[currentAggressiveness] * data.hat_rx
    velocity.linear.x = aggressiveness[currentAggressiveness] * data.hat_lx
    
    pub.publish(velocity)
    # hint: to detect a button being pressed, you can use the following pseudocode:
    # 
    # if ((data.button is pressed) and (old_data.button not pressed)),
    
    
    #change aggresiveness
    if (data.dpad_y == -1 and data.dpad_y == 0):
        if currentAggressiveness == 0:
            currentAggresiveness = 0
        else:
            currentAggressiveness -= 1
    
    if (data.dpad_y == 1 and data.dpad_y == 0):
        if currentAggressiveness == 4:
            currentAggresiveness = 4
        else:
            currentAggressiveness += 1
    #clear if ps button pressed
    if (data.ps == true and old_data.ps == false):
    	srv_clear()
    
    #change color when shape buttons pressed
    if (data.triangle == true and old_data.triangle == false):
        srv_col((0,255,0))
        
    if (data.circle == true and old_data.circle == false):
        srv_col((255,0,0))
        
    if (data.cross == true and old_data.cross == false):
        srv_col((0,0,255))
        
    if (data.square == true and old_data.square == false):
        srv_col((128,0,128))
    
    
    
    old_data = data

if __name__ == '__main__':
    rospy.init_node('ps4_controller')
    
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size = 1)# publisher object goes here... hint: the topic type is Twist
    sub = rospy.Subscriber('/input/ps4_data',Ps4Data,callback)# subscriber object goes here
    
    # one service object is needed for each service called!
    srv_col = rospy.ServiceProxy('/turtle1/set_pen',SetPen)# service client object goes here... hint: the srv type is SetPen
    srv_clear = rospy.ServiceProxy('/clear',Empty)
    # fill in the other service client object...
    
    rospy.spin()
