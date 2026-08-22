class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        point=intervals[0][1]
        res=0
        for i in range(1,len(intervals)):
            if intervals[i][0]>=point:
                point=intervals[i][1]
            else:
                res+=1
                point=min(intervals[i][1],point)
        return res
#引入point来不断判断，更新，删除即可