__author__ = 'nsrivas3'

import math
import time

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        str1 = []
        for i in range(0,nums.__len__()):
            str1.append(str(nums[i]))
            print(str1)
        str1.sort(reverse=True)
        print(str1)
        str2 = ""
        for i in range(0,str1.__len__()):
            str2 = str2 + str1[i]
            print(str2)
        return(str2)


Sol1 = Solution()
print(Sol1.largestNumber([3, 30, 34, 5, 9]))
# print(Sol1.largestNumber([121,12]))

