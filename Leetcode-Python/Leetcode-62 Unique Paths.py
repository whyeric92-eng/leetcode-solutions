#解法一：Recursion 容易TLE
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==1 or n==1:
            return 1
        else:
            return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
#解法二：纯数学解法
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res=1
        for i in range(n,m+n-1):
            res*=i
        for i in range(1,m):
            res/=i
        return res
#解法三：二维DP
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[1]*m for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
#DP和Recursion其实是一个意思，DP加了记忆，所以不会TLE
#解法四：一维DP
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [1]*n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]
#dp[j]代表到第j列的方法