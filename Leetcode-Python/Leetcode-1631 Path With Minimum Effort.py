import heapq
class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        INF = float('inf')
        effort = [[INF] * col for _ in range(row)]
        effort[0][0] = 0
        queue = [(0, (0, 0))]
        heapq.heapify(queue)
        while queue:
            e, temp = heapq.heappop(queue)
            if effort[temp[0]][temp[1]] < e:
                continue
            for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new = (temp[0] + move[0], temp[1] + move[1])
                if 0 <= new[0] < row and 0 <= new[1] < col:
                    ne = max(e, abs(heights[new[0]][new[1]] - heights[temp[0]][temp[1]]))
                    if ne < effort[new[0]][new[1]]:
                        effort[new[0]][new[1]] = ne
                        heapq.heappush(queue, (ne, new))
        return effort[row-1][col-1]
#dijkstra的变式 不是找min path，其实只有更新那一步的判断需要改