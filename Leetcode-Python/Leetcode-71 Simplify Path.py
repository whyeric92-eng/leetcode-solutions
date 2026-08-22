class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        cur=path.split("/")
        stack=[]
        res=""
        for char in cur:
            if char=="" or char==".":
                continue
            elif char=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        if not stack:
            return "/"
        for char in stack:
            res=res+"/"+char
        return res
#这道题一个比较巧妙的地方就是先用"/"把path分隔开来
#这样再对于每个directory进行处理，分情况讨论即可