class Solution(object):
    def maximumWealth(self, accounts):
        n=[]
        for i in accounts:
            n.append(sum(i))
        return max(n)
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        