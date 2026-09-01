# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node.next
        while cur.next:
            node.val = cur.val
            node = node.next
            cur = cur.next
        node.val = cur.val
        node.next = None

#这道题的难点在于不给head 只给了node
#解决方法就是一个一个把值复制到前一个 最后一个删掉 实现删除node的效果 (要求就是node不可以是最后一个)

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

#很巧妙的一个写法