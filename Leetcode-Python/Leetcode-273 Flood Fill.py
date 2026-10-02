from queue import Queue
class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        q = Queue(maxsize = 0)
        q.put((sr, sc))
        max_r = len(image)
        max_c = len(image[0])
        visited = [[False] * max_c for _ in range(max_r)]
        while (not q.empty()):
            r, c = q.get()
            temp = image[r][c]
            image[r][c] = color
            visited[r][c] = True
            if r+1 < max_r and not visited[r+1][c] and image[r+1][c] == temp:
                q.put((r+1, c))
            if r-1 >=0 and not visited[r-1][c] and image[r-1][c] == temp:
                q.put((r-1, c))
            if c+1 < max_c and not visited[r][c+1] and image[r][c+1] == temp:
                q.put((r, c+1))
            if c-1 >= 0 and not visited[r][c-1] and image[r][c-1] == temp:
                q.put((r, c-1))
        return image
#很慢 选错了 不应该用Queue

#BFS
from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if old == color:          # 关键:新旧颜色相同,什么都不用做
            return image

        rows, cols = len(image), len(image[0])
        image[sr][sc] = color     # 入队时就涂色,相当于标记
        q = deque([(sr, sc)])

        while q:
            r, c = q.popleft()
            for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == old:
                    image[nr][nc] = color   # 入队时涂色
                    q.append((nr, nc))
        return image

#DFS
class Solution:
    def floodFill(self, image, sr, sc, color):
        old = image[sr][sc]
        if old == color:
            return image

        def dfs(r, c):
            if not (0 <= r < len(image) and 0 <= c < len(image[0])) or image[r][c] != old:
                return
            image[r][c] = color
            dfs(r+1, c); dfs(r-1, c); dfs(r, c+1); dfs(r, c-1)

        dfs(sr, sc)
        return image