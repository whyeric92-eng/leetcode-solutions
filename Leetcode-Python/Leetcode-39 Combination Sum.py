#解法一
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        n=len(candidates)
        res=[]
        def backtrack(path,index):
            if index<n:
                path.append(candidates[index])
                sum_v=sum(path)
                if sum_v<target:
                    backtrack(path,index)
                if sum_v==target:
                    res.append(path[:])
                    path.pop()
                    if path:
                        a=path.pop()
                    else:
                        return res
                    sum_v=sum(path)
                    backtrack(path,candidates.index(a)+1)
                if sum_v>target:
                    path.pop()
                    if path:
                        a=path.pop()
                    else:
                        return res
                    sum_v=sum(path)
                    backtrack(path,candidates.index(a)+1)
                return res
            else:
                if path:
                    a=path.pop()
                    backtrack(path,candidates.index(a)+1)
                else:
                    return 
        return backtrack([],0)
#这个解法其实就是根据自己做这类题时的思路，类似于画树状图的思路，来编写程序
#几个需要注意的点：1.题目中未说明一定是按顺序的，需要先sort
#2.复制path的时候，用path[:]，因为列表是mutable的，所以后续变化会产生影响，必须复制，用[:]
#3.撤销两次的情况需要考虑到还能不能继续撤销，用if先判断一下
#4.a=path.pop()这样可以赋值的，并且同时也有删除的作用
#5.list.index(a)这个就是a在list中的index的意思
#6.处处严谨，啥时候推进啥时候不推进
#***最难想的一点就是index=n时该怎么处理：如果说path为空了（上一个删的是list的最后一个，path的第一个），那确实没了；path还有，那就应该删掉然后再推进***

#解法二
class Solution(object):
    def combinationSum(self, candidates, target):
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
                path.append(candidates[i])
                backtrack(path,i,remain-candidates[i])
                path.pop()
            return res
        backtrack([],0,target)
        return res
#这个解法明显就要简洁不少，整体性好很多
#怎么想到这个方法的呢？1.用remain来代替自己写法中的判断的步骤(直接将remain与0作比较) 2.剪枝的思路 3.for循环以及配合start和n的运用
#这种方法我现在感觉最多是看得懂，但自己想要写出完整性这么高的代码还得努力