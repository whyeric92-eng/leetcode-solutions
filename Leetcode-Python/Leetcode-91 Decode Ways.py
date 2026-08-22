class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0]*(len(s)+1)
        dp[0]=1
        if s[0]=="0":
            return 0
        dp[1]=1
        for i in range(2,len(s)+1):
            if s[i-1]=="0":
                if s[i-2]=="1" or s[i-2]=="2":
                    dp[i]=dp[i-2]
                else:
                    return 0
            elif s[i-1]>="7":
                if s[i-2]=="1":
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
            else:
                if s[i-2]=="1" or s[i-2]=="2":
                    dp[i]=dp[i-1]+dp[i-2]
                else:
                    dp[i]=dp[i-1]
        return dp[len(s)]
#这道题DP，思路不难，细节处理(尤其是对于0)，要非常仔细
#这个写法分类太细了，有点啰嗦

class Solution(object):
    def numDecodings(self, s):
        if s[0] == "0": return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 # 因为前面已经判断过 s[0] != '0' 了
        
        for i in range(2, n + 1):
            # 1. 单独看当前位：只要不是 '0'，就能继承 dp[i-1]
            current_digit = int(s[i-1])
            if current_digit != 0:
                dp[i] += dp[i-1]
            
            # 2. 结合前一位看：如果是 10-26，就能继承 dp[i-2]
            two_digits = int(s[i-2:i]) # 取出两位的数值
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
#这个看着就简单直接！