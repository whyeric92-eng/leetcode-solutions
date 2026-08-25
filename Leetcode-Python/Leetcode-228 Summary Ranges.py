from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        if not nums:
            return res
        start,end=nums[0],nums[0]
        for i in range(1,len(nums)):
            if nums[i]==end+1:
                end+=1
            elif start==end:
                res.append(f"{start}")
                start,end=nums[i],nums[i]
            else:
                res.append(f"{start}->{end}")
                start,end=nums[i],nums[i]
        res.append(f"{start}->{end}") if start!=end else res.append(f"{start}")
        return res

#提升代码简洁性
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            end = nums[i]
            res.append(f"{start}" if start == end else f"{start}->{end}")
            i += 1
        return res