__author__ = 'nsrivas3'

import time

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        # List of candies for each kid
        def candyAlloc(iter,ratings,candyList):
            if ratings.__len__()<=1:
                if ratings.__len__()==0:
                    return([0])
                else:
                    return([1])

            if iter==0:
                if ratings[0]>ratings[1]:
                    candyList[0] = 2
                return(candyList)

            if ratings[iter]>ratings[iter-1]:
                candyList[iter] = candyList[iter-1] + 1
            else:
                candyList[iter] = max(candyList[iter-1] - 1,1)
            return(candyList)

        candyList = [1]*ratings.__len__()
        for i in range(0,ratings.__len__()):
            candyList = candyAlloc(i,ratings,candyList)
        return(candyList)


start = time.time()
Sol1 = Solution()
print(Sol1.candy([5,3,1]))
print(Sol1.candy([0,0,2]))
print(Sol1.candy([1]))
print(Sol1.candy([]))
print(Sol1.candy([1,0,2,1]))
print(Sol1.candy([1,0,2,2]))
stop = time.time()
# print(stop-start)



