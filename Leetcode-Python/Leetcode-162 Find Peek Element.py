from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        begin=float('-inf')
        end=float('-inf')
        new_nums=[begin]+nums+[end]
        for i in range(1,len(new_nums)-1):
            if new_nums[i]>new_nums[i+1] and new_nums[i]>new_nums[i-1]:
                return i-1


class SolutionBinarySearch:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return lo
#如果 nums[mid] < nums[mid+1]，那么右边一定存在峰值（因为数组边界是 -inf）；反之左边一定存在峰值。
#每次都往"更高的那侧"走，最终一定能夹住一个峰值
#其实有点函数的思想，零点存在定理的感觉

#能排除 mid  → right = mid - 1，用 left <= right
#不能排除 mid → right = mid，   用 left < right