class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        word=""
        for letter in s:
            if letter!=" ":
                word=word+letter
            elif word:
                stack.append(word)
                word=""
        if word:
            stack.append(word)
        res=stack[::-1]
        return " ".join(res)

class Solution:

    def reverseWords(self, s: str) -> str:
        # s.split() 自动按空格切分并过滤多余空格
        # [::-1] 翻转列表
        # " ".join() 拼接
        return " ".join(s.split()[::-1])