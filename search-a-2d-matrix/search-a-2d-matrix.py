class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if target==matrix[i][j]:
                    return True
                


        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """