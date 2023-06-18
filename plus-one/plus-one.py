class Solution(object):
    def plusOne(self, digits):
        #converting list to integer
        result=''.join(str(i) for i in digits)
        z=int(result)+1
        #convert our answer to list
        ans=[int(i) for i in str(z)]
        return ans
        
        """
        :type digits: List[int]
        :rtype: List[int]
        """