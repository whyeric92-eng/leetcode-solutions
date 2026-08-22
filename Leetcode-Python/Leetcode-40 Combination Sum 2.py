#解法一
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res=[]
        n=len(candidates)
        def backtrack(path,start,remain):
            if remain==0:
                res.append(path[:])
                return
            for i in range(start,n):
                if candidates[i]>remain:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(path,i+1,remain-candidates[i])
                path.pop()
            return res
        r=backtrack([],0,target)
        return r
#这道combination sum2 和 1 的区别就在于这个里面的元素只能用一次(但是这里面的元素有可能重复)
#这类题避免重复的思路：1.递归完来判定有没有（但这样极大可能超出时间复杂度）2.sort之后，在for循环那里，如果一样就直接到下一个（和3Sum一样的处理方式）
#在这个函数里面第一个return：这一层已经结束了，只是退出当前这一层递归，不会返回值，不会退出整个程序
#break：不会进行for循环了，返回上一层递归
#******这类题在一个递归周期结束时，返回上一层（这是调用这个函数的地方）*******