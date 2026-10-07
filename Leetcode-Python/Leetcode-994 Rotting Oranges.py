class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        step = 0
        m = len(grid)
        n = len(grid[0])
        rotten = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        while rotten:
            temp = rotten.pop(0)
            r = temp[0]
            c = temp[1]
            for rr,cc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= rr < m and 0 <= cc < n:
                    if grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        rotten.append((rr,cc,temp[2]+1))
                        fresh -= 1
                        step = max(step, temp[2]+1)
        return step if fresh == 0 else -1
#大体思路就是先把rotten的入队 然后记录fresh的数量 对于rotten进行BFS(每一个需要记录自己的位置+step)

#一些改进
from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1

        step = 0
        while queue:
            r, c, t = queue.popleft()
            for rr, cc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 1:
                    grid[rr][cc] = 2
                    fresh -= 1
                    step = t + 1
                    queue.append((rr, cc, step))
        return step if fresh == 0 else -1