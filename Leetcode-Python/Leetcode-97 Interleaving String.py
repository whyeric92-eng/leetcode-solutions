class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l,n,m=len(s3),len(s1),len(s2)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        if l!=m+n:
            return False
        for i in range(n+1):
            for j in range(m+1):
                if i==j==0:  #index都为0先派出
                    continue
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]: #此时i>=1才可以
                    dp[i][j] = True
                elif j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]: #此时j>=1才可以
                    dp[i][j] = True
        return dp[n][m]
#这道题首先，贪心算法行不通，因为两个相同时不知道删哪个，无法判断
#然后这道题dp，就要思考几维dp，这道题巧妙之处就在于二维dp完美解决
#dp[i][j]，i代表s1的前i个，j代表s2的前j个，dp[i][j]表示这样能否构成s3的前(i+j)个
#这样就可以有选择，不需要在相等时做出决定