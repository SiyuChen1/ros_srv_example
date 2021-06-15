#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from blend_trajectory.srv import MulThreeInts

def multi_three_ints_client(a, b, c):
    rospy.wait_for_service('multi_three_ints')
    try:
        multi_three_ints = rospy.ServiceProxy('multi_three_ints', MulThreeInts)
        print(type(multi_three_ints))
        resp1 = multi_three_ints(a, b, c)
        print(type(resp1))
        return resp1.res
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [a b c]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s * %s * %s"%(a, b, c))
    print("%s * %s * %s = %s"%(a, b, c, multi_three_ints_client(a, b, c)))