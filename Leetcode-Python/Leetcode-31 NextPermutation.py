class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=len(nums)-1
            while nums[i]>=nums[j]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        left,right=i+1,len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        return nums
#其实大致思路挺简单：step1.从后往前找到第一个不是升序的num
#step2.从后面的部分找到第一个比该num大的数，交换
#step3.剩余的直接sort为升序之后即可