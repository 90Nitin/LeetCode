__author__ = 'nsrivas3'

import math
import time

# 1. We need a guess of initial point of rob
# 2. We need a guess of spaces assumed between the houses to rob
# 3. Problem - we cant assume that we shall maintain a fixed distance between the houses

def rob(nums):
    totalHouse = nums.__len__()
    # The maximum number of houses to be stolen from given a list
    maxnumRob = math.ceil(totalHouse/2)
    copyRob = sorted(nums, reverse = True)
    print(nums)
    print(copyRob)
    idxRob = []
    for i in copyRob:
        idxRob.append(nums.index(i))
    print(idxRob)
    # To store the amount of Rob in a sequence
    robAmnt = 0


# def RecRob(listHouse,firstRob):
#     # To calculate the maximum Rob amount with a starting house
#
#
#
#
#     return(RobTotal)





# Test Cases
start = time.time()
print(rob([12,3,4,5,0,7,5]))
stop = time.time()
print(start-stop)