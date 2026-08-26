from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashtable={}
        res=[]
        for num in nums:
            if num in hashtable:
                hashtable[num]+=1
            else:
                hashtable[num]=1
        bar=len(nums)//3
        for key,value in hashtable.items():
            if value>bar:
                res.append(key)
        return res
#常规思路 利用hashtable存储每个出现的数量

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        bar = len(nums) // 3
        return [num for num, freq in count.items() if freq > bar]
#利用counter简化计数部分

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = None, None
        cnt1, cnt2 = 0, 0
        
        for num in nums:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
            #真正出现次数大于n//3的数字是消耗不完的 
            #假设该数字为x 有count(x)个 完全消耗(else分支)需要3*count(x)这么多个元素 这个已经超过了n (count(x)出现次数大于n//3)
        
        # 验证阶段
        res = []
        for cand in [cand1, cand2]:
            if nums.count(cand) > len(nums) // 3:
                res.append(cand)
        return res
#Boyer-Moore 摩尔投票法 一个数组中出现次数超过n/3的元素最多只有两个 实现额外空间为O(1)