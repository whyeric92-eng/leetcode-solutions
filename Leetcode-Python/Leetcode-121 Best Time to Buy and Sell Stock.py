#解法一：dp
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        dp[0][0]=-prices[0]
        for i in range(1,n):
            if i>0:
                dp[i][1]=max(prices[i]+dp[i-1][0],dp[i-1][1])
                dp[i][0]=max(dp[i-1][0],-prices[i])
        return dp[n-1][1]
#这个解法的精妙之处就是引入dp[i][0]，这个0/1来表示当前状态，持有/未持有该股票

#解法一变式(压缩空间)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        # 对应你原来的 dp[0][0] (持有股票) 和 dp[0][1] (不持有股票)
        # hold 表示截止当前持有股票也就是最小的买入价格（负数表示）
        # cash 表示截止当前卖出股票后的最大利润
        hold = -prices[0]
        cash = 0
        for i in range(1, n):
            # 状态转移
            new_cash = max(cash, hold + prices[i]) # 卖出
            new_hold = max(hold, -prices[i])       # 买入
            cash = new_cash
            hold = new_hold
        return cash

#解法二：greedy
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf')
        max_profit=0
        for price in prices:
            if price<min_price:
                min_price=price
            max_profit=max(price-min_price,max_profit)
        return max_profit
#这个解法就是基本的greedy，不断更新即可