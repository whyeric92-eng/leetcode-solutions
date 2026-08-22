#解法一
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def f(x):
            res=1
            for i in range(2,x+1):
                res*=i
            return res
        def permutation(lst,k):
            n=len(lst)
            res=[]
            if not lst:
                return []
            if k==0:
                lst.reverse()
                res.extend(lst)
                return res
            if k%(f(n-1))==0:
                m=k//f(n-1)-1
                new_lst=lst[:m]+lst[m+1:]
                res.append(lst[m])
            else:
                m=k//f(n-1)
                new_lst=lst[:m]+lst[m+1:]
                res.append(lst[m])
            return res+permutation(new_lst,k%(f(n-1)))
        lst=[i for i in range(1,n+1)]
        final_lst=permutation(lst,k)
        return "".join(map(str,final_lst))
#这个解法要注意的点太多了，极其容易出错
#1.这个的循环终止条件到底是啥，not lst是，同时k==0也是 2.常规情况的递归，啥时候+1啥时候-1，new_lst到底该怎么定义(自己多举几个例子试一试)
#3.字符串的类型，str与int的转化

#解法二
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def f(x):
            res=1
            for i in range(2,x+1):
                res*=i
            return res
        lst=[str(i) for i in range(1,n+1)]
        res=""
        for i in range(n,0,-1):
            fact=f(i-1)
            index=(k-1)//fact
            res+=lst[index]
            lst.pop(index)
            k%=fact
        return res
#简单明了，用index=(k-1)//fact避免了很多不必要的讨论
#index直接表明就是lst的第几个
#不用recursion一样可以做