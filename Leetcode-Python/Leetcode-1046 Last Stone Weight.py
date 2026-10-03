import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-s for s in stones]
        # 需要取负数 因为是min-heap
        heapq.heapify(heap)
        while len(heap) > 1:
            x = heapq.heappop(heap)   # 最大(负值最小)
            y = heapq.heappop(heap)   # 第二大
            if x != y:
                heapq.heappush(heap, x - y)  # x ≤ y ≤ 0,x-y 即 -(|x|-|y|)
        return -heap[0] if heap else 0