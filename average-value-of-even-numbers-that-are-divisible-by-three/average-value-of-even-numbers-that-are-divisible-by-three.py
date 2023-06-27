class Solution(object):
    def averageValue(self, nums):
        n=[]
        sum=0
        for i in nums:
            if i%3==0 and i%2==0:
                n.append(i)
        for i in n:
            sum+=i
        
        if len(n)!=0:
            return ((sum//len(n)))
        else:
            return 0 
        
        """
        :type nums: List[int]
        :rtype: int
        """