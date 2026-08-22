class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def select(num,n):     #从num中除去n个数
            stack=[]
            for i in range(len(num)):
                while stack and n>0 and num[i]>stack[-1]:
                    stack.pop()
                    n-=1
                stack.append(num[i])
            if n>0:
                stack=stack[:-n]
            return stack
        def merge(stack1,stack2):   #将stack1和stack2 merge到一起
            res=[]
            while stack1 and stack2:
                if stack1[0]>stack2[0]:
                    res.append(stack1[0])
                    stack1.pop(0)
                elif stack1[0]<stack2[0]:
                    res.append(stack2[0])
                    stack2.pop(0)
                else:
                    str1="".join(map(str,stack1))
                    str2="".join(map(str,stack2))
                    if str1*10>str2*10:
                        res.append(stack1[0])
                        stack1.pop(0)
                    else:
                        res.append(stack2[0])
                        stack2.pop(0)
            if stack1:
                res+=stack1
            else:
                res+=stack2
            return res
        hashmap={}
        maxkey=0
        for i in range(max(0,k-len(nums2)),min(k,len(nums1))+1):
            stack1=select(nums1,len(nums1)-i)
            stack2=select(nums2,len(nums2)-k+i)
            res=merge(stack1,stack2)
            hashmap[int("".join(map(str,res)))]=res
            maxkey=max(int("".join(map(str,res))),maxkey)
        return hashmap[maxkey]
#这个算法虽然逻辑是对的，也可以跑的通，但是还是有很多改进地方
#1.merge：stack1[0]=stack2[0]处理不够简洁 2.hashmap真的有必要吗
#这道题其实就是缝合怪，先用greedy+stack选，再merge，最后比较输出

#改进地方-merge板块
def merge(stack1,stack2):
    res=[]
    while stack1 or stack2:
        better=stack1 if stack1>stack2 else stack2
        res.append(better.pop(0))
    return res
#其实和上面的逻辑是一样的，都是比较-append-删除，这个逻辑会简单许多

#改进地方-hashmap不必使用
k=1 #仅为例子
stack1=[0] #仅为例子
stack2=[0] #仅为例子
max_res=[0]*k #循环外
candidate=merge(stack1,stack2)
max_res = max(max_res, candidate)

#[]列表可以直接参与大小比较-字典序（Lexicographical Order）
#规则：1.逐位比较，一旦分出高下立即停止 2.如果当前位相同，比较下一位 3.如果比到一方没数据了，长的那个大