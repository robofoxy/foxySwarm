#!/usr/bin/env python
import rospy
import os
from multimaster_msgs_fkie.msg import LinkStatesStamped
from foxySwarm.msg import TrajectoryPolynomialPiece

trajectory = TrajectoryPolynomialPiece()

def trajectory_callback(trj):
	global trajectory
	print trj.destination
	if trj.destination == os.environ['ROS_HOSTNAME']:
		trajectory = trj
	
def print_trj():
	for i in range(len(trajectory.poly_x)):
		print "################################"
		print "dest:", trajectory.destination
		print "pol_x [", i, "] =", trajectory.poly_x[i]
		print "pol_y [", i, "] =", trajectory.poly_y[i]
		print "pol_z [", i, "] =", trajectory.poly_z[i]
		print "pol_yaw [", i, "] =",trajectory.poly_yaw[i]
		print "duration =", trajectory.duration
	
def RR():
	rospy.init_node('droneCore', anonymous=True)
	rospy.Subscriber('/trajectoryPublisher', TrajectoryPolynomialPiece, trajectory_callback)
	
	while not rospy.is_shutdown():
		print_trj()
		rospy.sleep(0.4)
	
if __name__ == '__main__':
	try:
		RR()
	except rospy.ROSInterruptException:
		pass
