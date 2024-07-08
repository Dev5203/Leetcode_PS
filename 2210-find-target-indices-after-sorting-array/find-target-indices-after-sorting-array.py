class Solution(object):
    def targetIndices(self, nums, target):
        l=[]
        nums.sort()
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                l.append(i)
        return l


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        