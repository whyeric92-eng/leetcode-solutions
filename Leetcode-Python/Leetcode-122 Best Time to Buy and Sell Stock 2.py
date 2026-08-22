#解法一
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices) 
        profit=0
        for i in range(n-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit
#这个解法就很简单直接，但可能运行时间会长一点，没有任何多余操作