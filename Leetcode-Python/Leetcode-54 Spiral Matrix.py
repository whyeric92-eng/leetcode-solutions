class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res=[]
        row=len(matrix)
        col=len(matrix[0])
        up,down=0,row-1
        left,right=0,col-1
        while left<=right and up<=down:
            for i in range(left,right+1):
                res.append(matrix[up][i])
            up+=1
            if up>down: break
            for j in range(up,down+1):
                res.append(matrix[j][right])
            right-=1
            if left>right: break
            for i in range(right,left-1,-1):
                res.append(matrix[down][i])
            down-=1
            if up>down: break
            for j in range(down,up-1,-1):
                res.append(matrix[j][left])
            left+=1
        return res
#这道题simulation，其本质就是模拟这个1过程，先右，再下，后左，再上。
#重复这个过程，用up/down/left/right来检测，出现问题及时break(避免重复)