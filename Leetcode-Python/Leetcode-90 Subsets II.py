class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        def backtrack(path,s):
            if not res or path not in res:
                res.append(path[:])
            for i in range(s,len(nums)):
                num=nums[i]
                path.append(num)
                backtrack(path,i+1)
                path.pop()
        backtrack([],0)
        return res
#每次单独判断path是否在res中不太好
class Solution(object):
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()  # 必须排序，让相同的元素挨在一起
        
        def backtrack(path, s):
            # 每进入一层递归，直接把当前 path 加入结果
            res.append(path[:]) 
            
            for i in range(s, len(nums)):
                # 【核心剪枝逻辑】
                # 如果当前遍历的数字和前一个数字相同，
                # 并且前一个数字在这一层还没有被用过（i > s），直接跳过！
                if i > s and nums[i] == nums[i-1]:
                    continue
                
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
                
        backtrack([], 0)
        return res