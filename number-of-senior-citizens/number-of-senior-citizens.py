class Solution(object):
    def countSeniors(self, details):
        modified_details = [item[:10] + item[11:] for item in details]
        n=[]
        for i in range(len(modified_details)):
            if int(modified_details[i][10:12])>60:
                n.append(int(modified_details[i][10:12]))
        return len(n)

        """
        :type details: List[str]
        :rtype: int
        """