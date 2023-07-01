class Solution(object):
    def capitalizeTitle(self, title):
        c=title.split()
        t=' '.join([i.lower() if len(i)==1 or len(i)==2 else i.title() for i in c])
        return t

        
        """
        :type title: str
        :rtype: str
        """
        