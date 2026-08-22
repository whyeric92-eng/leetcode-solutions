class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        n1=len(num1)
        n2=len(num2)
        num=[0]*(n1+n2)
        for i in range(n1-1,-1,-1):
            for j in range(n2-1,-1,-1):
                p=int(num1[i])*int(num2[j])
                num[i+j+1]+=p%10
                if num[i+j+1]>=10:
                    num[i+j]+=num[i+j+1]//10
                    num[i+j+1]%=10
                num[i+j]+=p//10
                if num[i+j]>=10:
                    num[i+j-1]+=num[i+j]//10
                    num[i+j]%=10
        for i in range(n1+n2):
            if num[i]!=0:
                start=i
                break
        return "".join(map(str,num[start:]))
#大体思路是模拟竖式乘法，用长度为len(num1)+len(num2)的list来储存
#有些细节有点多余，可以改善
class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1, n2 = len(num1), len(num2)
        res = [0] * (n1 + n2)
        
        # 预先将字符转为数字，避免循环内重复调用
        d1 = [ord(c) - ord('0') for c in num1]
        d2 = [ord(c) - ord('0') for c in num2]

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                mul = d1[i] * d2[j]
                # p1 是十位（进位），p2 是个位
                p1, p2 = i + j, i + j + 1
                
                # 叠加到当前位
                _sum = mul + res[p2]
                res[p2] = _sum % 10
                res[p1] += _sum // 10  # 进位直接累加到前一位

        # 找到第一个非零数字的索引
        idx = 0
        while idx < len(res) and res[idx] == 0:
            idx += 1
            
        return "".join(map(str, res[idx:]))