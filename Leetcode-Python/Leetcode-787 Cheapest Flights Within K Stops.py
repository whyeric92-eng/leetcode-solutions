class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0
        for _ in range(k+1):
        #最多k stops 即(k+1)条边
            new = dist[:]
            for u,v,w in flights:
                if dist[u] != INF and new[v] > dist[u] + w:
                    new[v] = dist[u] + w
            dist = new
        #用快照来实现原子更新
        return dist[dst] if dist[dst] != INF else -1   