class Solution(object):
    def maximumProduct(self, nums):
        pro=1
        nums.sort()
        return(max(nums[-1]*nums[0]*nums[1],nums[-1]*nums[-2]*nums[-3]))
        """
        :type nums: List[int]
        :rtype: int
        """
        