__author__ = 'nsrivas3'

import math
import time

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        def mapDict(s):
            mapping = {}
            for i in range(0,s.__len__()):
                if s[i] in mapping.keys():
                    mapping[s[i]] = str(mapping[s[i]]) + str(","+str(i))
                else: mapping[s[i]] = str(i)
            return(mapping)
        # the lower and upper case might be mapped differently - s.lower()
        # the lower and upper case might be mapped differently - t.lower()
        valS = mapDict(s).values()
        valT = mapDict(t).values()
        if valS.__len__()!=valT.__len__(): return(False)
        valS.sort()
        valT.sort()
        for i in range(0,valS.__len__()):
            if valS[i]!=valT[i]: return(False)
        return(True)




start = time.time()
Sol1 = Solution()
print(Sol1.isIsomorphic("nitin","mitin"))
stop = time.time()
print(start-stop)
        