class Solution(object):
    def isAnagram(self, s, t):
        s1=sorted(s)
        t1=sorted(t)
        if s1[0:]==t1[0:]:
            return True
        else:
            return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """