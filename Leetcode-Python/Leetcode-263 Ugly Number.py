class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        while (n % 2 == 0):
            n = n / 2
        while (n % 3 == 0):
            n = n / 3
        while (n % 5 == 0):
            n = n / 5
        return n == 1

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        # 用位运算处理因子 2,比取模/除法更快
        while n & 1 == 0:
            n >>= 1

        for factor in (3, 5):
            while n % factor == 0:
                n //= factor

        return n == 1