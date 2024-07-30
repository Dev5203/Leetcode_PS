class Solution(object):
    def shuffle(self, nums, n):
        a=nums[0:n]
        b=nums[n:]
        c=[a,b]
        b=[]

        tc=[[c[j][i] for j in range(len(c))] for i in range(len(c[0]))]
        for i in tc:
            for j in i:
                b.append(j)
        return b

        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        