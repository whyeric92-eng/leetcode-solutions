from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        while row < m and col >= 0:
            while col >= 0 and target < matrix[row][col]:
                col -= 1
            if col < 0:
                return False
            if matrix[row][col] == target:
                return True
            while row < m and target > matrix[row][col]:
                row += 1
            if row >= m:
                return False
            if matrix[row][col] == target:
                return True
        return False

#思路很简单,比某一列的开头小 这一列都否 左移
#该循环结束时 就会比当前row/col锁定出来的那个大，就可以进入下一个循环
#比某一行的最后大 这一行都否
#通过边界条件(index error)来决定是否退出循环

#时间复杂度为O(n)