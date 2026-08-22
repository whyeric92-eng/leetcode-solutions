class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def backtrack(k,temp,start):
            if len(temp)==k:
                res.append(temp[:])
                return 
            if temp:
                start=nums.index(temp[-1])
            for num in nums[start:]:
                if not temp or num!=temp[-1]:
                    temp.append(num)
                else:
                    continue
                backtrack(k,temp,start)
                temp.pop()
            return res
        for i in range(len(nums)+1):
            backtrack(i,[],0)
        return res
#这个方法有点繁杂，而且每次传入了不必要的参数-start
class Solution(object):
    def subsets(self, nums):
        res = []
        def backtrack(start, temp):
            res.append(temp[:]) # 收集当前子集
            
            for i in range(start, len(nums)):
                temp.append(nums[i])
                # 关键：直接把 i + 1 传给下一层，这就是下一层的 start
                backtrack(i + 1, temp) 
                temp.pop()
                
        backtrack(0, [])
        return res
#这个方法挺好的，每次就收集当前子集，然后通过range来控制不重复