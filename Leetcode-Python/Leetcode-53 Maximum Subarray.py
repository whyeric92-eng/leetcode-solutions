#解法一
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = nums[0]
        res = nums[0]
        for x in nums[1:]:
            cur = max(x, cur + x)
            res = max(res, cur)
        return res
#用cur和res来记录，取值
#解法二
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)
#对于dp，dp[i]其实就是到i位置的最大sum，不必展示哪个取，哪个不取的步骤，结果不断更新即可

#*****这种题技巧大差不差，记忆这种pattern******