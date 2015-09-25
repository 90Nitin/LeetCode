__author__ = 'nsrivas3'

import time
import math

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        k = abs(k)
        k = min(nums.__len__()-1,k)
        print("Init K: "+str(k))
        if nums.__len__()==0: return(False)
        if k==0: return(False)
        else:
            i = 0
            j = k
            while(i<nums.__len__()-k):
                while(j!=i):
                    if nums[i]==nums[j]:
                        return(True)
                    j = j - 1
                    print("I: "+str(i)+" J: "+str(j))
                i = i + 1
                j = i + min(k,nums.__len__()-1)
            return(False)

start = time.time()
Sol1 = Solution()
# print(Sol1.containsNearbyDuplicate([1,2,3,1],100))
print(Sol1.containsNearbyDuplicate([1,1,2,4,5,0,77,8,8],4))
print(Sol1.containsNearbyDuplicate([1],0))
print(Sol1.containsNearbyDuplicate([],1))
# print(Sol1.containsNearbyDuplicate([1],1))
# print(Sol1.containsNearbyDuplicate([1],1))
stop = time.time()
print(stop-start)

