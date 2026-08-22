#解法一
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        step=0
        path=0
        while True:
            if path>=n-1:
                    return step
            max_forward=0
            for i in range(1,nums[path]+1):
                if path+i>=n-1:
                    step+=1
                    return step
                elif nums[path+i]+i>max_forward:
                    forward=i
                    max_forward=nums[path+i]+i
            path+=forward
            step+=1
#这个解法的思路和Jump Game的解法一很像，但这道题用这个就很合适，因为要找最短的step，所以要找每个最有潜力的那个step
#需要注意的地方：1.，每个循环判定优先 2.防止index溢出 3.最多前进nums[path]，所以range还要+1 4.return和break到底选哪个想清楚