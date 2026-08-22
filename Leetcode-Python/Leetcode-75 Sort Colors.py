#解法
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0,count_1,count_2=0,0,0
        for num in nums:
            if num==0:
                count_0+=1
            elif num==1:
                count_1+=1
            else:
                count_2+=1
        nums[:]=[0]*count_0+[1]*count_1+[2]*count_2
#注意：最后用[0]*count_0这种来表示很多个0