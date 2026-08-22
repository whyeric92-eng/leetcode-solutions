class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp=0
        res=0
        for char in s:
            if char=="1":
                temp+=1
            else:
                res+=(temp+1)*temp/2
                temp=0
        res+=(temp+1)*temp/2
        return res%(10**9+7)
#连续n个1就会产生n*(n+1)/2个1
#注意读题，题目中说了res太大时该怎么处理