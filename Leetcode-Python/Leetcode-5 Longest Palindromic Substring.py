#解法一
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        n=len(s)
        maxlen=0
        result=""
        def pal(char):
            if char[::]==char[::-1]:
                return True
            else:
                return False
        for i in range(n):
            res.append(s[i:])
            for j in range(i,n):
                res.append(s[i:j])
        for char in res:
            if pal(char) and len(char)>maxlen:
                maxlen=len(char)
                result=char
        return result
#解法二 dp
class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res = s[0]

        for r in range(n):
            for l in range(r+1):
                if s[l] == s[r] and (r-l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = True
                    if r-l+1 > len(res):
                        res = s[l:r+1]
        return res
#dp[l][r]=True代表s[l:r+1]是回文数，有点递推的感觉