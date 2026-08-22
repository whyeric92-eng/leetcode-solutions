class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=[0]*32
        for num in nums:
            for i in range(32):
                count[i]+=(num>>i)&1
        res=0
        for i in range(32):
            if (count[i]%3==1):
                res|=(1<<i)
        if res >= 0x80000000:
            res -= 0x100000000
        return res
#这道题思路是：搞一个32位数组来记录每一位出现0/1的次数，无法整除3的就是那个single number
#具体实现方面：1.(num>>i)&i 取从右往左数的index(i)位数
#2.res|=(1<<i) 把从右往左数的index(i)位数变为1
#3.最后记得处理负数的情况