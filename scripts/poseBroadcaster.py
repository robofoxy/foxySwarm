#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

def talker():
    pub = rospy.Publisher('poseBroadcaster', Pose, queue_size=2)
    rospy.init_node('poseBroadcaster', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        current_pose = PoseStamped()

		current_pose.header.frame_id = "rasp1"
		current_pose.pose.position.x = 4.56123
		current_pose.pose.position.y = 7.98327
		current_pose.pose.position.z = 1.56445
		current_pose.pose.orientation.x = 0.94988
		current_pose.pose.orientation.y = 0.18811
		current_pose.pose.orientation.z = 0.19811
		current_pose.pose.orientation.w = 0.13872
		
		rospy.loginfo(current_pose)
        pub.publish(current_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
