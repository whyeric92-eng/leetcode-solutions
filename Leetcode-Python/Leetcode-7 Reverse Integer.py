#解法一
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output=0
        y=abs(x)
        while (y>0):
            output=output*10+y%10
            y=y//10
        if x>=0 and output <= 2**31-1:
            return output
        elif x<0 and -output >=-2**31:
            return -output
        else:
            return 0
#总结：这道题主要思路就是反转一个数值，output=output*10+y%10，y=y//10，判断条件是y>0
#注意点就是要看题，返回的值有限制的，仔细一点！