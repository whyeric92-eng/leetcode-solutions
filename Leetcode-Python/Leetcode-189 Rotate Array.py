from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        temp=nums[n-k:]
        nums[:]=temp+nums[:n-k]

def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
#这个可以实现空间复杂度为O(1) 比较巧妙