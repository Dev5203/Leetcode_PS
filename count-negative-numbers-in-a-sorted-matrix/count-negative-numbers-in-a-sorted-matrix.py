class Solution(object):
    def countNegatives(self, grid):
        nums=[]
        for i in grid:
            for j in i:
                if j<0:
                    nums.append(j)
        return len(nums)
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        