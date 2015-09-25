__author__ = 'nsrivas3'

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)
        if t.__len__() == s.__len__():
            while((t.__len__()>0) and (s.__len__()>0)):
                try:
                    idx = t.index(s[0])
                    t.pop(idx)
                    s.pop(0)
                except:
                    return(False)
            if t.__len__() == s.__len__():
                return(True)
            else: return(False)
        else: return(False)

Sol1 = Solution()
print(Sol1.isAnagram('nitin','tinii'))