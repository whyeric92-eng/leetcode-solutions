class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)
        count=0
        temp=None
        res=[]
        for num in nums:
            if temp!=num:
                res.append(num)
                count=1
                temp=num
            else:
                if count<2:
                    res.append(num)
                    count+=1
                else:
                    count+=1
        nums[:]=res
        return len(res)
#可以AC，但是问题是无法做到in place修改，额外的space不是O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # i 是慢指针，表示下一个待写入的位置
        # 前两个元素（index 0 和 1）无论如何都可以保留
        i = 2 
        
        # 从第三个元素开始遍历（快指针）
        for j in range(2, len(nums)):
            # 关键逻辑：如果当前数字 nums[j] 与我们要写入位置的前两格数字不同
            # 说明 nums[j] 还没出现超过两次（因为数组是有序的）
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        
        return i
#这个方法好高级，慢慢学习