#解法一
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        small=nums[0]
        medium_exist=False
        for i in range(1,n):
            if nums[i]<small:
                small=nums[i]
            elif nums[i]>small and not medium_exist:
                medium=nums[i]
                medium_exist=True
            elif medium_exist and nums[i]>small and nums[i]<medium:
                medium=nums[i]
            elif medium_exist and nums[i]>medium:   #关键：更新small不会影响现在已经有的medium的有效性
                return True
        return False
#就是贪心，目前遇到的最小的当成small，第二小的当成medium

#解法二
def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')
    
    for n in nums:
        if n <= first:
            # 遇到了更小的数，更新最小值
            first = n
        elif n <= second:
            # n 比 first 大，但比 second 小，
            # 说明找到了一个更适合做"中间值"的数
            second = n
        else:
            # n 比 first 和 second 都大
            # 也就是找到了: first < second < n
            return True
            
    return False

#贪心就是一直寻找最优解