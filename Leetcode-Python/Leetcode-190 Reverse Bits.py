class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for _ in range(32):
            res=(res<<1)
            res=res|(n&1)
            n=(n>>1)
        return res
#关于bit manipulation: 
#1. 整数存储的本质就是二进制。因此，res << 1 这种位运算操作直接作用于该整数对应的二进制表示
#2. 这个题目的本质就是把n的32位数全部反转一遍 这种题目的常规思路就是一位一位遍历添加到res当中
#3. 常见操作: 
#(1): res<<1 给最右边续一位(0) 如101->1010
#(2): n&1 利用and运算取出n的最后一位
#(3): n>>1 消除掉最右边的一位