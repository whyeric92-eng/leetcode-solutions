#解法一
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n=len(nums)
        used=[False]*n
        res=[]
        def backtrack(path):
            if len(path)==n:
                res.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                if not used[i-1] and i>0 and nums[i]==nums[i-1]:
                    continue
                used[i]=True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i]=False
            return res
        return backtrack([])
#注意点：避免重复！！！！关键是同层次之间避免重复：非常非常巧妙的用法：not used[i-1] 如果这个为True，说明i-1不在，此时i和i-1是同层********