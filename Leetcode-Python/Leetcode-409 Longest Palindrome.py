class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        res=0
        odd=True
        for char in hashmap:
            if hashmap[char]%2==0:
                res+=hashmap[char]
            elif odd and hashmap[char]%2==1:
                res+=hashmap[char]
                odd=False
            else:
                res+=hashmap[char]-1
        return res
#用hashmap记录出现频率即可