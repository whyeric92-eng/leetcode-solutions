class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        half=self.myPow(x,n//2)
        if n%2==0:
            return half*half
        else:
            return half*half*x
#注意点：1.调用函数：self.myPow(x,n)
#2.此种情况，推荐用half,这样可以减少recursion的次数****小技巧