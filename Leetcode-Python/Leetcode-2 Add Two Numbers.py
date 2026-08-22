# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        current=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0

            total=val1+val2+carry
            carry=total//10
            current.next=ListNode(total%10)
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next
#思路差不多，甚至很多步骤都是相同的
#定义dummy，引入cur，每次操作后cur/l1/l2到下一位
#这道题关键是引入进位(carry)