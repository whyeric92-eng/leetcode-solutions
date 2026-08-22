class Solution:
    def isHappy(self, n: int) -> bool:
        hashtable={}
        def subHappy(n,hashtable):
            temp=0
            for num in str(n):
                temp+=int(num)**2
            if temp==1:
                return True
            else:
                if temp not in hashtable:
                    hashtable[temp]=1
                    if subHappy(temp,hashtable):
                        return True
                    else:
                        return False
                else:
                    return False
        return subHappy(n,hashtable)
#思路正确 有点臃肿

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        # 只要 n 不为 1 且没进入循环，就一直计算
        while n != 1 and n not in seen:
            seen.add(n)
            # 计算各位平方和
            n = sum(int(digit) ** 2 for digit in str(n))
            
        return n == 1
#别嵌套函数 直接while即可

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            return sum(int(digit) ** 2 for digit in str(number))
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
#把空间复杂度降到O(1)  经典判断是否成环的方法