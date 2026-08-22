class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix=[[0 for _ in range(n)] for _ in range(n)]
        up,down=0,n-1
        left,right=0,n-1
        count=1
        while up<=down and left<=right:
            for i in range(left,right+1):
                matrix[up][i]=count
                count+=1
            up+=1
            if up>down: break
            for i in range(up,down+1):
                matrix[i][right]=count
                count+=1
            right-=1
            if left>right: break
            for i in range(right,left-1,-1):
                matrix[down][i]=count
                count+=1
            down-=1
            if up>down: break
            for i in range(down,up-1,-1):
                matrix[i][left]=count
                count+=1
            left+=1
        return matrix