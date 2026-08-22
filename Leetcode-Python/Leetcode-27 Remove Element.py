class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
        return slow 
#标准的slow，fast双指针原地修改
#注意最后返回slow即可，因为slow+1已在if中