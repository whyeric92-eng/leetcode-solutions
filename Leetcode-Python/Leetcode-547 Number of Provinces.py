from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = []
        n = len(isConnected)
        for i in range(n):
            group = set()
            for j in range(n):
                if isConnected[i][j] == 1:
                    group.add(j)
            new_province = []
            for p in province:
                if p & group:
                    group |= p      # group = group | p (把p合并进group)        
                else:
                    new_province.append(p) 
            new_province.append(group)       
            province = new_province
        return len(province)
#这道题的思路就是union 用集合来判断是否为现有的province group

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        count = 0
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        return count    
#DFS写法
#DFS一定要想清楚每个dfs是用来干啥的，这道题里面每个dfs就是把和这个省份connected的全部串起来(通过visited数组)
#实际的计数的环节是放在后面的循环里面去完成的