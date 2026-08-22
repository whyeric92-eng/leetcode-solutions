class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        res=0
        nums=[]
        oper=[]
        def compute(num1,num2,token):
            if token=="+":
                return num1+num2
            elif token=="*":
                return num1*num2
            elif token=="/":
                return int(float(num2)/num1)
            #这个写法是强制往0靠拢，-1//2=-1, int(-1/2)=0
            elif token=="-":
                return num2-num1
        for token in tokens:
            if token not in ["+","-","*","/"]:
            #别用.isdigit() -- 无法识别负数
                nums.append(int(token))
            else:
                num1=nums.pop()
                num2=nums.pop()
                nums.append(compute(num1,num2,token))
        return nums[0]