__author__ = 'nsrivas3'

import math
import time

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        sumprime = 0
        def chkPrime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0: return(0)
            return(1)
        for i in range(2,n):
            sumprime = sumprime + chkPrime(i)
        return(sumprime)

# Test Cases
start = time.time()
Sol1 = Solution()
print(Sol1.countPrimes(499979))
# print(Sol1.countPrimes(4))
stop = time.time()
print(start-stop)





