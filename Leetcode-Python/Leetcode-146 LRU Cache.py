class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
#这个Node的定义也值得思考，首先是hashtable(key+value)，然后是doubly linked list(prev+next)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache={}
        self.capacity=capacity
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
#要求O(1)时间复杂度，所以得同时用hashtable和linked list来存储

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_head(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node=self.cache[key]
            self.remove(node)
            self.add_head(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            old_node=self.cache[key]
            self.remove(old_node)
        #可以不重复创建节点，考虑直接修改node的value
        elif len(self.cache)>=self.capacity:
            del self.cache[self.tail.prev.key]
            self.remove(self.tail.prev)
        new_node=ListNode(key,value)
        self.cache[key]=new_node
        self.add_head(new_node)
        return
    
#易错点是每次添加和删除都要在linked list和hashtable里面都要处理

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)