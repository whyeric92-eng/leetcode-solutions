class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_num={}
        for num in nums:
            if new_num and num in new_num:
                return True
            else:
                new_num[num]=1
        return False
#注意判读存不存在用hash table即可