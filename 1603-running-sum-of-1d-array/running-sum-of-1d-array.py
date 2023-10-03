class Solution(object):
    def runningSum(self, nums):
        sum=0
        n=[]
        for i in range(len(nums)):
            sum+=nums[i]
            n.append(sum)
        return n
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """