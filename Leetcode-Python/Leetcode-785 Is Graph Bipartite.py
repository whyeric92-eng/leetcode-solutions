class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        for start in range(n):
            q = [(start, True)]
            color = [2] * len(graph)
            visited = [False] * len(graph)
            while q:
                temp = q.pop(0)
                if color[temp[0]] == 2:
                    color[temp[0]] = 1 if temp[1] else 0
                elif color[temp[0]] == 1 and not temp[1]:
                    return False
                elif color[temp[0]] == 0 and temp[1]:
                    return False
                if not visited[temp[0]]:
                    for v in graph[temp[0]]:
                        q.append((v, not temp[1]))
                    visited[temp[0]] = True 
        return True
#可以AC 但是很慢 太多重复操作 (没必要这样来处理unconnected graph)

from collections import deque

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1] * n                  # 放在循环外面

        for start in range(n):
            if color[start] != -1:        # 已处理过的连通块,跳过
                continue
            color[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True