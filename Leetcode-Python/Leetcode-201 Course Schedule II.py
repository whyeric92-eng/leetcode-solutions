from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph= [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        visited = [0]*numCourses
        def dfs(node,path):
            if visited[node]==1:
                return False
            elif visited[node]==2:
                return True
            visited[node]=1
            for neighbor in graph[node]:
                if visited[neighbor]==2:
                    pass
                elif not dfs(neighbor,path):
                    return False
            visited[node]=2
            path.append(node)
            return True
        path=[]
        for i in range(numCourses):
            if not dfs(i,path):
                return []
        return path
#已完成检查的，visited[node]==2的时候，就不应该append或者跑一次dfs了，代表此时的node应该已经在path里面了

#根据依赖关系，会一直调用dfs(node),只有全部结束了才会调用append (就是这个节点"最后一个依赖也搞定了"的时刻，而这个时刻天然就应该排在后)