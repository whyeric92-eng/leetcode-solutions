class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right=0,len(nums)-1
        res=[]
        while left<=right:
            mid=(left+right)//2
            if (nums[mid]==target):
                mid1,mid2=mid,mid
                while (0<= mid1 and mid1<=len(nums)-1) and (nums[mid1]==target):
                    mid1+=1
                while (0<= mid2 and mid2<=len(nums)-1) and(nums[mid2]==target):
                    mid2-=1
                return [mid2+1,mid1-1]
            elif (nums[mid]>target):
                right=mid-1
            else:
                left=mid+1
        if not res:
            return [-1,-1]