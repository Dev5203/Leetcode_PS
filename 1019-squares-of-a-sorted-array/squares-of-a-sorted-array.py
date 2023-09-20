class Solution(object):
    def sortedSquares(self, nums):
        n=[]
        for i in nums:
            n.append(i*i)
        for j in range(len(n)):
            min_val=min(n[j:])
            min_ind=n.index(min_val,j)
            n[j],n[min_ind]=n[min_ind],n[j]
        return n
        
        
        

        """
        :type nums: List[int]
        :rtype: List[int]
        """