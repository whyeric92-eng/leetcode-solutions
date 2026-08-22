"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        head1=head
        hashtable={}
        while head1:
            hashtable[head1]=Node(head1.val)
            head1=head1.next
        head2=head
        while head2:
            if head2.next:
                hashtable[head2].next=hashtable[head2.next]
            else:
                hashtable[head2.next]=None
            head2=head2.next
        head3=head
        while head3:
            if head3.random:
                hashtable[head3].random=hashtable[head3.random]
            else:
                hashtable[head3.random]=None
            head3=head3.next
        return hashtable[head]
    
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        hashtable = {}
        
        # 第一遍：创建所有节点
        curr = head
        while curr:
            hashtable[curr] = Node(curr.val)
            curr = curr.next
            
        # 第二遍：同时连接 next 和 random
        curr = head
        while curr:
            # 使用 .get()，如果键是 None 会自动返回 None，避免了繁琐的 if 判断
            hashtable[curr].next = hashtable.get(curr.next)
            hashtable[curr].random = hashtable.get(curr.random)
            curr = curr.next
            
        return hashtable[head]