class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for elements in row:
                if elements==target:
                    return True
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """