class Solution(object):
    def countNegatives(self, grid):
        grid_str=str(grid)
        z=grid_str.count('-')
        return z

        


        """
        :type grid: List[List[int]]
        :rtype: int
        """