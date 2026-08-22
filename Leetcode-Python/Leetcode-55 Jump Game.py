#解法一
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        path=0
        while True:
            x=nums[path]
            if path+x>=n-1:
                return True
            elif x==0:
                return False
            else:
                maxlen=nums[path]
                forward=0
                for i in range(x):
                    if nums[path+i]+i>maxlen:
                        maxlen=nums[path+i]+i
                        forward=i
                if path+maxlen>=n-1:
                    return True
                if forward==0:
                    path+=maxlen
                if forward!=0:
                    path+=forward
#这种解法就是最最基础的贪心算法，每一步都是做当前最优解
#注意点：*******很多次都在循环内定义变量，这样不对！！！这样相当于每次都在重置，应该在循环外定义初始变量

#解法二
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        max_reach=0
        for i in range(n):
            if i>max_reach:
                return False
            max_reach=max(max_reach,i+nums[i])
            if max_reach>n-1:
                return True
        return True
#这种解法确实快而且简洁
#max_reach理解为现在可以到达的最远距离，如果i>max_reach，意味着路径被阻断，返回False
#感觉不太容易想到，多模仿多学习