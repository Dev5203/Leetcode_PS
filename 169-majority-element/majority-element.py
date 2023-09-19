class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
       
        middle=len(nums)//2
        return(nums[middle])

        

        
       
        """
        :type nums: List[int]
        :rtype: int
        """