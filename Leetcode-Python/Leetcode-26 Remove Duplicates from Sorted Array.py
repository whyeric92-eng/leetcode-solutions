#解法一
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        appear=[]
        i=0
        while i<=len(nums)-1:
            if appear and nums[i] in appear:
                nums.remove(nums[i])
            else:
                appear.append(nums[i])
                i+=1
        return len(nums)
#缺点：时间复杂度太高，O(N2)
#巧妙之处：remove的时候不进行i+=1

#解法二
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        slow=0
        for fast in range(1,len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1
#优点：时间复杂度低，运用双指针，不断比较，多多学习