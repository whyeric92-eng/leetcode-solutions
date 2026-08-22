#解法一
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=[char for char in str(x)]
        l=len(y)
        cout=0
        for i in range(0,l):
            if y[i]==y[l-1-i]:
                cout +=1
            else:
                cout +=0
        return cout==l
#解法二
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=[char for char in str(x)]
        return s==s[::-1]
#解法三
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=x
        if x<0 or (x%10==0 and x!=0):
            return False
        reversed_num=0
        while x > 0:
            reversed_num=reversed_num*10+x%10
            x//=10
        return a==reversed_num
    #注意点：第一处应该是if，while如果条件是x>0的话，应该保留一个初始的x，因为x在while循环中值会变
#解法四
class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10
    #优点在于只用反转一遍，最后检验是否和//10相等是对于奇数长度的数字