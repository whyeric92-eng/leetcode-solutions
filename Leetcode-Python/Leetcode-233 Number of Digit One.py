class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        elif n<10:
            return 1 
        m=str(n)
        k=len(m)-1
        first=int(m[0])
        power=10**k
        remainder=n-first*power
        if first==1:
            return remainder+1+self.countDigitOne(power-1)+self.countDigitOne(remainder)
        else:
            return power+self.countDigitOne(power-1)*first+self.countDigitOne(remainder)
#这道题:Count Digit One，本质思想就是一位一位的来看有多少个1满足条件
#对于1abcd这种，(abcd+1)个1开头的，对于不在最高位的1，可能是1(abcd),可能是0(9999)，由此产生两个式子
#对于abcde这种，10000个1开头的，对于不在最高位的1，可能是(0-a-1)(9999),也可能是a(bcde)，由此产生两个式子
#这种题不好想，理解，记忆，然后模仿