class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pair={')':'(',']':'[','}':'{'}
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or stack[-1]!=pair[char]:
                    return False
                else:
                    stack.pop()
        return not stack
#解法：stack(栈)
#用于判断括号是否合理：左括号，添加；如果说是右括号，那就必须与最近的左括号（当前stack的最后一个）对应（也有可能现在stack为[]，直接输出False）
#如果不？False，对应？删掉对应的左括号
#这样子的话，到最后，如果是合理的，那stack就应该是一个[]