from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        # 不够好 时间复杂度是O(NlogN)
        if len(nums)<1:
            return 0
        gap=0
        for i in range(1,len(nums)):
            cur_gap=nums[i]-nums[i-1]
            if gap<cur_gap:
                gap=cur_gap
        return gap
    
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        n = len(nums)
        min_val, max_val = min(nums), max(nums)
        
        if min_val == max_val:
            return 0
        
        # 桶的宽度（至少为1）
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        #其实是抽屉原理,N个值分布在min和max之间,最大间距一定大于等于平均值
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # 每个桶只存 min 和 max
        buckets = [None] * bucket_count  # None 表示空桶
        
        for num in nums:
            idx = (num - min_val) // bucket_size
            if buckets[idx] is None:
                buckets[idx] = [num, num]  # [bucket_min, bucket_max]
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        # 遍历相邻非空桶，计算最大间距
        # 这个应该是用第二个桶的最小值减去上一个桶的最大值
        max_gap = 0
        prev_max = None
        for bucket in buckets:
            if bucket is None:
                continue
            if prev_max is not None:
                max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]
        
        return max_gap
    #非常巧妙的确保时间复杂度为O(N)