# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        hashtable={}
        cur=head
        i=0
        while cur:
            hashtable[i]=cur
            cur=cur.next
            i+=1
        def reorder(head,init,leng):
            if not head:
                return None
            if not head.next or not head.next.next:
                return head
            lastNode=hashtable[init+leng-1]
            seclast=hashtable[init+leng-2]
            seclast.next=None
            #关键的一部，要把这个连接断开
            temp=head.next
            head.next=lastNode
            lastNode.next=reorder(temp,init+1,leng-2)
            return head
        return reorder(head,0,i)
#这个算法的思路相对简单，就是用一个hashtable来存储所有Node，然后每次Recursion时带两个参数，init和leng

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        while fast.next and fast.next.next:
    #巧妙的终止条件判断
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
#快慢指针，分成2个部分
        def reverse(head):
            if not head:
                return None
            if not head.next:
                return head
            new_head=reverse(head.next)
            head.next.next=head
            head.next=None
            return new_head
        second_start=reverse(second_half)
#反转第二部分
        cur=head
        while second_start and cur:
            temp1=cur.next
            cur.next=second_start
            temp2=second_start.next
            second_start.next=temp1
            cur=temp1
            second_start=temp2
        return head
#拼接两个部分