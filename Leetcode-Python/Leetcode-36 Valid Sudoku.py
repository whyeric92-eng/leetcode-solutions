class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def square(x,y):
            hashtable={}
            for i in range(3):
                for j in range(3):
                    char=board[x+i][y+j]
                    if char.isdigit():
                        if hashtable and char in hashtable:
                            return False
                        hashtable[char]=1
            return True
        def row(x):
            hashtable={}
            for i in range(9):
                char=board[x][i]
                if char.isdigit():
                    if hashtable and char in hashtable:
                        return False
                    hashtable[char]=1
            return True
        def col(x):
            hashtable={}
            for i in range(9):
                char=board[i][x]
                if char.isdigit():
                    if hashtable and char in hashtable:
                        return False
                    hashtable[char]=1
            return True
        res=True
        for i in range(9):
            res=res*row(i)*col(i)
        for i in range(0,9,3):
            for j in range(0,9,3):
                res*=square(i,j)
        return True if res==1 else False
#另解：一次走私，3个set(col,row,squaer_id)，每次判定一下即可，一次遍历搞定
class Solution(object):
    def isValidSudoku(self, board):
        # 初始化 9 个集合，分别存放每一行、每一列、每一个九宫格已有的数字
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # 跳过空格
                if val == '.':
                    continue
                
                # 计算当前格子属于哪个九宫格 (0-8)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # 核心逻辑：如果在对应的行、列或块中已经见过这个数字，则无效
                if (val in rows[r] or val in cols[c] or val in boxes[box_idx]):
                    return False
                
                # 否则，把数字存入三个对应的集合中
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True