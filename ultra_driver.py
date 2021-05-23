#!/usr/bin/env python

#self driving assignment_1
import rospy, math
from std_msgs.msg import Int32MultiArray


#variables for driving
FL=0
FM=0
FR=0
R=0
L=0
P_VAL=0#PID TUNE VALUE

def callback(msg):
   global FL
   global FM
   global FR
   global R
   global L
   FL=msg.data[0]
   FM=msg.data[1]
   FR=msg.data[2]
   R=msg.data[6]
   L=msg.data[7]
   print(msg.data)

def go_straight(P_VAL):
   angle = 0+P_VAL+(FR-FL)
   xycar_msg.data = [angle, 1000]
   

def turn_right():
   angle = 45
   xycar_msg.data = [angle, 1000]
def turn_left():
   angle = -450
   xycar_msg.data = [angle, 1000]

rospy.init_node('guide')
motor_pub = rospy.Publisher('xycar_motor_msg', Int32MultiArray, queue_size=1)
ultra_sub = rospy.Subscriber('ultrasonic', Int32MultiArray, callback)

xycar_msg = Int32MultiArray()


while not rospy.is_shutdown():
      P_VAL=2*(R-L)

      if FL<FR&FR>300:
         turn_right()
      elif FL>FR&FL>300:
         turn_left()
      else:
         angle=0
         go_straight(P_VAL)


      motor_pub.publish(xycar_msg)

