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
        # Sieve of the most rudimentary nature
        j = 3
        while j<n:
            sumprime = sumprime + chkPrime(j)
            j = j + 2
        return(sumprime+1)

# Test Cases
start = time.time()
Sol1 = Solution()
print(Sol1.countPrimes(499979))
print(Sol1.countPrimes(2))
print(Sol1.countPrimes(10))
print(Sol1.countPrimes(15))
print(Sol1.countPrimes(20))
stop = time.time()
print(stop-start)





