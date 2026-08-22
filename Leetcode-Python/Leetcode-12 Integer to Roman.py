class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res=""
        i=0
        dic={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        while num>0:
            if num%10!=4 and num%10!=9:
                res=(num%10)*dic[10**i]+res if num%10<5 else dic[5*10**i]+(num%10-5)*dic[10**i]+res
            elif num%10==4:
                res=dic[10**i]+dic[5*10**i]+res
            else:
                res=dic[10**i]+dic[10*10**i]+res
            num/=10
            i+=1
        return res
#简单描述即可，注意一些细节：1.正着添加还是逆着添加 2.啥时候添加条件不同