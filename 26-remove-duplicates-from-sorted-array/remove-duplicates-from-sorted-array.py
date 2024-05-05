class Solution(object):
    def removeDuplicates(self, nums):
        res=1
        for i in range(1,len(nums)):
            if nums[res-1]!=nums[i]:
                nums[res]=nums[i]
                res+=1
        return res
            

      
        
        