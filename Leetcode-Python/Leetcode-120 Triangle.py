class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n=len(triangle)
        dp=[[0]*(i+1) for i in range(n)]
        dp[0]=triangle[0]
        if n==1:
            return dp[0][0]
        for j in range(1,n):
            for k in range(j+1):
                if k==0:
                    dp[j][0]=dp[j-1][0]+triangle[j][0]
                elif k==j:
                    dp[j][k]=dp[j-1][j-1]+triangle[j][k]
                else:
                    dp[j][k]=triangle[j][k]+min(dp[j-1][k],dp[j-1][k-1])
        return min(dp[n-1])
#这道题就是典型的从上到下的DP，注意点就是一些边界处理
#这个可能需要改进的地方：空间有点大，这个解法是用的二维数组，应该尝试用滚动数组优化空间复杂度