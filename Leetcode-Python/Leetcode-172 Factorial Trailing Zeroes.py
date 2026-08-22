class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0:
            return 0
        def num_x(n,x):
            res=0
            while n>=x:
                res+=(n//x)
                x*=5
            return res
        return num_x(n,5)
#这道题就一个核心思路 就是尾部的0只取决于有多少个5 (因为5肯定比2少)