class TreeNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class WordDictionary:

    def __init__(self):
        self.root=TreeNode()

    def addWord(self, word: str) -> None:
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TreeNode()
            current=current.children[char]
        current.is_end_of_word=True
    
    def search(self, word: str) -> bool:
        def dfs(node,i):
            if i==len(word):
                return node.is_end_of_word
            char=word[i]
            if char==".":
                for children in node.children.values():
                    if dfs(children,i+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char],i+1)
        return dfs(self.root,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


#关键点是想清楚dfs函数的目的是什么，应该怎么写来实现
#step1: 先想清楚状态，不要想代码 -- 我要解决这个子问题，需要知道哪些会变化的信息
#比如说这道题，处理"."的问题的时候，我需要知道两个: 1.现在在Trie的哪里(方便我继续往下找) 2.现在是word的哪个位置了(方便我往下匹配)
#step2: 想清楚递归出口(base cases)
#比如说这道题，显然base case就是i==len(word)检查到最后一个char的时候
#step3: 想清楚下一步应该怎么走，剩下的交给谁去处理 
#---"处理完当前这一个字符之后，剩下的部分是不是和原问题结构一样，只是规模变小了？"