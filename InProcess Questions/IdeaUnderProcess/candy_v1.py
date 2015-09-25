__author__ = 'nsrivas3'

import time
import math

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        # List of candies for each kid
        candyList = [1]*ratings.__len__()
        def candyAlloc(iter,ratings,candyList):

            if ratings.__len__()<=1:
                if ratings.__len__()==0:
                    return([0])
                else:
                    return([1])
            if iter>0:
                if ratings[iter]>ratings[iter-1]:
                    candyList[iter] = candyList[iter-1] + 1
                else:
                    candyList[iter] = max(candyList[iter-1] - 1,1)
            else:
                if ratings[1]>ratings[0]:
                    candyList[1] = 2
                    candyList[0] = 1
                else:
                    candyList[0] = 1
                    candyList[1] = 1

            return(candyList)

        for i in range(0,ratings.__len__()):
            candyList = candyAlloc(i,ratings,candyList)
        return(candyList)


start = time.time()
Sol1 = Solution()
print(Sol1.candy([2,1]))
stop = time.time()
print(stop-start)


