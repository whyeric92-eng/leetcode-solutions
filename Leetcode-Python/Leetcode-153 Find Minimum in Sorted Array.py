from types import List 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[left]>nums[mid]:
                right=mid
            elif nums[left]>nums[right] and nums[left]==nums[mid]:
                return nums[right]
            elif nums[mid]>nums[right]:
                left=mid
            else:
                return nums[left]
        return nums[left]
#太多边界条件判断

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 如果 mid 的值大于 right 的值，说明最小值一定在 mid 的右边
            if nums[mid] > nums[right]:
                left = mid + 1
            # 否则，mid 或者是最小值，或者最小值在 mid 的左边
            else:
                right = mid
                
        return nums[left]