# 方法：DFS + 三色标记法判断有向图是否有环
# 0=未访问, 1=正在当前递归路径上(访问中), 2=已确认无环(访问完成)
# 递归中再次遇到状态1的节点 => 路径绕回自身 => 存在环 => 无法完成所有课程
# 状态2相当于记忆化缓存，避免同一节点被不同路径重复递归验证
#
# 启示：
# 1. "先修关系"本质是有向图的依赖关系，判断能否完成 = 判断图中有无环（拓扑排序是否存在）
# 2. 单纯的 visited 布尔值不够用——图不是树，一个节点可能被多条路径共同依赖，
#    必须区分"正在访问中"和"已彻底访问完"，否则会把"共同依赖"误判成"环"
# 3. 三色标记本质上是给 DFS 加了记忆化，把每个节点的验证结果缓存下来，
#    避免指数级重复计算，是图论里检测环的通用套路（也可用于拓扑排序 Leetcode 210）
# 4. visited 是所有 dfs 调用共用的同一个数组，这是环检测和记忆化两个作用能同时生效的关键
# 5. dfs(node)返回True 与 visited[node]==2 是等价的：visited[node]=2 这一行，
#    本质就是把"dfs(node)该返回True"这个结论缓存下来，供其他路径直接查表复用
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq) 
        visited = [0] * numCourses
        def dfs(node):
            if visited[node]==1:
                return False
            if visited[node]==2:
                return True
            visited[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node]=2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True