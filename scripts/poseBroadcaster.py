#!/usr/bin/env python
import rospy
import os, random
from geometry_msgs.msg import PoseStamped

def pose_broadcaster():
    pub = rospy.Publisher('poseBroadcaster', PoseStamped, queue_size=2)
    rospy.init_node('poseBroadcaster', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        current_pose = PoseStamped()
        current_pose.header.frame_id = os.environ['ROS_HOSTNAME'] #str(random.randint(0,2)) #SIM MODE
        now = rospy.get_rostime()
        current_pose.header.stamp = rospy.get_rostime()
        current_pose.pose.position.x = random.uniform(-4.5, 4.9)
        current_pose.pose.position.y = random.uniform(-4.5, 4.9)
        current_pose.pose.position.z = random.uniform(-4.5, 4.9)
        current_pose.pose.orientation.x = random.uniform(-1.5, 1.9)
        current_pose.pose.orientation.y = random.uniform(-1.5, 1.9)
        current_pose.pose.orientation.z = random.uniform(-1.5, 1.9)
        current_pose.pose.orientation.w = random.uniform(-1.5, 1.9)
        rospy.loginfo(current_pose)
        pub.publish(current_pose)
        rate.sleep()

if __name__ == '__main__':
    try:
        pose_broadcaster()
    except rospy.ROSInterruptException:
        pass
