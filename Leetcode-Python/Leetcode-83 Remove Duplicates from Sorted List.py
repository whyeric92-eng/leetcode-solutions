# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        if not head:
            return 
        prev=ListNode(head.val)
        dummy.next=prev
        while head:
            while head and prev.val==head.val:
                head=head.next
            if not head:
                return dummy.next
            prev.next=ListNode(head.val)
            prev=prev.next
            head=head.next
        return dummy.next
#空间复杂度依然有待提高，这个每次都要新建ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 1. 处理空链表或只有一个节点的情况
        if not head:
            return head
        
        # 2. 使用指针遍历链表
        curr = head
        while curr and curr.next:
            # 3. 如果当前值等于下一个值，跳过下一个节点
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                # 4. 否则，继续移动指针
                curr = curr.next
                
        return head
#相当于是从一个列表里面删除