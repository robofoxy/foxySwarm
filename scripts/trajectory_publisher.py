#!/usr/bin/env python
import rospy
from multimaster_msgs_fkie.msg import LinkStatesStamped
from multimaster_msgs_fkie.msg import LinkState
from msg/foxySwarm.msg import TrajectoryPolynomialPiece

links = list()

def links_callback(link_states):
	global links
	links = link_states.links

def print_links():
	print "----------------------------"
	for i in range(0, len(links)):
		print links[i].destination
	
def RR():
	rospy.init_node('linksSubscriber', anonymous=True)
	rospy.Subscriber('/master_discovery/linkstats', LinkStatesStamped, links_callback)
	rospy.Publisher('trajectoryPublisher', TrajectoryPolynomialPiece, queue_size=30)
	
	while not rospy.is_shutdown():
		print_links()
		rospy.sleep(0.4)

	
if __name__ == '__main__':
	try:
		RR()
		
	except rospy.ROSInterruptException:
		pass
