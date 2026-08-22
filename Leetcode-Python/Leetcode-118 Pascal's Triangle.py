class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp=[[] for _ in range(numRows)]
        dp[0]=[1]
        if numRows==1:
            return dp
        if numRows>=2:
            dp[1]=[1,1]
        for i in range(2,numRows):
            dp[i]=[1]
            for j in range(len(dp[i-1])-1):
                dp[i].append(dp[i-1][j]+dp[i-1][j+1])
            dp[i].append(1)
        return dp
#这道题比较简单，直接翻译就解决了