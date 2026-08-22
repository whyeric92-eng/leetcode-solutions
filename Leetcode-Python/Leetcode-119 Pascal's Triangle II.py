class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp=[[] for _ in range(rowIndex+1)]
        dp[0]=[1]
        if rowIndex+1==1:
            return dp[0]
        if rowIndex+1>=2:
            dp[1]=[1,1]
        for i in range(2,rowIndex+1):
            dp[i]=[1]
            for j in range(len(dp[i-1])-1):
                dp[i].append(dp[i-1][j]+dp[i-1][j+1])
            dp[i].append(1)
        return dp[rowIndex]