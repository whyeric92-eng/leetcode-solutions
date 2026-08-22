class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def backtrack(start, temp):
            if len(temp) == k:
                res.append(list(temp))
                return 
            #判定条件，是否终止
            for i in range(start, n + 1):
                temp.append(i)
                #做出决策
                backtrack(i + 1, temp)
                #进入backtrack，一路到底
                temp.pop()
                #撤销决策
        
        backtrack(1, [])
        return res
#backtrack本质是一种DFS