# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def merge(first,second):
            dummy=ListNode(0)
            cur=dummy
            while first and second:
                if first.val<second.val:
                    cur.next=first
                    first=first.next
                else:
                    cur.next=second
                    second=second.next
                cur=cur.next
            if first:
                cur.next=first
            if second:
                cur.next=second
            return dummy.next

        if not head or not head.next:
            return head
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        second_half=slow.next
        slow.next=None
        first_half=self.sortList(head)
        second_half=self.sortList(second_half)
        return merge(first_half,second_half)
#思路就是普通list的mergesort的写法
#mergesort一直就是分到无可再分(0或者1),然后进行merge(merge是对两个sorted list进行merge)
#这样已经很好，时间复杂度O(nLOGn),空间复杂度O(n)

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # 1. 先统计链表总长度
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        dummy = ListNode(0)
        dummy.next = head
        
        # 2. 从自增步长开始：1 -> 2 -> 4 -> 8 ...
        step = 1
        while step < length:
            prev = dummy      # prev 用来连接合并后的子链表
            curr = dummy.next # curr 用来遍历拆分链表
            
            while curr:
                # 提取第一部分 l1，长度为 step
                l1 = curr
                l2 = self.split(l1, step)    # split 函数会切断并返回 l2 的头
                curr = self.split(l2, step)  # 再切断，并返回剩下未处理的链表头
                
                # 合并 l1 和 l2，并接在 prev 后面
                prev.next = self.merge(l1, l2)
                
                # 把 prev 移动到当前合并完的这段链表的末尾
                while prev.next:
                    prev = prev.next
                    
            step *= 2 # 步长翻倍
            
        return dummy.next

    # 辅助函数 1：切断链表。从 head 开始数 n 个节点，断开，并返回后半部分的头
    def split(self, head, n):
        while n > 1 and head:
            head = head.next
            n -= 1
        if not head:
            return None
        next_part = head.next
        head.next = None # 断开连接！
        return next_part

    # 辅助函数 2：经典的合并两个有序链表（不占额外空间）
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next