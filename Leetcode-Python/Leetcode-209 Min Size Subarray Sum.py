from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre=0
        res=nums[0]
        if nums[0]>=target:
            return 1
        min_len=0
        for i in range(1,len(nums)):
            res+=nums[i]
            if res>=target:
                if min_len!=0:
                    min_len=min(min_len,i-pre+1)
                else:
                    min_len=i-pre+1
                while res>=target:
                    res-=nums[pre]
                    pre+=1
                min_len=min(min_len,i-pre+2)
        return min_len
#正确但是有点丑陋 就是最后while一直弹出pre的时候，弹出结束记得update一次最小窗口

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = 0
        min_len = float('inf')
        for right in range(len(nums)):
            res += nums[right]
            while res >= target:
                min_len = min(min_len, right - left + 1)
                res -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0