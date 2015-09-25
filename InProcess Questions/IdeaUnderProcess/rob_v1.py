__author__ = 'nsrivas3'

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        totalSum = sum(nums)
        evenSum = 0
        i = 0
        while (i<nums.__len__()):
            evenSum = evenSum + nums[i]
            i = i + 2
        if evenSum>(totalSum-evenSum):
            return(evenSum)
        else:
            return(totalSum-evenSum)

Sol1 = Solution()
print(Sol1.rob([1,3]))
