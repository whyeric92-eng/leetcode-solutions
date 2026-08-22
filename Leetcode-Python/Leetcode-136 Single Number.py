class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res=res^num
        return res
#这道题就是^(XOR/异或)的妙用
#任何数异或0就是自己
#两个相同的数字异或就是0