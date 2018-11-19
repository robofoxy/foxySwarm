#!/usr/bin/env python
import rospy, random, os, curses
from multimaster_msgs_fkie.msg import LinkStatesStamped
from foxySwarm.msg import TrajectoryPolynomialPiece
from std_msgs.msg import String

links = list()
stats = {}

def links_callback(link_states):
	global links
	links = link_states.links
	
def statsCallBack(status):
	global stats
	stats[status.data] = True


def genStatus(status):
	if status:
		return ' ' * 6 + "OK" + ' ' * 7
	else:
		return ' ' * 6 + "NA" + ' ' * 7
	

def print_link_status(scr, i, host_name, status):
	global stats, links
	for j in range(len(links)):
		if not(links[j].destination in stats):
			stats[links[j].destination] = False
	
	if status:
		color = curses.color_pair(77)
	else:
		color = curses.color_pair(125)
	
	scr.addstr(i,0,"#|    {0}{1}||".format(host_name, ' '*(16-len(host_name))))
	scr.addstr(i,24,"{0}".format(genStatus(status)), color)
	scr.addstr(i,40,"|#")

def print_dict(scr):
	scr.addstr(0,0,"##########################################")
	scr.addstr(1,0,"#######     FOXY_SWARM NETWORK     #######")
	scr.addstr(2,0,"##########################################")
	scr.addstr(3,0,"#|    ROS_HOSTNAME    ||     STATUS     |#")
	scr.addstr(4,0,"#|--------------------------------------|#")
	if len(stats) > 0:
		i = 5
		for host_name, status in stats.items():
			print_link_status(scr, i, host_name, status)
			i += 1
		scr.addstr(i,0,"#|--------------------------------------|#")
		scr.addstr(i+1,0,"##########################################")
		scr.refresh()


	
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
	rospy.Subscriber('/trjFeedBack', String, statsCallBack)
	trj_publisher = rospy.Publisher('trajectoryPublisher', TrajectoryPolynomialPiece, queue_size=30)
	scr = curses.initscr()
	curses.start_color()
	curses.use_default_colors()
	for i in range(0, curses.COLORS):
		curses.init_pair(i + 1, i, -1)
		
	while not rospy.is_shutdown():
		if not published:
			for i in range(len(links)):
				if links[i].destination != os.environ['ROS_HOSTNAME']:
					trj_publisher.publish(create_fake_trj(links[i].destination))
					published = True
		print_dict(scr)
		rospy.sleep(0.4)
	
if __name__ == '__main__':
	try:
		RR()
	except rospy.ROSInterruptException:
		pass
