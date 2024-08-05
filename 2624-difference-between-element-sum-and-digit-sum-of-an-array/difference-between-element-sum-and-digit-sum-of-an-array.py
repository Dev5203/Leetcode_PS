class Solution(object):
    def differenceOfSum(self, nums):
        s=0
        for i in nums:
            s+=i
        integer="".join(str(i) for i in nums)
        c=int(integer)
        z=[int(i) for i in str(c)]

        return (s-sum(z))
        """
        :type nums: List[int]
        :rtype: int
        """
        