class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==1:
            return [0,1]
        res=self.grayCode(n-1)
        new=[num+2**(n-1) for num in res[::-1]]
        res.extend(new)
        return res
#更偏向于数学方法，镜像找规律，其本质是只有一位不同，前半部分和后半部分区别就是最高位(镜像)
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        visited = {0}  # 用集合记录已经用过的数字，查找速度快(O(1))
        
        # 定义回溯函数
        def backtrack():
            # Base Case: 序列长度达到了 2^n，说明找齐了，直接返回 True 停止搜索
            if len(res) == 1 << n:
                return True
            
            current = res[-1]
            
            # 尝试翻转 current 的第 i 位 (i 从 0 到 n-1)
            for i in range(n):
                # 利用异或运算翻转第 i 位：1 << i 构造了一个只有第 i 位是 1，其余是 0 的数
                next_val = current ^ (1 << i)
                
                # 如果这个新数字没被用过
                if next_val not in visited:
                    # 1. 做出选择（加到路径里）
                    visited.add(next_val)
                    res.append(next_val)
                    
                    # 2. 递归进入下一层
                    # 如果后续的路径能成功到达终点，直接一路返回 True 退出
                    if backtrack():
                        return True
                    
                    # 3. 撤销选择（回溯：说明这条路走不通，把刚才加的删掉，尝试下一种翻转）
                    visited.remove(next_val)
                    res.pop()
            
            # 如果 n 个位都试过了都不行，返回 False
            return False
            
        backtrack()
        return res