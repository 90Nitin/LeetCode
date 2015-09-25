__author__ = 'nsrivas3'

import math

# @param {string} s
# @return {string}
def shortestPalindrome(s):
# 1. Assume that the center of symmetry in the string is at the center of the string
# 2. Verify to see if this is true
# 3. Keep moving the center to the left till u can find symmetry somewhere
# 4. As soon as we find symmetry we take the rest of the words in the string and put them in front of the first letter in the string
# 5. This becomes our starting of the string
    def PalinCheck(str):
        len = str.__len__()
        if len%2==0:
            n = (len+1)/2-1
            m = (len+1)/2-1
            while (n>0):
                # Conditions only applied to the left part of the string since we shall be shifting the mean of the string
                # the left
                if str[math.floor(n)] != str[math.ceil(m)]:
                    return(0)
                n = n - 1
                m = m + 1
            return(1)
        else:
            n = int((len+1)/2-1)
            i = 0
            while (n-i>=0):
                if str[n-i] != str[n+i]:
                    return(0)
                i = i + 1
            return(1)
    str = s
    len = str.__len__()
    l = str.__len__()
    while(l>=0):
        if (PalinCheck(str)==1):
            addStr = s[l:len]
            return(addStr+s)
        l = l - 1
        str = str[0:l]


print(shortestPalindrome("abcd"))


