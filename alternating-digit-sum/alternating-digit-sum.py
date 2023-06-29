class Solution(object):
    def alternateDigitSum(self, n):

        sol=0
        sign=1
        while n>0:
            
            sign*=-1
            sol+=n%10*sign
            n/=10
        return sign*sol
        """
        :type n: int
        :rtype: int
        """
        