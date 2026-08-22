class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        if n==1:
            return True
        elif n%2==0:
            return self.isPowerOfTwo(n//2)
        else:
            return False
#这题挺简单的，注意一下要加上n<1的判断条件
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and n&(n-1)==0
#用bit manipulation来解题，简洁