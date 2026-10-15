import heapq
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        INF = float('inf')
        def judge(a, b):
            n = len(a)
            count = 0
            for i in range(n):
                if a[i] != b[i]:
                    count += 1
            return count == 1
        hash_table = {}
        for word in wordList:
            hash_table[word] = [w for w in wordList if judge(w, word)]
        hash_table[beginWord] = [w for w in wordList if judge(w, beginWord)]
        dist = {}
        for word in wordList:
            dist[word] = INF
        dist[beginWord] = 1
        queue = [(1, beginWord)]
        heapq.heapify(queue)
        while queue:
            _ , u = heapq.heappop(queue)
            for word in hash_table[u]:
                if dist[word] > dist[u] + 1:
                    dist[word] = dist[u] + 1
                    heapq.heappush(queue, (dist[word], word))    
        return 0 if dist[endWord] == INF else dist[endWord]
#用dijkstra算法解决 但是会TLE 建表那一步太复杂

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        while queue:
            u, d = queue.popleft()
            if u == endWord:
                return d
            for i in range(len(u)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    v = u[:i] + c + u[i+1:]
                    if v in words and v not in visited:
                        visited.add(v)
                        queue.append((v, d + 1))
        return 0
#直接BFS其实就可以了