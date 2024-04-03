#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal



# Callbacks definition

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    # rospy.loginfo("Current location: "+str(feedback))
    pass


def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('goal_pose')



def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    global navclient
    global finished
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()


# position: 
#       x: -0.06696480288532558
#       y: -0.09883931182945492
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: 0.9994887389554521
#       w: 0.031972811906996405



rospy.loginfo("moving to point 10 \n")
moveToPose( -0.06696480288532558, -0.09883931182945492, 0, 0, 0, 0.9994887389554521, 0.031972811906996405)
rospy.loginfo("successfully moved to point 10 \n")


# position: 
#       x: -4.2165744005579935
#       y: -0.06083301549222669
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.9999243574253511
#       w: 0.012299570216010598

rospy.loginfo("moving to point 11 \n")
moveToPose( -4.2165744005579935, -0.06083301549222669, 0, 0, 0, -0.9999243574253511, 0.012299570216010598)
rospy.loginfo("successfully moved to point 11 \n")



#  x: -7.40637581128899
#       y: 0.052670496913996716
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: 0.9279895578821173
#       w: 0.37260620024598684


rospy.loginfo("moving to point 12 \n")
moveToPose( -7.40637581128899, 0.052670496913996716, 0, 0, 0, 0.9279895578821173, 0.37260620024598684)
rospy.loginfo("successfully moved to point 12 \n")



# x: -8.376734559152952
#       y: -3.0508130138263327
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: 0.6138156477872668
#       w: 0.7894493970682972


rospy.loginfo("moving to point 13 \n")
moveToPose( -8.376734559152952, -3.0508130138263327, 0, 0, 0, 0.6138156477872668, 0.7894493970682972)
rospy.loginfo("successfully moved to point 13 \n")



#    x: -11.301963044177784
#       y: -4.429917552650054
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.9998258488895035
#       w: 0.01866204416412427

rospy.loginfo("moving to point 14 \n")
moveToPose(-11.301963044177784, -4.429917552650054, 0, 0, 0, -0.9998258488895035, 0.01866204416412427)
rospy.loginfo("successfully moved to point 14 \n")





#  x: -11.05295852107006
#       y: 0.18878247703432893
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: 0.9594881217150687
#       w: 0.28174908036706975


rospy.loginfo("moving to point 16 \n")
moveToPose(-11.05295852107006, 0.18878247703432893, 0, 0, 0, 0.9594881217150687, 0.28174908036706975)
rospy.loginfo("successfully moved to point 6 \n")


if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())