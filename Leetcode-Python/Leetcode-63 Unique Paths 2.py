#解法一：二维dp
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[1 if num==0 else 0 for num in char] for char in obstacleGrid]
        if dp[0][0]==0:
            return 0
        for i in range(0,m):
            for j in range(0,n):
                if i==0:
                    if j>0:
                        dp[i][j]*=dp[i][j-1]
                elif j==0:
                    dp[i][j]*=dp[i-1][j]
                else:
                    dp[i][j]*=dp[i-1][j]+dp[i][j-1] 
        return dp[m-1][n-1] 
#思路大致相同，就是易错，尤其是第一行/第一列，也得进行判断
#解法二：一维dp
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]

        return dp[-1]