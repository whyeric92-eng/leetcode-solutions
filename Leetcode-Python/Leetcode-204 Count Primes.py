from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        def judge(n):
            if n<4:
                return True
            for i in range(2,int(sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        res=0
        for i in range(2,n):
            if judge(i):
                res+=1
        return res
#这个方法无法AC 时间复杂度太高 为n*sqrt(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # 从 i*i 开始标记，因为更小的倍数已经被更小的质数标记过了
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
#时间复杂度为O(n log log n)
#主要思想就是根据已有的质数 把所在范围内所有的该质数的倍数全部标记了 只用维持一个一维数组即可