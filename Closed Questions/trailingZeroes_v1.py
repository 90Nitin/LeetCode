__author__ = 'nsrivas3'

import math

# To find the number of trailing zeroes in a given number

class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n==0:
            return(0)
        else:
            maxI = math.floor(math.log10(n)/math.log10(5))
            sumI = 0
            for i in range(1,maxI+1):
                print(" I: "+str(i))
                sumI = sumI + math.floor(n/(5**i))
            # print(sumI)
            return(int(sumI))


Sol1 = Solution()
print(Sol1.trailingZeroes(10))


