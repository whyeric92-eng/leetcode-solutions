from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable={}
        for num in nums:
            if num in hashtable:
                hashtable[num]+=1
            else:
                hashtable[num]=1
        for key,value in hashtable.items():
            if value>(len(nums)//2):
                return key
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # 当血量归零时，更换当前数字为新的擂主候选人
            if count == 0:
                candidate = num
            
            # 阵营相同加血，不同扣血
            count += (1 if num == candidate else -1)
            
        return candidate
#把空间复杂度变为O(1)
#乍一看感觉有点奇怪 但是--"因为多数元素的数量比其他所有人加起来还要多，所以它一定能活到最后"