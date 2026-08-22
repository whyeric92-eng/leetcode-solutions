from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        # 返回值为 None：答案是靠拼路径得到的（走到底就把 path 塞进 res），
        # 不是靠子问题结果合并得到的（那种情况才需要 dfs 有返回值，比如树形 dp）。
        def backtrack(start,remain,path):
            if len(path)==k:
                if remain==0:
                    res.append(path[:])
                return 
            for num in range(start,10):
                path.append(num)
                backtrack(num+1,remain-num,path)
                path.pop()
        backtrack(1,n,[])
        return res