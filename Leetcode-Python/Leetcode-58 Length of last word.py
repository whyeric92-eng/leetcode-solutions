class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
#s.split()这样子就是以空格为间隔，不管几个空格
#s.strip()就是切掉前后的空白字符