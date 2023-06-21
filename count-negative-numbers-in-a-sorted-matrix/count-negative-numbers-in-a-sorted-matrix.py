class Solution(object):
    def countNegatives(self, grid):
        grid_str=''.join(str(i) for i in grid)
        return grid_str.count('-')
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        