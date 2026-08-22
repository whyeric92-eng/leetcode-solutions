class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n=len(s),len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(2, n + 1):   #细节注意1：对于j=0的时候，可以"吃掉"2个
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]!="*":
                    if (p[i-1]=="." or p[i-1]==s[j-1]) and dp[i-1][j-1]:
                        dp[i][j]=True
                else:
                    if dp[i-2][j]:    #细节注意2：可以吃掉2个，对于"*"
                        dp[i][j]=True
                    elif dp[i][j-1] and (p[i-2]==s[j-1] or p[i-2]=="."):
                    #本题最关键/最精妙的一个处理:用dp[i][j-1]而非dp[i-1][j]，让"*"可以一直吃
                        dp[i][j]=True
        return dp[n][m]
#这道题不愧是difficult的
#大致思路就是看p的前i个能否匹配s的前j个，较为典型的dp
#这道题困难之处在于细节太多，需要注意
#后面的分类讨论，逻辑清楚一些，不要全在那里if，elif，过于冗杂

#这道题写法其实有点奇怪，应该是从s开始遍历，从p开始有点奇怪反正