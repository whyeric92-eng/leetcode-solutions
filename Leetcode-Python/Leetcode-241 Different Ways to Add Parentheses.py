from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        if expression.isdigit():
            return [int(expression)]
        table = {}
        for i in range(len(expression)):
            if not expression[i].isdigit():
                table[i] = expression[i]
        for index, temp in table.items():
            temp = expression[index]
            left = self.diffWaysToCompute(expression[:index])
            right = self.diffWaysToCompute(expression[index+1:])
            if temp == "+":
                res.extend([a+b for a in left for b in right])
            elif temp == "-":
                res.extend([a-b for a in left for b in right])
            else:
                res.extend([a*b for a in left for b in right])
        return res
#先说思路 这道题看似是加括号 本质其实是divide and conquer 
#遍历expression 根据运算符可以分成左右两边 分别调用自身函数 生成对应的[res] 然后再合并计算

#上面那个写法有点冗长 table完全没有必要
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                if ch == "+":
                    res.extend([a+b for a in left for b in right])
                elif ch == "-":
                    res.extend([a-b for a in left for b in right])
                else:
                    res.extend([a*b for a in left for b in right])
        return res
    
#可以加上记忆化
from typing import List
from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(maxsize=None)
        # 缓存子问题结果,避免相同子串被重复计算
        def compute(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]
            
            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    if ch == "+":
                        res.extend([a+b for a in left for b in right])
                    elif ch == "-":
                        res.extend([a-b for a in left for b in right])
                    else:
                        res.extend([a*b for a in left for b in right])
            return res
        
        return compute(expression)