# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=head
        pre=ListNode(-1)
        dummy=pre
        pre.next=head
        while cur is not None:
            if cur.val==val:
                pre.next=cur.next
            else:
                pre=pre.next
            cur=cur.next
        return dummy.next
#可以写的更简洁

def removeElements(self, head, val):
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next