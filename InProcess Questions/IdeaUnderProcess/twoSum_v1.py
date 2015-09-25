__author__ = 'nsrivas3'

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        nums.sort()
        targMod = int(target/2)
        counter1 = 0
        counter2 = 0
        if (nums[0] >= 0):
            for i in range(0,nums.__len__()):
                if nums[i] <= targMod and nums[i+1] >= targMod:
                    counter1 = i
                    break
            for i in range(0,nums.__len__()):
                if nums[i] <= targMod + nums[0] and nums[i+1] >= targMod + nums[0]:
                    counter2 = i
                    break




# print(Sol1.largestNumber([121,12]))
Sol1 = Solution()
print(Sol1.twoSum([3, 30, 34, 5, 9],33))


