class Solution(object):
    def sortedSquares(self, nums):
        n=[]
        for i in nums:
            n.append(i**2)
        n.sort()
        return n

        """
        :type nums: List[int]
        :rtype: List[int]
        """