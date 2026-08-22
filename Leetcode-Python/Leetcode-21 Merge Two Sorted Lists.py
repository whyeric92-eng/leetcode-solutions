# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode()
        cur=dummy
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 if list1 else list2
        return dummy.next
#这个解法就是用指针一个一个去放，去存储
#需要注意的点就是：1.dummy就是一个虚拟节点，dummy.next的type才是ListNode
#注意每次比完，list1/list2/cur都需要进到下一位去

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val<list2.val:
            list1.next=self.mergeTwoLists(list1.next,list2)
            return list1
        if list2.val<=list1.val:
            list2.next=self.mergeTwoLists(list1,list2.next)
            return list2
#这个是用recursion的方法来处理的
#list1.next的形式才是ListNode