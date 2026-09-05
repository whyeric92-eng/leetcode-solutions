class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
#这个写法简洁 但是时间复杂度并非最优解

#更推荐的写法是用字典/counter 可以实现O(N)