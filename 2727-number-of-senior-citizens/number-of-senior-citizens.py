class Solution(object):
    def countSeniors(self, details):
        d=[]
        for i in details:
            d.append(int(i[11:13]))
        s=[i for i in d if i>60]
        return len(s)

        """
        :type details: List[str]
        :rtype: int
        """
        