#解法一
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        step=0
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in wordDict:
                    dp[i][j]=True 
                if dp[0][i-1] and dp[i][j]:
                    dp[0][j]=True
        return dp[0][n-1]
#dp[i][j]表示能否代表从i到j的字符串
#缺点：时间，空间复杂度都比较高

#解法二
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1,n+1):
            for j in range(i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[n]
#一维数组解决，dp[i]就代表到第i位能否成功

#优化
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # [关键优化1]：转为 set，查找速度提升几千倍**********
        word_set = set(wordDict) 
        
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i): # 这里 range(i) 即可
                # [关键优化2]：使用 set 进行查找
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    # [关键优化3]：一旦确认 dp[i] 为真，立即停止当前 i 的后续尝试
                    break 
                    
        return dp[n]