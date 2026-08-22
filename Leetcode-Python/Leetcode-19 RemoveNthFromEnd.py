# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        post=head
        dummy=head
        pre=head
        while (n>=1) and pre:
            pre=dummy.next
            dummy=dummy.next
            n-=1
        if not pre:
            head=head.next
            return head
        while (pre.next):
            pre=pre.next
            post=post.next
        post.next=post.next.next
        return head
# 2 pointers 妙用