class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if target==nums[mid]:
                return mid
            if nums[start]<=nums[mid]:
                if nums[start]<=target<nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1
#在rotate的情况下的binary search (该序列要么左半边有序，要么右半边有序)
#几个易错点：1.start<=end 2.判断左半边/右半边有序，要加上<=，而且最好用else(避免出现两个if都不进的情况)