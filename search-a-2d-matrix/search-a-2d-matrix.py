class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in matrix:
            for j in i:
                if target==j:
                    return True
                


        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """