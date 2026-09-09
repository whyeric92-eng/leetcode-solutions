class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            res = 0
            for part in str(num):
                res += int(part)
            num = res
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
# O(1) 数学技巧
# 一个数 mod 9 的结果，恒等于它各位数字之和 mod 9