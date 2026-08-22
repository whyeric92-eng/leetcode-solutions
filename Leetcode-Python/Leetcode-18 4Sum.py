#解法一
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        output=[]
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        output.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left +=1
                        while left<right and nums[right]==nums[right-1]:
                            right -=1
                        left +=1
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]>target:
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left +=1
        return output
#解法二
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        output=[]
        if n<4:
            return output
        for i in range(n-3):
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                return output
            if nums[i]+nums[n-1]+nums[n-2]+nums[n-3] < target:
                continue
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i]+nums[j]+nums[n-2]+nums[n-1]< target:
                    continue
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=n-1
                while left<right:
                    if nums[i]+nums[j]+nums[left]+nums[right]==target:
                        output.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left +=1
                        while left<right and nums[right]==nums[right-1]:
                            right -=1
                        left +=1
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]>target:
                        right-=1
                    elif nums[i]+nums[j]+nums[left]+nums[right]<target:
                        left +=1
        return output
#总结：两个解法本质是一样的，但解法二快很多，因为多了“剪枝”这个步骤
#剪枝：提前排除一些很显然不成立的情况：1.长度小于4的话，直接输出[] 2.理论最小已经更大-退出当前循环/此种情况理论最大还更小，i+=1
#细节：1.return output(结束该项目了直接) vs break(只是退出当前循环)
    #2.第二个j那里避免重复的情况，判断条件为j>i+1,因为j=i+1的时候没必要排除nums[j]==nums[i]的情况