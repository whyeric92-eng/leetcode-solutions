class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        prev_op = '+'
        n = len(s)

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            # 遇到运算符,或者到达字符串末尾时,结算当前 num
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if prev_op == '+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop() * num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / num))  # 向零截断
                prev_op = char
                num = 0

        return sum(stack)
#和以往那种专门一个stack来记录oper 一个stack来记录数字的不一样 
#这个不是prefix或者postfix 不方便这样遍历
#用prev_op来记录上一个符号 stack来记录数字即可 这个和运算优先级的关系也不大