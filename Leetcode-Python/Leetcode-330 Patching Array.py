class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss=1
        patch=0
        i=0
        while i<len(nums):
            if miss-1>=n:
                return patch
            if nums[i]<=miss:
                miss+=nums[i]
                i+=1
            else:
                miss*=2
                patch+=1
        while miss-1<n:
            miss*=2
            patch+=1
        return patch
#核心思想：用miss来不断更新可以表示的数的范围
#思想就是如果说现在miss的数量很大，多一个nums[i]，只会延长总的范围，并且是连续的
#miss表示的是[1,miss-1]这个处理很巧妙，模仿