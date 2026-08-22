class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        def pal(s):
            return s==s[::-1]
        def backtrack(start,path):
            if start==len(s):
                res.append(list(path))
                return 
            for end in range(start+1,len(s)+1):
                if pal(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end,path)
                    path.pop()
        backtrack(0,[])
        return res
#典型的backtrack解法
class Solution(object):
    def partition(self, s):
        n = len(s)
        # dp[i] 存储 s[:i] 的所有划分方案
        # 初始状态：dp[0] 为空字符串的方案，即一个包含空列表的列表 [[]]
        dp = [[] for _ in range(n + 1)]
        dp[0] = [[]]
        
        # 辅助函数：判断回文（也可以结合方案一的二维DP来做双重优化）
        def is_pal(sub):
            return sub == sub[::-1]

        for i in range(1, n + 1):
            # 尝试在 j 处切开，s[:i] 变成了 s[:j] 和 s[j:i] 两部分
            for j in range(i):
                suffix = s[j:i]
                if is_pal(suffix):
                    # 如果后半部分是回文，就把 suffix 接在 dp[j] 每一个方案的后面
                    for path in dp[j]:
                        dp[i].append(path + [suffix])
                        # concatenate 把path和[suffix]拼起来
        return dp[n]
#这种是纯dp递推