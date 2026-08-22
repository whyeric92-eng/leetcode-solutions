class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=1,2
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for _ in range(n-2):
                a,b=b,a+b
            return b
#其实就是斐波那契数列，但是不用recursion，最优解了，这个时间复杂度最低