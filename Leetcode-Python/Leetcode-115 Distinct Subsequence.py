#解法一
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n,m=len(s),len(t)
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[0]=[1]*(n+1)
        for i in range(1,m+1):
            for j in range(i,n+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]+=dp[i-1][j-1]
                dp[i][j]+=dp[i][j-1]
        return dp[m][n]
#这道题就比较OK了，一个二维数组轻松搞定
#dp最难的就是选择dp[i][j]的定义，这道题中就是用s的前j个变成t的前i个的方法
#状态转移方程就是用不用新加进来的那个，会产生一个if语句然后搞定
#但其实这道题我们注意到只会用这一行的，我们是不是可以考虑用一维数组就解决了

#解法二
#用滚动数组把二维空间优化为一维数组
class Solution(object):
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        dp = [0] * (m + 1)
        dp[0] = 1 # t为空时只有一种解
        for j in range(n): # 遍历 s
            for i in range(m, 0, -1): # 倒序遍历 t  (这个倒序很关键)
                if s[j] == t[i-1]:
                    dp[i] += dp[i-1]
        return dp[m]
#dp[i]的含义：在 s 目前已经遍历过的部分（即 s[0...j]）中，有多少个子序列等于 t 的前 i 个字符（即 t[0...i-1]）