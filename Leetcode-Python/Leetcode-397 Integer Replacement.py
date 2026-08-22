class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=0
        while n!=1:
            if n==3:
                step+=2
                return step
            elif n%2==0:
                n/=2
                step+=1
            elif n%2==1:
                if n%4==3:
                    n+=1
                    step+=1
                else:
                    n-=1
                    step+=1
        return step
#就是简单的数学思想，需要注意的就是n=3时，这个情况是特例，3-2-1这样子会快一步(单独拎出来说即可)