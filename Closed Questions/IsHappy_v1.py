__author__ = 'nsrivas3'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n==1:
            return(True)
        else:
            sum1 = 0
            while n!=0:
                sum1 = sum1 + (n%10)**2
                n = int(n/10)
            n = sum1
            print(sum1)
            self.isHappy(n)


Sol1 = Solution()
print(Sol1.isHappy(19))

