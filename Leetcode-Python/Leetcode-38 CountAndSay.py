#recursion
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        count=0
        countSay=self.countAndSay(n-1)
        temp=countSay[0]
        res=""
        for i in range(len(countSay)):
            if countSay[i]==temp:
                count+=1
            else:
                res=res+str(count)+str(temp)
                temp=countSay[i]
                count=1
        res=res+str(count)+str(temp)
        return res
#iteration
class Solution(object):
    def countAndSay(self, n):
        res = "1"
        # 使用迭代代替递归，更省内存
        for _ in range(n - 1):
            next_res = []
            i = 0
            while i < len(res):
                count = 1
                # 内部循环直接找连续相同的字符
                while i + 1 < len(res) and res[i] == res[i+1]:
                    i += 1
                    count += 1
                next_res.append(str(count))
                next_res.append(res[i])
                i += 1
            res = "".join(next_res)
        return res
#同时用list存，最后转str，可以提高space complexity