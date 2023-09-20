class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            min_val=min(nums[i:])
            min_ind=nums.index(min_val,i)
            nums[i],nums[min_ind]=nums[min_ind],nums[i]
        return nums


        
        
        """

        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """