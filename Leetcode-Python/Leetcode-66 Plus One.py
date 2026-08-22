class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        out=int("".join(map(str,digits)))+1
        res=[int(x) for x in str(out)]
        return res
#表示list最简单直接的方法永远都是[... for _ in ....]