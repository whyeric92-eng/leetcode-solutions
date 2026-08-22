class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        def backtrack(start,path):
            if len(path)==4:
                if start==len(s):
                    res.append(".".join(path[:]))
                return 
            for i in range(1,4):
                if start+i>len(s):
                    break
                if int(s[start:start+i])>255 or (i>1 and s[start:start+i][0]=="0"):
                    continue
                #关键的剪枝操作
                path.append(s[start:start+i])
                backtrack(start+i,path)
                path.pop()
        backtrack(0,[])
        return res
#核心思路：确定终止条件->正常做出选择->提前剪枝->撤销选择