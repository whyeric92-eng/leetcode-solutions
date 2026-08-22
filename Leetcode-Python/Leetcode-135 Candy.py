#解法一
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            res[i]=1
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
            if ratings[i]<ratings[i-1] and res[i-1]==1:
                res[i-1]+=1
                for j in range(i-2,-1,-1):
                    if (ratings[j]<=ratings[j+1] and ratings[j]<=ratings[j-1]) or (ratings[j]>ratings[j+1] and res[j]>res[j+1]) or (ratings[j]==ratings[j+1]) or (ratings[j]<ratings[j+1] and res[j]<res[j+1]):
                        break
                    else:
                        res[j]+=1
        return sum(res)
#这个解法的时间复杂度是O(N2),较为复杂，因为我只想着从右往左算，然后加入了一大堆判定的条件，过于复杂了
#而且这个算法容易遗漏掉很多种情况，我自己也是改了很多次才改出来
#给一个debug的方法，自己按着自己编程的思路去试着运行一下，看看哪一步会出问题

#解法二
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                res[i]=res[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                res[i]=max(res[i],res[i+1]+1)
        return sum(res)
#这个解法的时间复杂度是O(N),因为这个是从左往右和从右往左同时检查，时间复杂度会小很多
#*******一个小启示：其实很多题都是从左往右同时从右往左同事遍历来减小时间复杂度，很多题都可以从这个角度入手来思考