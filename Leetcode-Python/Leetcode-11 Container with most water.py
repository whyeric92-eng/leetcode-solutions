#解法：Greedy
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        max_area=0
        while left<right:
            area=(right-left)*min(height[left],height[right])
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
#现在对于贪心算法的初步理解：贪心算法并非是不严谨，而是类似于通过一些数学变化来排除一些不必要的计算
#感觉这种一般是可以用for循环暴力拆解来做的(但是一般这个都会超出时间复杂度)