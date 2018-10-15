#!/usr/bin/env python
import rospy, sys, os, tf, curses, math
from geometry_msgs.msg import PoseStamped

pose_dictionary = {}

def pose_callback(poseStamped):
	pose_dictionary[poseStamped.header.frame_id] = poseStamped

def ln(num):
	return len(str(num))
	
def toStr(num):
	s = "%3.3f" % num
	if num <0:
		res =  " " + s
	else:
		res =  "  " + s
	
	return res + (11 - len(res)) * ' '
	
def print_pose(scr, key, i):
	poseStamped = pose_dictionary[key]
	frame = poseStamped.header.frame_id
	px = poseStamped.pose.position.x
	py = poseStamped.pose.position.y
	pz = poseStamped.pose.position.z
	quaternion = (poseStamped.pose.orientation.x, poseStamped.pose.orientation.y, poseStamped.pose.orientation.z, poseStamped.pose.orientation.w)
	euler = tf.transformations.euler_from_quaternion(quaternion)
	#ox = poseStamped.pose.orientation.x
	#oy = poseStamped.pose.orientation.y
	#oz = poseStamped.pose.orientation.z
	#ow = poseStamped.pose.orientation.w
	scr.addstr(i,0,"#|    {0}{1}||{2}|{3}|{4}|{5}|{6}|{7}|#".format(frame, ' '*(16-len(frame)), toStr(px), toStr(py), toStr(pz), toStr(euler[0]), toStr(euler[1]), toStr(euler[2])))


def print_dict(scr):
	scr.addstr(0,0,"#################################################################################################")
	scr.addstr(1,0,"#############                           FOXY_SWARM NETWORK                          #############")
	scr.addstr(2,0,"#################################################################################################")
	scr.addstr(3,0,"#|    ROS_HOSTNAME    ||     X     |     Y     |     Z     |   ROLL    |   PITCH   |    YAW    |#")
	scr.addstr(4,0,"#|---------------------------------------------------------------------------------------------|#")
	if len(pose_dictionary) > 0:
		i = 5
		for key, poseStamped in pose_dictionary.items():
			print_pose(scr, key, i)
			i += 1
		scr.addstr(i,0,"#|---------------------------------------------------------------------------------------------|#")
		scr.addstr(i+1,0,"#################################################################################################")
		scr.refresh()

def pose_subscriber():
	rospy.init_node('poseSubscriber', anonymous=True)
	rospy.Subscriber('poseBroadcaster', PoseStamped, pose_callback)
	scr = curses.initscr()
	curses.noecho()
	curses.cbreak()	
	while not rospy.is_shutdown():
		print_dict(scr)
		rospy.sleep(0.4)

if __name__ == '__main__':
	try:
		pose_subscriber()
	except rospy.ROSInterruptException:
		pass
