#解法
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        Hash={}
        for char in strs:
            key="".join(sorted(char))
            if key not in Hash:
                Hash[key]=[char]
            else:
                Hash[key].append(char)
        return Hash.values()
#这道题思路不算太难，就是用一个Hash Table来存储key
#这道题需要注意很多细节用法，sorted(char)这个是针对字符串的，它会把字符串变成list，所以还需要join
#Hash.values()这个会返回list的形式了，所以无需过多操作