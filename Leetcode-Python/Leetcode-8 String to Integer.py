class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=[]
        lst=[char for char in s]
        for char in lst:
            if char==" " and not res:
                continue
            elif char.isdigit():
                res.append(char)
            elif (char=="-" or char=="+") and not res:
                res.append(char)
                res.append("0")
            else:
                break
        out=int("".join(res)) if res else 0
        if out>2**31-1:
            out=2**31-1
        if out<-2**31:
            out=-2**31
        return out
#几个注意要点：1." "这种不算是空的 2." "啥时候该忽略，啥时候不该，考虑清楚 3.int("042")--42,0不需要特殊处理