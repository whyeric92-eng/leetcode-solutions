class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        hashtable=set(nums)
        for num in hashtable:
#关键点是遍历hashtable而不是nums,因为这样可以很有效地去重
            if (num-1) not in hashtable:
                cur=num
                cur_res=1
                while (cur+1) in hashtable:
                    cur_res+=1
                    cur+=1
                res=max(res,cur_res)
        return res