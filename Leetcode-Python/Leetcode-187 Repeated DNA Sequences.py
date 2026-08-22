from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n=len(s)
        set1=set()
        set2=set()
        res=[]
        for i in range(n-9):
            temp=s[i:i+10]
            if temp in set1 and (not set2 or temp not in set2):
                res.append(temp)
                set2.add(temp)
            elif not set1 or temp not in set1:
                set1.add(temp)
        return res

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set() # 不能用{}来初始化
        res = set() # 使用 set 存储结果，自动处理重复添加问题
        
        for i in range(len(s) - 9):
            temp = s[i : i + 10]
            if temp in seen:
                res.add(temp) # 如果已经在 seen 中，说明重复，加入结果集
            else:
                seen.add(temp) # 否则标记为已见过
                
        return list(res)
#in会自动处理空set的情况