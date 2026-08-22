class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        n=len(intervals)
        res=[]
        for i in range(n):
            if intervals[i][1]<newInterval[0]:
                res.append(intervals[i])
            else:
                break
        if newInterval[0]<=intervals[i][1]:
            if newInterval[1]>=intervals[i][0]:
                start=min(intervals[i][0],newInterval[0])
            else:
                res.append(newInterval)
                for j in range(i,n):
                    res.append(intervals[j])
                return res
            if i+1==n:
                end=max(intervals[i][1],newInterval[1])
                res.append([start,end])
                return res
            for j in range(i+1,n):
                if intervals[j][1]>=newInterval[1]:
                    break
            if newInterval[1]>=intervals[j][0]:
                end=max(intervals[j][1],newInterval[1])
                res.append([start,end])
                for k in range(j+1,n):
                    res.append(intervals[k])
            else:
                end=max(newInterval[1],intervals[i][1])
                res.append([start,end])
                for k in range(j,n):
                    res.append(intervals[k])
            return res
        if newInterval[0]>intervals[i][1]:
            start=newInterval[0]
            if i+1==n:
                end=max(intervals[i][1],newInterval[1])
                res.append([start,end])
                return res
            for j in range(i+1,n):
                if intervals[j][1]>=newInterval[1]:
                    break
            if newInterval[1]>=intervals[j][0]:
                end=max(intervals[j][1],newInterval[1])
                res.append([start,end])
                for k in range(j+1,n):
                    res.append(intervals[k])
            else:
                end=max(newInterval[1],intervals[i][1])
                res.append([start,end])
                for k in range(j,n):
                    res.append(intervals[k])
            return res
#这个代码太烂了，别这么写
class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        n = len(intervals)
        
        # 1. 处理左侧完全不重叠的区间
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        # 2. 处理重叠区间，并不断更新 newInterval 的边界
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 将合并后的新区间放入结果
        res.append(newInterval)
        
        # 3. 处理右侧完全不重叠的区间
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
#手动更新处理重叠区间，用while，只关注初态末态避免多次分类讨论