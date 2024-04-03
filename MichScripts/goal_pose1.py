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

#  x: 0.08014566718819073
#       y: -0.09953355145107484
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.9980145664399961
#       w: 0.06298353097109248


rospy.loginfo("moving to point 1 \n")
moveToPose(0.08014566718819073, -0.09953355145107484, 0, 0, 0, -0.9980145664399961, 0.06298353097109248)
rospy.loginfo("successfully moved to point 1 \n")


# x: -6.272309294072849
#       y: 0.23757609709749788
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.9451734845464723
#       w: 0.3265686514506244

# change this all the way to the end  and use it for the rest of them
rospy.loginfo("moving to point 2 \n")
moveToPose( -6.272309294072849, 0.23757609709749788, 0, 0, 0, -0.9451734845464723, 0.3265686514506244)
rospy.loginfo("successfully moved to point 2 \n")

# x: -6.090844613038354
#       y: -6.280478684444017
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.36331253664424756
#       w: 0.9316673229845095


rospy.loginfo("moving to point 3 \n")
moveToPose( -6.090844613038354, -6.280478684444017, 0, 0, 0, -0.36331253664424756, 0.9316673229845095)
rospy.loginfo("successfully moved to point 3 \n")


#  x: -1.8576737478583556
#       y: -6.230285188192806
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: 0.10208323389408128
#       w: 0.994775860864007

rospy.loginfo("moving to point 4 \n")
moveToPose( -1.8576737478583556, -6.230285188192806, 0, 0, 0, 0.10208323389408128, 0.994775860864007)
rospy.loginfo("successfully moved to point 4 \n")

# x: 0.11018908948006703
#       y: -6.488492751542908
#       z: 0.0
#     orientation: 
#       x: 0.0
#       y: 0.0
#       z: -0.1058843541123644
#       w: 0.994378450869792

rospy.loginfo("moving to point 5 \n")
moveToPose( 0.11018908948006703, -6.488492751542908, 0, 0, 0, -0.1058843541123644, 0.994378450869792)
rospy.loginfo("successfully moved to point 5 \n")




if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())