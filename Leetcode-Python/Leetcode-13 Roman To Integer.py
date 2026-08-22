#解法一（用if语句判断）
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        num=0
        for i in range(0,n):
            if s[i]=='I':
                if (i<n-1) and s[i+1] in ('V','X'):
                    #注意点：1.i<n-1，i是index，注意细节！（尤其是端点值）
                    #2.and的优先级高于or，所以说如果要判断or的话，后面打上括号
                    #3.这种写法不对：x=='a' or 'b'
                    num += -1
                else:
                    num +=1
            if s[i]=='V':
                num +=5
            if s[i]=='X':
                if i<n-1 and s[i+1] in ('L','C'):
                    num +=-10
                else:
                    num +=10
            if s[i]=='L':
                num +=50
            if s[i]=='C':
                if i<n-1 and s[i+1] in ('D','M'):
                    num +=-100
                else:
                    num +=100
            if s[i]=='D':
                num +=500
            if s[i]=='M':
                num +=1000
        return num
#解法二（用dictionary）
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n=len(s)
        num=0
        for i in range(n):
            if i<n-1 and roman[s[i+1]]>roman[s[i]]:
                num -=roman[s[i]]
            else:
                num +=roman[s[i]]
        return num
    #用字典处理，更快更便捷