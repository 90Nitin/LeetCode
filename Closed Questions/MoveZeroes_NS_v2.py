__author__ = 'nsrivas3'


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        for i in range(0,nums.__len__()-1):
            l = []
            if nums[i] == 0:
                l.append(i)
                if nums[i+1] == 0:
                    counter = i + 1
                    while(counter < nums.__len__()):
                        if nums[counter] == 0:
                            l.append(counter)
                            counter = counter + 1
                        else: counter = nums.__len__() + 1
            # print(l,nums)
            if l.__len__()>0:
                if (l[-1] < nums.__len__()-1):
                    nums.insert(l[0],nums[l[-1]+1])
                    nums.pop(l[-1]+2)
        return(nums)

Sol1 = Solution()
print(Sol1.moveZeroes([0,1,0,3,12]))




