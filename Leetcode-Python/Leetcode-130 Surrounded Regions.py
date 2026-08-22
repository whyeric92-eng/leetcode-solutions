class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def dfs(i,j):
            if i<0 or i>m-1 or j<0 or j>n-1 or board[i][j]!="O":
                return 
            board[i][j]="C"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1) 
        for j in range(n):
            dfs(0, j)     
            dfs(m - 1, j)  
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "C":
                    board[i][j] = "O"
#这道题就是考察对于dfs更深入的理解了
#一个非常关键的处理就是先把所有是O的全变成C，并且尝试阻断路径(判断方式就是不是O就返回---X和C都会返回)
#然后从4条边上开始dfs
#最后拉通来看，如果还是O，就代表没有联通(变成X)，如果变成C，代表和边上的O有联通，应该变成O