class Solution(object):
    def alternateDigitSum(self, n):
        l=[int(i) for i in str(n)]
        n=[]
        p=[]
        for i in range(0,len(l),2):
            n.append(l[i])
        for j in range(1,len(l),2):
            p.append(-l[j])
        return sum(n+p)


        """
        :type n: int
        :rtype: int
        """