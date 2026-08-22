class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashtable={}
        seen=set()
        for i in range(len(s)):
            if s[i] in hashtable and hashtable[s[i]]!=t[i]:
                return False
            elif s[i] not in hashtable:
                if t[i] in seen:
                    return False
                #注意两个方向都要确保唯一性
                hashtable[s[i]]=t[i]
                seen.add(t[i])
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        seen = set()
        for cs, ct in zip(s, t):
        #用zip 不用手动维护index 
            if cs in mapping:
                if mapping[cs] != ct:
                    return False
            else:
                if ct in seen:
                    return False
                mapping[cs] = ct
                seen.add(ct)
        return True