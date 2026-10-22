class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for u, v in edges:
            ru, rv = find(u), find(v)
            if ru == rv:
                return [u,v]
            parent[ru] = rv
            #这个地方一定是把ru的parent给rv (因为ru rv已经是各自的parent了)