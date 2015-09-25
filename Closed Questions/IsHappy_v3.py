__author__ = 'nsrivas3'

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        notHappy = 0
        iterlist = []

        def check(n):
            sum1 = 0
            while n!=0:
                sum1 = sum1 + (n%10)**2
                n = int(n/10)
            n = sum1
            # print(sum1)
            return(n)

        while (n!=1) and (notHappy!=1):
            n = check(n)
            print("n: "+str(n)+" NotHappy: "+str(notHappy)+" iterlist: "+str(iterlist))
            for I in iterlist:
                if n==I:
                    # print("n: "+str(n)+" NotHappy: "+str(notHappy)+" ChkRslt "+str(n==I))
                    notHappy = 1
                    break
                # else:
                    # print("n: "+str(n)+" NotHappy: "+str(notHappy)+" ChkRslt "+str(n==I))
            iterlist.append(n)

        if n==1: return(True)
        elif notHappy == 1: return(False)

Sol1 = Solution()
print(Sol1.isHappy(99798))

