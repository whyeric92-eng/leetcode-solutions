class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        p=[[] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(i+1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    if j==0:
                        p[i].append(s[0:i])
                    else:
                        for char in p[j]:
                            char=char+" "+s[j:i]
                            p[i].append(char)
        return p[n] if dp[n] else []
#这道题作为变式，最难的地方在于如何存储数据
#关于p的定义，是[""]，还是[]:推荐[]，这样只用单独·处理j==0的情况，单独"启动"