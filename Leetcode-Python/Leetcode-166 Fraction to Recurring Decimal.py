class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator*denominator==0:
            return "0"
        elif numerator*denominator>0:
            sign=""
        else:
            sign="-"
        integer=abs(numerator)//abs(denominator)
        floatings=[]
        hashtable={}
        fraction=abs(numerator)-integer*abs(denominator)
        if fraction==0:
            return sign+str(integer)
        while fraction>0:
            digit=fraction*10//abs(denominator)
            if fraction in hashtable:
                break
            else:
                hashtable[fraction]=digit
            floatings.append((str(fraction),str(digit)))
            fraction=fraction*10-digit*abs(denominator)
        if fraction==0:
            end="".join([digit[1] for digit in floatings])
            return sign+str(integer)+"."+end
        else:
            idx=floatings.index((str(fraction),str(digit)))
            front=floatings[:idx]
            back=floatings[idx:]
            frontend="".join([digit[1] for digit in front])
            backend="".join([digit[1] for digit in back])
            return sign+str(integer)+"."+frontend+"("+backend+")"
#比较冗长但是思路清晰的方法，就是模拟自己列竖式计算有小数点的情况

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer = numerator // denominator
        remainder = numerator % denominator
        if remainder == 0:
            return sign + str(integer)
        
        result = [sign, str(integer), "."]
        seen = {}  # remainder -> index in digits list
        digits = []
        
        while remainder != 0:
            if remainder in seen:
                idx = seen[remainder]
                digits.insert(idx, "(")
                digits.append(")")
                break
            seen[remainder] = len(digits)
        #这个关键就是存储此时的index 不需要再用一个list来维护
            remainder *= 10
            digits.append(str(remainder // denominator))
            remainder %= denominator
        
        result.append("".join(digits))
        return "".join(result)