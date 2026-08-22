class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row=len(board)
        col=len(board[0])
        def dfs(r,c,path):
            char=board[r][c]
            path=path+char
            if not word.startswith(path):
                return False
            if path==word:
                return True
            board[r][c]="#"
            for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr=r+dr
                nc=c+dc
                if 0<=nr<row and 0<=nc<col and board[nr][nc]!="#":
                    if dfs(nr,nc,path):
                        return True
                    #一定要记得保存dfs结果并return True
            board[r][c]=char
            return False

        for r in range(row):
            for c in range(col):
                if dfs(r,c,""):
                    return True
        return False
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row=len(board)
        col=len(board[0])
        def dfs(r, c, k):
            if k == len(word):
                return True
            if not (0 <= r < row and 0 <= c < col) or board[r][c] != word[k]:
                return False
            temp = board[r][c]
            board[r][c] = "#"
            res = (dfs(r+1, c, k+1) or 
                dfs(r-1, c, k+1) or 
                dfs(r, c+1, k+1) or 
                dfs(r, c-1, k+1))
            board[r][c] = temp
            return res
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
#这个用k，不用每次比较path和word

#这类题目降低runtime最快的方式就是进行剪枝操作，提前终止一些无意义的dfs