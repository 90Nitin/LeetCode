__author__ = 'nsrivas3'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums.sort()
        nums.sort(reverse = True)
        dnums = dnums - anums
        for i in range(0,nums.__len__()):
            if anums[i]==dnums[i]: return(anums[i])




