#解法一：直接翻译，必然TLE
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        def base(n):
            return 2**(n%4) if n%4!=3 else 3
        def convert(nums1):
            n=len(nums1)
            nums2=0
            for i in range(n):
                nums2+=int(nums1[i])*base(n-1-i)
            return nums2%5==0
        n=len(nums)
        res=[]
        for i in range(n):
            res.append(convert("".join(map(str,nums[:i+1]))))
        return res
#解法二
class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        n=len(nums)
        res=[]
        cur=0
        for i in range(n):
            cur=(cur*2+nums[i])%5
            res.append(cur==0)
        return res
#充分运用上次算的cur来降低时间复杂度