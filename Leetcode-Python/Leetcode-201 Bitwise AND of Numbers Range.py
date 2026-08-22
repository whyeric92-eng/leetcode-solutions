class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        def bitwise(a,b):
            res=0
            for i in range(32):
                res=res<<1
                temp=(a&1)&(b&1)
                a=a>>1
                b=b>>1
                res=res|temp
            def reverse(n):
                res=0
                for _ in range(32):
                    res=(res<<1)
                    res=res|(n&1)
                    n=(n>>1)
                return res
            return reverse(res)
        res=left
        for i in range(left+1,right+1):
            res=bitwise(res,i)
        return res
#这个解法理论上来说是对的 但是不行 太蠢笨了 时间复杂度是range*32 不可取

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift=0
        while left<right:
            left>>=1
            right>>=1
            shift+=1
        return left<<shift
#这个解法很巧妙 直接找到left和right相同开头的部分 因为他们尾巴bitwise之后肯定是0 不用管 用shift来记录位移个数

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= (right - 1)  # 清除 right 最低的 1
        return right
#这个解法也很巧妙 这个的思路就是逐渐减小right(通过把right最低位的1变为0)
#这个的最后临界条件可能不是left==right 因为right可能一下子就缩小到小于left的值