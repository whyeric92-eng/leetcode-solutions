#简单解法，用内置函数sort
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
#维持当前最大k个，容易TLE
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lst=nums[:k]
        for num in nums[k:]:
            if num>min(lst):
                index=lst.index(min(lst))
                lst[index]=num
        return min(lst)
#其实此题更好解法有heap和quickselect