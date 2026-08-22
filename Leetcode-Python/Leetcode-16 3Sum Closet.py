class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def closer(cur_sum,target,new_sum):
            if abs(new_sum-target)<abs(cur_sum-target):
                cur_sum=new_sum
            return cur_sum
        n=len(nums)
        nums.sort()
        cur_sum=nums[0]+nums[1]+nums[2]
        if nums[0]+nums[1]+nums[2]>=target:
            return nums[0]+nums[1]+nums[2]
        elif nums[-1]+nums[-2]+nums[-3]<=target:
            return nums[-1]+nums[-2]+nums[-3]
        else:
            for i in range(n-2):
                left=i+1
                right=n-1
                while left<right:
                    new_sum=nums[i]+nums[left]+nums[right]
                    cur_sum=closer(cur_sum,target,new_sum)
                    if new_sum>target:
                        right -=1
                    if new_sum<target:
                        left +=1
                    if new_sum==target:
                        return target
            return cur_sum
#这题解法也是O(n2)，但是最开始只beat 5%，后面beat 98% 原因其实在于自己在最前面加了两行判断条件，这是对于如果target比较极端的情况，这样可以直接输出
#启示：有时候缩短run time，不一定要从时间复杂度开始降，每一个可能减少run time的机会都不要放过（如排除极端情况等等）
#注意点：cur_sum的定义，一定要仔细，在for循环外定义，不然每次循环被重置一次