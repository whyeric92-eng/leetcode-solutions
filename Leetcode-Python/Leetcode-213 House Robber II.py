from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums):
            prev, curr = 0, 0
            for num in nums:
                prev, curr = curr, max(curr, prev + num)
            return curr
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
#这道题的思路其实很简单，无非就是两个情况:不考虑第一个或者不考虑最后一个，分别进行一次dp就可以搞定