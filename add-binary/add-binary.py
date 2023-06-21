class Solution(object):
    def addBinary(self, a, b):
        ai=int(a,2)
        bi=int(b,2)
        c=ai+bi
        d=bin(c)
        return d[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """