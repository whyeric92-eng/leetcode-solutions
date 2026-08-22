from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=1
        right=len(numbers)
        while left<right:
            cur_sum=numbers[left-1]+numbers[right-1]
            if cur_sum==target:
                return [left,right]
            elif cur_sum>target:
                right-=1
            else:
                left+=1
#非常常规的思路 直接binary search即可