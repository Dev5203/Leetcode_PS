class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        elif target<nums[-1]:
            nums.insert(nums[-1],target)
            nums.sort()
            return nums.index(target)
        else:
            nums.append(target)
            return nums.index(target)
            



        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
           
        

    