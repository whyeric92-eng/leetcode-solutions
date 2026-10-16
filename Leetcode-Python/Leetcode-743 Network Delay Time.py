import heapq
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        networks = [[] for _ in range(n+1)]
        INF = float('inf')
        for time in times:
            networks[time[0]].append((time[1], time[2]))
        dist = [INF] * (n+1)
        dist[k] = 0
        queue = [(0, k)]
        heapq.heapify(queue)
        in_queue = [False] * (n+1)
        res = 0
        while queue:
            temp, u = heapq.heappop(queue)
            if in_queue[u]:
                continue
            in_queue[u] = True
            res = max(res, temp)
            #注意要放在in_queue判断之后
            for v, d in networks[u]:
                if dist[v] > dist[u] + d:
                    dist[v] = dist[u]+ d
                    heapq.heappush(queue, (dist[v], v))
        return res if in_queue[1:n+1] == [True]*n else -1
#标准dijkstra算法 heap实现+lazy deletion

#不用in_queue 也可以判断 更简洁
# temp, u = heapq.heappop(queue)
# if temp > dist[u]:
#     continue
# res = max(res, temp)