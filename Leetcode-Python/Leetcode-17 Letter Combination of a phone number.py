#解法一
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict={'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],
              '6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        n=len(digits)
        output=[]
        if n==1:
            return dict[digits[0]]
        if n==2:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    strr=i+j
                    output.append(strr)
            return output
        if n==3:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    for k in dict[digits[2]]:
                        strr=i+j+k
                        output.append(strr)
            return output
        if n==4:
            for i in dict[digits[0]]:
                for j in dict[digits[1]]:
                    for k in dict[digits[2]]:
                        for m in dict[digits[3]]:
                            strr=i+j+k+m
                            output.append(strr)
            return output
#要点：1.字符串可以直接加法合并 2."23"这是个str，可以直接用长度，以及index处理

#解法二
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict={'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],
              '6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        n=len(digits)
        res=[]
        def backtrack(index,path):
            if index==n:
                res.append("".join(path))
                return
            for char in dict[digits[index]]:
                path.append(char)
                backtrack(index+1,path)
                path.pop()
        backtrack(0,[])
        return res
#用的新方法：backtracking
#理解为：判定？选择，继续选择，撤销选择
#（目前的理解）适用范围：排列问题，一个树，很多分支，我要输出所有分支
#注意的写法：1.res.append("".join(path)) 
# 2.这道题推进的方法较为简单（因为顺序相对固定的，用index，index+1直接简单推进）
# 3.第一处的return，作用就是告诉我们当前分支已经结束，其实不会返回任何值