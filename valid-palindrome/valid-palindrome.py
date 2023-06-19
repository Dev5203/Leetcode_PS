class Solution(object):
    def isPalindrome(self, s):
        s1="".join(c for c in s if c.isalnum())
        d=s1.lower()
        
        
        
        if d==d[::-1]:
            return True
        else:
            return False
        """
        :type s: str
        :rtype: bool
        """