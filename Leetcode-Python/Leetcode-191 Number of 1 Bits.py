class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        while (n!=0):
            n=n&(n-1)
            num+=1
        return num
#这个n&(n-1)作用就是消除最右边的1