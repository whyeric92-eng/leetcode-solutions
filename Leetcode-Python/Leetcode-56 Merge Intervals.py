#解法一
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        def check_inter(intervals):
            inter=False
            i=0
            if len(intervals)==1:
                return False,intervals
            else:
                while i<len(intervals)-1:
                    if intervals[i][1]>=intervals[i+1][0]:
                        inter=True
                        intervals[i:i+2]=[[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]]
                    i+=1
                return inter,intervals
        while True:
            inter,intervals=check_inter(intervals)
            if not inter:
                return intervals
            if inter:
                continue
#这个解法的思路较为简单，但是时间复杂度高，思路就是一个一个判断，判断完一次后继续判断下一次，中途用True/False来标记
#注意的情况：1.[1,4] [2,3]这种完全包住的 2.[[1,3]]这种就一个的 
#3.采用的方法是intervals[i:i+2]，替换这个切片，这导致len(intervals)一直在变，建议用while手动调节

#解法二
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i:i+2]=[[intervals[i][0],max(intervals[i][1],intervals[i+1][1])]]
            else:
                i+=1
        return intervals
#时间复杂度有降低，if intervals[i][1]>=intervals[i+1][0]:类似于一个循环，会一直判断，直到无法合并

#解法三
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        merge=[]
        for interval in intervals:
            if not merge or merge[-1][1]<interval[0]:
                merge.append(interval)
            else:
                merge[-1]=[merge[-1][0],max(merge[-1][1],interval[1])]
        return merge
#慢慢模仿吧，挺牛逼的这个方法，最优解了