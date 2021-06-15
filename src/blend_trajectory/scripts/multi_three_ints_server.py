#!/usr/bin/env python

from __future__ import print_function

from blend_trajectory.srv import MulThreeInts,MulThreeIntsResponse
import rospy

def handle_multi_three_ints(req):
    print("Returning [%s * %s * %s = %s]"%(req.a, req.b, req.c, (req.a * req.b * req.c)))
    return MulThreeIntsResponse(req.a * req.b * req.c)

def multi_three_ints_server():
    rospy.init_node('multi_three_ints_server')
    s = rospy.Service('multi_three_ints', MulThreeInts, handle_multi_three_ints)
    print("Ready to multi three ints.")
    rospy.spin()

if __name__ == "__main__":
    multi_three_ints_server()