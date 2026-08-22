class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=""
        while columnNumber!=0:
            temp_num=columnNumber%26
            if temp_num==0:
                temp_char="Z"
                res=temp_char+res
                columnNumber=columnNumber//26-1
            else:
                temp_char=chr((temp_num-1)%26+65)
                res=temp_char+res
                columnNumber//=26
        return res
#这个看似是简单的10进制与26进制的互相转换，但真正的难点在于这个没有0，每一位是1-26
#所以解决办法其实就是单独处理26的情况