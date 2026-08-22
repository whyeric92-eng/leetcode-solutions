class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        if len(a)>len(b):
            b="0"*(len(a)-len(b))+b
        if len(a)<len(b):
            a="0"*(len(b)-len(a))+a
        lst_a=list(map(int,a))
        lst_a.reverse()
        lst_b=list(map(int,b))
        lst_b.reverse()
        res=[]
        carry=0
        for i in range(len(lst_a)):
            res.append((lst_a[i])^(lst_b[i])^carry)             
            carry=1 if (lst_a[i]+lst_b[i]+carry)>1 else 0
        if carry==1:
            res.append(1)
        res.reverse()
        return "".join(map(str,res))
#算法部分略微改进：total = lst_a[i] + lst_b[i] + carry
                #res.append(total % 2) 
                #carry = total // 2

class Solution(object):
    def addBinary(self, a, b):
        res = []
        # Simulation: 使用双指针从字符串末尾向前遍历
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        # 只要还有位数没算完，或者还有进位，就继续循环
        while i >= 0 or j >= 0 or carry:
            # String: 如果指针越界就视为0，这样就不需要手动补零了
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            # Math: 当前位的总和
            total = digit_a + digit_b + carry
            
            # Bit Manipulation / Math:
            # total % 2 得到当前位的二进制值 (相当于位运算 total & 1)
            res.append(str(total % 2))
            
            # total // 2 得到新的进位 (相当于位运算 total >> 1)
            carry = total // 2
            
            # 移动指针
            i -= 1
            j -= 1
        
        # String: 最后把结果反转并拼接
        return "".join(res[::-1])
#双指针解法可以避免多次反转和补0操作