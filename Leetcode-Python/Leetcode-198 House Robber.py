from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[(0,False)]*n
        dp[0]=(nums[0],True)
        if n>1:
            dp[1]=(nums[1],True) if nums[1]>nums[0] else (nums[0],False)
        if n>2:
            for i in range(2,n):
                if dp[i-1][1] is False:
                    dp[i]=(dp[i-1][0]+nums[i],True)
                elif dp[i-1][0]>dp[i-2][0]+nums[i]:
                    dp[i]=dp[i-1]
                else:
                    dp[i]=(dp[i-2][0]+nums[i],True)
        return dp[n-1][0]
#比较基础的dp 用一个变量True/False来存储当前nums[i]是否被使用

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]
        
        # 使用两个变量滚动更新，空间复杂度可优化至 O(1)
        prev2 = 0 # 对应 dp[i-2]
        prev1 = 0 # 对应 dp[i-1]
        
        for x in nums:
            # 当前最大收益是：不抢当前(prev1) 和 抢当前(prev2 + x) 的较大值
            curr = max(prev1, prev2 + x)
            prev2 = prev1
            prev1 = curr
            
        return prev1
#这个写法其实是对的 但是不直观 这个包含了[1 3 1 2]这种情况 是通过prev2+x来实现的
#其实prev1没有选最后一个就等价于prev2了