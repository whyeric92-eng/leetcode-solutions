# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def rotateonce(head):
            dummy=head
            pre=head
            if not pre:
                return head
            if not pre.next:
                return head
            cur=pre.next
            while cur.next:
                pre=cur
                cur=cur.next
            num=cur.val
            pre.next=None
            new_node=ListNode(num)
            new_node.next=dummy
            return new_node
        def length(head):
            if not head:
                return 0
            count=1
            while head.next:
                count+=1
                head=head.next
            return count
        res=head
        length=length(head)
        if length==0:
            return head
        k1=k%length
        while (k1>=1):
            res=rotateonce(res)
            k1-=1
        return res
#这个方法中规中矩，不算最优解，但是逻辑简单，且运用%length去减小时间复杂度
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # 1. 计算长度并找到旧尾部
        old_tail = head
        length = 1
        while old_tail.next:
            old_tail = old_tail.next
            length += 1
        
        # 2. 闭合成环
        old_tail.next = head
        
        # 3. 找到新的尾部：距离头节点第 (length - k % length - 1) 个节点
        k = k % length
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # 4. 断开环，确定新头部
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head