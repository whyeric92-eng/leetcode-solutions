# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        right,left=head,prev
        while right and left:
            if right.val!=left.val:
                return False
            right=right.next
            left=left.next
        return True
#核心思路，找到中间位置的node，右边翻转，然后逐一比较右边和左边
#如何找中间位置，slow和fast两个指针，slow就是中间位置(fast或者fast.next是None)