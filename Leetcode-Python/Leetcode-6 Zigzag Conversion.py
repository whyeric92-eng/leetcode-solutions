#解法一
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lst_s=[char for char in s]
        new_nums = [[] for _ in range(numRows)]
        output_nums=[]
        i=0
        if numRows==1:
            return s
        while i<numRows:
            for k in range(len(lst_s)):
                if k%(2*numRows-2)==i or k%(2*numRows-2)==2*numRows-2-i:
                    new_nums[i].append(lst_s[k])
            i+=1
        for i in range(numRows):
            output_nums.extend(new_nums[i])
        return "".join(map(str,output_nums))
#注意：new_nums = [[] for _ in range(numRows)] 这样才是创建了numRows个空列表
      #注意[]*numRows是不对的，这样依旧是空列表
#解法二
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lst_s=[char for char in s]
        new_nums = [[] for _ in range(numRows)]
        output_nums=[]
        n=numRows
        i=0
        if numRows==1:
            return s
        for k in range(len(lst_s)):
            if k%(2*n-2)<=n-1:
                new_nums[k%(2*n-2)].append(lst_s[k])
            else:
                new_nums[2*n-2-k%(2*n-2)].append(lst_s[k])
        for i in range(numRows):
            output_nums.extend(new_nums[i])
        return "".join(map(str,output_nums))
#微调，让时间复杂度从N方变为N

#解法三
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows=[""]*numRows #这样不是空列表，把""重复了numRows次
        cur=0
        step=-1
        if numRows==1:
            return s
        for c in s:
            rows[cur]+=c
            if cur==0 or cur==numRows-1:
                step*=-1
            cur+=step
        return "".join(rows)
#最快的，实际上也是O(N)，但是少了很多常数计算
#cur和step的用法，学习