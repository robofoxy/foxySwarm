#!/usr/bin/env python
import rospy, random, os
from multimaster_msgs_fkie.msg import LinkStatesStamped
from foxySwarm.msg import TrajectoryPolynomialPiece

links = list()

def links_callback(link_states):
	global links
	links = link_states.links

def print_links():
	print "----------------------------"
	for i in range(0, len(links)):
		print links[i].destination
	
def create_fake_trj(dest):
	msg = TrajectoryPolynomialPiece()
	msg.destination = dest
	for i in range(1000):
		msg.poly_x.append(random.uniform(-4.5, 4.9))
		msg.poly_y.append(random.uniform(-4.5, 4.9))
		msg.poly_z.append(random.uniform(-4.5, 4.9))
		msg.poly_yaw.append(random.uniform(-1, 1))
		msg.duration = rospy.Duration(10, 0)
	return msg
	
def RR():
	rospy.init_node('trajectoryPublisher', anonymous=True)
	rospy.Subscriber('/master_discovery/linkstats', LinkStatesStamped, links_callback)
	trj_publisher = rospy.Publisher('trajectoryPublisher', TrajectoryPolynomialPiece, queue_size=30)
	
	while not rospy.is_shutdown():
		for i in range(len(links)):
			if links[i].destination != os.environ['ROS_HOSTNAME']:
				trj_publisher.publish(create_fake_trj(links[i].destination))
		print_links()
		rospy.sleep(0.4)
	
if __name__ == '__main__':
	try:
		RR()
	except rospy.ROSInterruptException:
		pass
