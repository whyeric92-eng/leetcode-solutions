class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre=""
        l=len(strs)
        lst=[]
        cout=0
        attempt=0
        for i in range(0,l):
            lst.append(len(strs[i])) 
        minlen=int(min(lst))
        for i1 in range(0,minlen):
            attempt +=1
            for i2 in range(0,l):
                if strs[i2][i1]==strs[0][i1]:
                    cout +=1
                else:
                    cout +=0
            if cout==l*attempt:
                pre=pre+strs[i2][i1]
            if cout!=l*attempt:
                break
        return pre
#注意点：1.append那一块的使用，我是想把一个int直接送进list里面，所以应该用append
#2.这种写法cout每次没有重置，所以应该每次乘attempt

#简便写法（思路相同）
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre = ""
        l = len(strs)
        minlen = min(len(s) for s in strs)
        #直接用min，同时len(s) for s in strs直接构造函数
        for i in range(minlen):
            char = strs[0][i]
            #其实后面都是拿第一个的作比较，可以直接定义char
            for j in range(1, l):
                if strs[j][i] != char:
                    return pre
                    #简洁：不管啥break了，直接return
            pre += char

        return pre
