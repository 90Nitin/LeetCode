__author__ = 'nsrivas3'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        print(nums)
        for i in range(0,nums.__len__()-1):
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                print(nums)
        return(nums)

Sol1 = Solution()
print(Sol1.moveZeroes([0,1,2,0,4]))




