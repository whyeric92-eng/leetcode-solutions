from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp = 1
        zero_1 = False
        zero_2 = False
        for num in nums:
            if num != 0:
                temp *= num
            elif num == 0 and not zero_1:
                zero_1 = True
            else:
                zero_2 = True
        for i in range(len(nums)):
            if nums[i] == 0:
                nums [i] = temp if not zero_2 else 0
            elif nums[i] != 0 and zero_1:
                nums[i] = 0
            else:
                nums[i] = int(temp/nums[i])
        return nums
#时间复杂度 空间复杂度 都过关 但是精度可能存在问题
#而且zero判读也较为繁琐

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
    #此时res[i]就是res左边所有数字的乘积
        suffix = 1
        for i in range(n - 1, -1, -1):
    #必须倒序
            res[i] *= suffix
            suffix *= nums[i]
        return res