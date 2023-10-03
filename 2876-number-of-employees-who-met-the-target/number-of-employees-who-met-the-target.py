class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        b=[i for i in hours if target<=i]
        return(len(b))
        

        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        