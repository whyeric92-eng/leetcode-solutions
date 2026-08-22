#解法一
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
#思路简单，直接切片判断即可
#解法二
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
#简单直接，python可以这么写
#解法三：Two pointers
#就是选一个开头，比较haystack和needle