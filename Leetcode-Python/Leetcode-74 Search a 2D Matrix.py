class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row=len(matrix)
        col=len(matrix[0])
        def convert(index):
            r=index//col
            c=index%col
            return matrix[r][c]
        start=0
        end=row*col-1
        while start<=end:
            mid=(start+end)//2
            if convert(mid)==target:
                return True
            elif convert(mid)>target:
                end=mid-1
            else:
                start=mid+1
        return False