#解法一：O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        left=0
        maxlen=0
        for i,ch in enumerate(s):
            if ch in seen and seen[ch]>=left: #检查是否在窗口里面
                left=seen[ch]+1
            seen[ch] = i  #更新窗口右侧
            maxlen = max(maxlen, i - left + 1)
        return maxlen
#这个解法是最优解
#思想就是***窗口**，i代表窗口的右侧，left代表窗口的左侧

#解法二：O(n2)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        cout=0
        appear=[]
        for i in range(len(s)):
            if  not appear or s[i] not in appear:
                cout+=1
                appear.append(s[i])
            elif s[i] in appear:
                maxlen=max(maxlen,cout)
                m=appear.index(s[i])
                appear=appear[m+1:]
                appear.append(s[i])
                cout=len(appear)
        return max(maxlen,cout)
#思路较为简单，注意的点：1.elif的使用(时刻考虑有没有可能两个if同时成立)，这个的关键是list是可变的
#2.对一个list进行更改的时候，考虑list是mutable的，所以不必再赋值给list