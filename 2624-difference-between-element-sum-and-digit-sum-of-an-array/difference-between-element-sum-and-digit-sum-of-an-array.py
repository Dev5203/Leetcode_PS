class Solution(object):
    def differenceOfSum(self, nums):
        integer="".join(str(i) for i in nums)
        c=int(integer)
        z=[int(i) for i in str(c)]

        return (sum(nums)-sum(z))
        """
        :type nums: List[int]
        :rtype: int
        """
        