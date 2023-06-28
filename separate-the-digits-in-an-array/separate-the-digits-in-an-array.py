class Solution(object):
    def separateDigits(self, nums):
        n=[]
        s=''.join(str(i) for i in nums)
        for i in s:
            n.append(int(i))
        return n
        """
        :type nums: List[int]
        :rtype: List[int]
        """