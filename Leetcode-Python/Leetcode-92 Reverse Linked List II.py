class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        # 使用 dummy 节点处理 left=1 的特殊情况
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        # 1. 移动 pre 到 left 的前一个位置
        for _ in range(left - 1):
            pre = pre.next
            
        # 2. 开始局部反转
        # cur 是反转区间不变的第一个节点（反转后会变成区间的末尾）
        cur = pre.next 
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        #这个方法很巧妙而且便捷，就是不太容易想
        return dummy.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left==right:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for _ in range(left):
            first_a=pre
            pre=pre.next
        last_a=pre
        cur=pre.next
        for _ in range(right-left):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        first_b=pre
        last_b=cur
        first_a.next=first_b
        last_a.next=last_b
        return dummy.next