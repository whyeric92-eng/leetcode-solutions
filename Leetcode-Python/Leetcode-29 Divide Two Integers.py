class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        q=0
        if dividend==0:
            return 0
        sign=-1 if (dividend>0)^(divisor>0) else 1
        did=abs(dividend)
        dis=abs(divisor)
        while did>=dis:
            temp_dis=dis
            mul=1
            while did>=(temp_dis<<1):
                temp_dis<<=1
                mul<<=1
            did-=temp_dis
            q+=mul
        if q>=2**31 and sign==1:
            return 2**31-1
        return q if sign==1 else -q
#bit manipulation：这样比一个一个除来得快，用<<1表示左移一位(实际上就是乘2)