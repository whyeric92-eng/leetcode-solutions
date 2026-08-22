class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-1-j]
        return dp[n]
#这道题的难点在于写出状态转移方程
#对于1-n的BST，选1为起点：dp[0]*dp[n-1]，选2为起点：dp[1]*dp[n-2].........
#多少种类型只和数量有关，与具体数据无关