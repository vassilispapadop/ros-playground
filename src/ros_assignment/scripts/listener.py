import rospy
from turtlesim.msg import Pose
from math import sqrt

prev_x = 0.0
prev_y = 0.0

def calculate_distance(p1_x, p1_y, p2_x ,p2_y):
    return sqrt((p1_x - p2_x) **2  + (p1_y - p2_y)**2)

def poseCallBack(msg, dist):
    r#ospy.loginfo("turtle pose: x:%06f, y:%0.6f",msg.x , msg.y)
    step = calculate_distance(prev_x, prev_y, msg.x, msg.y)
    dist += step
    prev_x = msg.x
    prev_y = msg.y
    print("distance", dist)


def subscriber():
    total_distance = 0
    rospy.init_node('turtle_subscriber', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, poseCallBack, total_distance)

    rospy.spin()

    # print
    print('Total travelled distance', total_distance)

if __name__ == '__main__':
    subscriber()
