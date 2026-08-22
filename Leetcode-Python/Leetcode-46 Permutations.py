#解法一
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        used=[False]*n
        res=[]
        def backtrack(path):
            if len(path)==n:
                res.append(path[:])
            for i in range(n):
                if used[i]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=False
            return res
        return backtrack([])
#这道题就是最基本的全排列的解法
#主要思路：使用used这个list来标记列表中的某个数字是否使用过，通过true和false来判断接下来的操作
#用过？下一个，没用？（这次用了马上标记为没用）撤销操作？撤销掉的数字标记为没用