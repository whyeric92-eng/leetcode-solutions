import heapq
class Solution:
    def cal(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((self.cal(points[i], points[j]), i, j))
        parent = list(range(len(points)))
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return parent[x]
        res = 0
        for w, u, v in sorted(edges):
            ru = find(u)
            rv = find(v)
            if ru != rv:
                res += w
                parent[ru] = rv
        return res
#Kruskal 有边列表即可 (最适用于稀疏图)

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        dist = [float('inf')] * n   # dist[v]：v 到当前树的最短距离
        visited = [False] * n
        dist[0] = 0
        res = 0
        for _ in range(n):
            # 1. 找树外 dist 最小的点
            u = -1
            for v in range(n):
                if not visited[v] and (u == -1 or dist[v] < dist[u]):
                    u = v
            visited[u] = True
            res += dist[u]
            # 2. 用 u 更新其他点到树的距离（边权现算）
            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    d = abs(x1 - points[v][0]) + abs(y1 - points[v][1])
                    if d < dist[v]:
                        dist[v] = d
        return res
#Prim (最适用于完全图)