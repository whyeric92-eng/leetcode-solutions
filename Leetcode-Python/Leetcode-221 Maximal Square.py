from typing import List
from math import sqrt
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def judge(i,j,l):
            for k in range(l):
                if matrix[i-k][j+1]=="0":
                    return False
                if matrix[i+1][j-k]=="0":
                    return False
            return True

        dp = [[int(x) for x in row] for row in matrix]
        m=len(matrix)
        n=len(matrix[0])
        res=0
        if 1 in dp[0]:
            res=1
        for row in range(m):
            if dp[row][0]==1:
                res=1
        for i in range(1,m):
            for j in range(1,n):
                if dp[i][j]==1:
                    if dp[i-1][j-1]!=0:
                        l=int(sqrt(dp[i-1][j-1]))
                        for ll in range(l,-1,-1):
                            if judge(i-1,j-1,ll):
                                dp[i][j]=(ll+1)**2
                                break
                        #这个地方要逐步倒退 如果judge成功了,就立即break
                    res=max(res,dp[i][j])
        return res

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
#让(i,j)处的正方形边长变成k,那它的左边、上边、左上角这三块都必须至少能撑起边长k-1的正方形,才能拼出一个更大的
                    res = max(res, dp[i][j])
        return res * res
#标准写法
#dp[i][j] 定义为:以 (i,j) 为右下角、能组成的最大正方形的边长