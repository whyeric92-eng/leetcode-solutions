class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l1, l2, l3 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[l1]*2, dp[l2]*3, dp[l3]*5)
            if dp[i] == dp[l1]*2:
                l1 += 1
            if dp[i] == dp[l2]*3:
                l2 += 1
            if dp[i] == dp[l3]*5:
                l3 += 1
        return dp[n-1]

#算法思路
#丑数序列中,每个丑数都是某个更小的丑数乘以 2、3 或 5 得到的。所以维护三个指针 l1, l2, l3,分别指向"下一个要乘 2 / 3 / 5 的丑数"。
#每一步:三个候选值取最小,作为下一个丑数
#凡是等于这个最小值的候选,对应指针都前进一步