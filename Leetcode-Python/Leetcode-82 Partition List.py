# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummy1=ListNode(0)
        pre1=dummy1
        dummy2=ListNode(0)
        pre2=dummy2
        while head:
            if head.val<x:
                pre1.next=ListNode(head.val)
                pre1=pre1.next
                head=head.next
            else:
                pre2.next=ListNode(head.val)
                pre2=pre2.next
                head=head.next
        pre1.next=dummy2.next
        return dummy1.next
class Solution(object):
    def partition(self, head, x):
        # 创建两个虚拟头节点，用于连接原节点
        less_head = ListNode(0)
        greater_head = ListNode(0)
        
        # 用于遍历和构建的指针
        less = less_head
        greater = greater_head
        
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr  # 直接指向原节点
                less = less.next
            else:
                greater.next = curr  # 直接指向原节点
                greater = greater.next
            curr = curr.next
        
        # 关键一步：断开大于等于链表的最后一个节点，防止形成环
        greater.next = None
        
        # 连接两个链表
        less.next = greater_head.next
        
        return less_head.next