class TrieNode:
    def __init__(self, char):
        self.char=char
        self.is_end_of_word=False
        self.next=None
        self.child=None

class Trie:

    def __init__(self):
        self.root=TrieNode("")

    def find_child(self,node,char):
        current=node.child
        while current:
            if current.char==char:
                return current
            current=current.next
        return None
    
    def add_child(self,node,char):
        new_node=TrieNode(char)
        new_node.next=node.child
        node.child=new_node
        return new_node

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            child=self.find_child(node,char)
            if not child:
                child=self.add_child(node,char)
            node=child
        node.is_end_of_word=True

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            child=self.find_child(node,char)
            if not child:
                return False
            node=child
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            child=self.find_child(node,char)
            if not child:
                return False
            node=child
        return True
#这个写法非常与用hash_table相比非常节约空间，是第一次学的时候学校讲的办法，值得复习

class TrieNode:
    def __init__(self):
        # 使用字典存储子节点：key 是字符，value 是对应的 TrieNode
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 如果字符不在当前节点的子节点中，则创建一个新节点
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
#这个写法是用hash_table来储存children的，时间复杂度较好，但是空间复杂度会比较大

#核心判断思路是一样的，for char in word, 判断char在不在node的children里面，在的话就移到children node, 不在的话就添加