class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=0
        for num in nums:
            temp^=num
        res_bit=0
        for i in range(32):
            if temp&(1<<i)!=0:
                res_bit=i
                break
        gp1=[]
        gp2=[]
        for num in nums:
            if num&(1<<res_bit)!=0:
                gp1.append(num)
            else:
                gp2.append(num)
        res1=0
        for num in gp1:
            res1^=num
        res2=0
        for num in gp2:
            res2^=num
        return [res1,res2]
#这道题的思路就是把nums分成2部分，分类的依据是两个single number某一位不一样
#然后就可以确保2个single number在不同的部分里面，再用XOR运算就可以获得答案
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Step 1: 算出所有数字的异或和。最后结果 temp = x ^ y
        temp = 0
        for num in nums:
            temp ^= num
        
        # Step 2: 提取 temp 最右侧的 1 (x 和 y 在这一位上必定是一个是 1，一个是 0)
        diff_bit = temp & (-temp)
        
        # Step 3: 根据 diff_bit 将数字分流，并直接在流中做异或
        res1 = 0
        res2 = 0
        for num in nums:
            if (num & diff_bit) != 0:
                res1 ^= num  # 第一组的异或和
            else:
                res2 ^= num  # 第二组的异或和
                
        return [res1, res2]