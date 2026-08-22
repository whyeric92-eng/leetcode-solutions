class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        def dfs(a,b):
            if a<0 or a>m-1 or b<0 or b>n-1 or grid[a][b]=="0":
                return 
            grid[a][b]="0"
            dfs(a-1,b)
            dfs(a+1,b)
            dfs(a,b-1)
            dfs(a,b+1)
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    count+=1
                    dfs(i,j)
        return count
#这个有点Recursion的感觉，dfs(a,b)--dfs(a+/-1,b),dfs(a,b+/-1)，相当于一直传递下去
#关于depth-first search，这个实际上就是利用递归(Recursion)来实现遍历