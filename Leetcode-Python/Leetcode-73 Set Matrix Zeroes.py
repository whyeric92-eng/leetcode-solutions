class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[]
        col=[]
        for i in range(m):
            if 0 in matrix[i]:
                row.append(i)
        for i in row:
            for j in range(n):
                if matrix[i][j]==0:
                    col.append(j)
        for r in row:
            matrix[r]=[0]*n
        for c in col:
            for j in range(m):
                matrix[j][c]=0
        return matrix
#这个方法空间复杂度略高，O(m+n)，不够好
class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # 1. 检查第一行和第一列是否原本就有 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # 2. 利用第一行和第一列存储其余部分的 0 情况
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3. 根据第一行和第一列的标记，将对应的内部元素置 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4. 最后处理第一行和第一列
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0