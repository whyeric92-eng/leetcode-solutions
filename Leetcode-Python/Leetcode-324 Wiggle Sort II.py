class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        nums1=nums[:(1+len(nums))//2]
        nums1.reverse()
        nums2=nums[(1+len(nums))//2:]
        nums2.reverse()
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=nums1[i//2]
            else:
                nums[i]=nums2[i//2]
        return nums
#这个解法不错，除了使用了新列表nums1，nums2来辅助
#其实这种排序方式就是在偶数index推谷底，奇数index堆波峰
#注意的是nums1最大的应该在最右边，nums2最小的最好在最左边(这两个隔的尽量远)