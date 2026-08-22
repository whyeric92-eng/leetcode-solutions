class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        def convert(title):
            return ord(title)-64
        res=0
        n=len(columnTitle)
        for i in range(n-1,-1,-1):
            res+=convert(columnTitle[i])*(26**(n-i-1))
        return res
#这个写法没啥问题 唯一可以改进的地方就是可读性--不用逆序

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for char in columnTitle:
            # 每次把之前的结果整体向左移一位（在26进制中就是乘26）
            # 然后加上当前字符代表的数字
            res = res * 26 + (ord(char) - ord('A') + 1)
        return res