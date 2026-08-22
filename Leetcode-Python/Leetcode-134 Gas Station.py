#解法一
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        tank=0
        start=0
        start_list=[]
        if sum(gas)<sum(cost):
            return -1
        for i in range(n):
            if gas[i]>=cost[i]:
                start_list.append(i)
        n1=len(start_list)
        m=0
        while m<n1:
            start=start_list[m]
            tank=gas[start]
            should_stop=False
            for i in range(start,n):
                tank-=cost[i]
                if tank<0:
                    m+=1
                    should_stop=True
                    break
                if i<n-1:
                    tank+=gas[i+1]
                if i==n-1:
                    tank+=gas[0]
            if not should_stop:
                should_return=True
                for i in range(start):
                    tank-=cost[i]
                    if tank<0:
                        m+=1
                        should_return=False
                        break
                    tank+=gas[i+1]
                if should_return:
                    return start
        return -1    
#这个解法时间复杂度是n2(平方)，因为把所有的都遍历了一遍，虽然前面有些剪枝操作，但其实整体还是偏复杂

#解法二(更优的贪心算法)
#贪心算法：现在的体会是一般开始前要通过一些数学或者逻辑分析来得到或排除一些情况，来减少时间复杂度
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n=len(gas)
        total,tank=0,0
        start=0
        for i in range(n):
            diff=gas[i]-cost[i]
            tank+=diff
            total+=diff
            if tank<0:
                start=i+1
                tank=0
        return start if total>=0 else -1
#这个的几个核心思路：1.只要total>=0，就一定可以找到，并且出发点是油量最低点(结合数学图像思考分析)
                #  2.如果i-j的total<0了，那这一段上的任何一个点都不适合做出发点,此时start=j+1
                #  3.这样只用遍历一遍就可以搞定