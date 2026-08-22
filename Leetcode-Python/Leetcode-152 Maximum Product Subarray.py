from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        # res 记录全局见过的最大乘积，先初始化为第一个数
        res = nums[0]
        
        # cur_max 和 cur_min 分别记录【以当前数字结尾】的连续子数组的最大和最小乘积
        cur_max = nums[0]
        cur_min = nums[0]
        
        # 从第二个数字开始，只用单层循环，只遍历一遍数组 -> O(n)
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 【核心逻辑】如果当前数字是负数，乘以它会让“最大变最小”，“最小变最大”
            # 所以在乘之前，先把它们两者的值交换过来
            if num < 0:
                cur_max, cur_min = cur_min, cur_max
            
            # 状态转移：当前位置的最大/最小值，要在“自己独立开组”和“乘上前面的成果”中选一个
            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            
            # 每走一步，都用当前算出的 cur_max 去挑战并更新全局最大值 res
            res = max(res, cur_max)
            
        return res
#这个O(1)空间的最优解，本质上就是最纯正的动态规划

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        n = len(nums)
        
        # 定义两个长度为 n 的一维 DP 数组 -> 空间复杂度 O(n)
        # dp_max[i] 表示以 nums[i] 结尾的连续子数组的最大乘积
        # dp_min[i] 表示以 nums[i] 结尾的连续子数组的最小乘积
        dp_max = [0] * n
        dp_min = [0] * n
        
        # 初始状态：第一个数字结尾的子数组，最大最小值都是它自己
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        
        # 全局最大值，先初始化为第一个数
        res = nums[0]
        
        # 单层循环从 1 走到 n-1 -> 时间复杂度 O(n)
        for i in range(1, n):
            num = nums[i]
            
            # 状态转移方程：
            # 这一位的最大值，来自以下三种情况的最大者：
            # 1. 只有自己本身 (num)
            # 2. 前一个位置的最大值乘上自己 (dp_max[i-1] * num)
            # 3. 前一个位置的最小值乘上自己（负负得正） (dp_min[i-1] * num)
            dp_max[i] = max(num, dp_max[i-1] * num, dp_min[i-1] * num)
            dp_min[i] = min(num, dp_max[i-1] * num, dp_min[i-1] * num)
            
            # 用当前位置的 dp_max[i] 去更新全局最大值
            res = max(res, dp_max[i])
            
        return res