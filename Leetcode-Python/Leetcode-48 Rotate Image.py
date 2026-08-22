#方法一
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix1 = [row[:] for row in matrix] #不可以matrix1=matrix(这样两个一起在改)
        n=len(matrix)
        for i in range(1,n+1):
            for j in range(1,n+1):
                matrix[j-1][n-i]=matrix1[i-1][j-1]

#方法二
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 1. Transpose: 沿主对角线交换元素
        for i in range(n):
            # 注意这里从 i 开始，是为了避免重复交换（只遍历对角线右上方）
            for j in range(i, n):
                # 互换 matrix[i][j] 和 matrix[j][i]
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse: 每一行左右翻转
        for i in range(n):
            # Python 的列表自带 reverse() 方法，是原地修改
            matrix[i].reverse()
#这个方法偏数学一点，就是先对角线换(注意只用遍历右上角)，然后inverse即可
#这个数学方法其实可以从法一的结论看出来