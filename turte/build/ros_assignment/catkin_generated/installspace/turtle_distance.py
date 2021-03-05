import rospy
from turtlesim.msg import Pose
from std_msgs.msg import String
from math import sqrt
from threading import Thread, Lock

prev_x = 0.0
prev_y = 0.0
total_distance = 0.0

# Euclidean distance
def calculate_distance(p1_x, p1_y, p2_x ,p2_y):
    return sqrt((p1_x - p2_x) **2  + (p1_y - p2_y)**2)

def poseCallBack(msg, publisher):
    #rospy.loginfo("turtle pose: x:%06f, y:%0.6f",msg.x , msg.y)
    global prev_x
    global prev_y
    global total_distance
    step = calculate_distance(prev_x, prev_y, msg.x, msg.y)
    total_distance += step
    prev_x = msg.x
    prev_y = msg.y

    #publish distance
    publish_msg = "Total distance %s" % total_distance
    rospy.loginfo(publish_msg)
    publisher.publish(publish_msg)

def subscriber():
    rospy.init_node('turtle_subscriber', anonymous=True)

    publisher = rospy.Publisher('turtle_publisher', String, queue_size=10)

    rospy.Subscriber('/turtle1/pose', Pose, poseCallBack, publisher)

    rospy.spin()

    # print
    print('Total travelled distance', total_distance)

if __name__ == '__main__':
    subscriber()
