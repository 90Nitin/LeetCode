__author__ = 'nsrivas3'

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        if n==0: return(count)
        # if n==1: return(count+1)
        while n!=0:
            if n%2!=0:
                count = count + 1
            n = n/2
            print("n: "+str(n)+" count: "+str(count))
        return(count)

Sol1 = Solution()
Sol1.hammingWeight(1)
# Sol1.hammingWeight(9)
# Sol1.hammingWeight(10)