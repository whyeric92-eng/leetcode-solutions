class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp=[[0]*len(word2) for _ in range(len(word1))]
        dp[0][0]=0 if word1[0]==word2[0] else 1
        used_i=True if dp[0][0]==1 else False
        for i in range(1,len(word1)):
            if word1[i]==word2[0] and used_i:
                dp[i][0]=dp[i-1][0]
                used_i=False
            else:
                dp[i][0]=dp[i-1][0]+1
        used_j=True if dp[0][0]==1 else False
        for j in range(1,len(word2)):
            if word1[0]==word2[j] and used_j:
                dp[0][j]=dp[0][j-1]
                used_j=False
            else:
                dp[0][j]=dp[0][j-1]+1
        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i]!=word2[j]:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i][j-1]+1,dp[i-1][j]+1)
        return dp[len(word1)-1][len(word2)-1]
#正确的解法！！！
#几个注意点：1.引入used_i和used_j来判断是否被第一次匹配(有一次免费操作相当于)
           #2.对于word1[i]==word2[j]的判断，决定是否免费
           #3.易错点：即使一样，dp[i][j]=min(dp[i-1][j-1],dp[i][j-1]+1,dp[i-1][j]+1)，应该是这样

#改进点(这个方法有些写法还是不够简洁)：最开始判读空word和[0]那一部分有点啰嗦--引入Padding(哨兵/填充法)
word1="GPA 5.0" #for example
word2="I love you too" #for example
m, n = len(word1), len(word2)
dp = [[0] * (n + 1) for _ in range(m + 1)]  #比上面多了一行和一列
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j    
#现在dp[i][j]的意思就是从i的长度的word1变为j的长度的word2，对于0(空字符)，就是字符长度
#相对应的，后面dp[i][j]相当于在说word[i-1]和word[j-1]，这个要微调一下