# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#解法一：用iteration
class Solution(object):
    def reverseList1(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre
#这个方法只用改变cur.next=pre就够了
#对于单向列表，A->B，只要说A.next=B,这条路就相当于通了
#解法二：用Recursion
class Solution(object):
    def reverseList2(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        while not head or not head.next:
            return head
        new_head=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return new_head
#这个方法就是先base case:没有head或者没有head.next，就没啥翻转的了，直接return head
#假设head.next已经reverse好了，返回new_head，就应该处理head的逻辑(注意避免成环)
#最后return的应该是new_head

#这道题A->B->C是改的指向，改为A<-B<-C