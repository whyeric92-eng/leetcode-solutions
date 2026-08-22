from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        def judge(i):
            if i+k+1<=n and nums[i] in nums[i+1:i+k+1]:
                return True
            elif i+k+1>n and nums[i] in nums[i+1:n]:
                return True
            return False
        for i in range(n):
            if judge(i):
                return True
        return False
#这个写法不好，会TLE

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        dic={}
        for i in range(n):
            if nums[i] in dic:
                if (i-dic[nums[i]])<=k:
                    return True
                else:
                    dic[nums[i]]=i
            else:
                dic[nums[i]]=i
        return False
#用dic来存储，一次性搞定