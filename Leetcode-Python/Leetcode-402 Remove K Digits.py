class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in range(len(num)):
            while k>0 and stack and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
        if k>0:
            stack=stack[:-k]
        result = "".join(stack).lstrip('0')
        return result if result else "0"
#可以可以，基本上大体思路，最关键的while循环都是自己搞定的
#这道题要充分理解栈(stack)本质
#几个易错点：1.开始自己还写了一个elif i<len(num)-1 and k>0 and num[i]>num[i+1]:k-=1 这样是错的，有可能这个不入栈的也比现在在栈里面的大！！！
           #2.关于删掉最开始的0：result = "".join(stack).lstrip('0')这样写最好
           #3.有些看似是特殊情况需要特殊处理，可以自己用自己的代码判断一下能不能避免，保证简洁性