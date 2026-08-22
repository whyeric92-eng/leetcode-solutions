#解法一
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        lst=["(",")"]*n
        used=[False]*len(lst)
        def isvalid(s):
            stack=[]
            for char in s:
                if char=="(":
                    stack.append(char)
                else:
                    if not stack or stack[-1]!="(":
                        return False
                    else:
                        stack.pop()
            return not stack
        def backtrack(path):
            if len(path)==2*n:
                if ("".join(path)) not in res and isvalid("".join(path)):
                    res.append("".join(path))
                    return
                else:
                    return
            for i in range(len(lst)):
                if used[i]:
                    continue
                used[i]=True
                path.append(lst[i])
                backtrack(path)
                path.pop()
                used[i]=False
        backtrack([])
        return res
#解法二
#合法括号的逻辑是：只有左括号多于右括号时，才可以添加右括号
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        def backtrack(path,left,right):
            if len(path)==2*n:
                res.append("".join(path))
            if left<n:
                path.append("(")
                backtrack(path,left+1,right)
                path.pop()
            if right<left:
                path.append(")")
                backtrack(path,left,right+1)
                path.pop()
            return res
        return backtrack([],0,0)
#使用backtracking，核心点是：1.只要left<n的，就可以继续推进，加左括号 2.left>right的话，就可以选择加右括号
#越来越感觉到其实backtracking的推进是靠在下一次调用backtracking时对变量进行+1/-1（***变量的选取至关重要）