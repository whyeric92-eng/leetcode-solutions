# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (not head) or (not head.next):
            return head
        new_head=self.swapPairs(head.next.next)
        temp=head.next
        head.next.next=head
        head.next=new_head
        return temp