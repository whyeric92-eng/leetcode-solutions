# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def insert(head,node):
            prev=head
            cur=head.next
            while cur and cur.val<node.val:
                cur=cur.next
                prev=prev.next
            prev.next=node
            node.next=cur
            return
        new_head=ListNode()
        while head:
            node=ListNode(head.val)
            insert(new_head,node)
            head=head.next
        return new_head.next
#大体上没啥问题，空间复杂度O(N)，还有优化空间(尝试inplace修改)

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # dummy 节点用来辅助头部插入
        dummy = ListNode(0)
        dummy.next = head
        
        # last_sorted: 已排序部分的最后一个节点
        # curr: 当前正在处理、准备插入的节点
        last_sorted = head
        curr = head.next
        
        while curr:
            if last_sorted.val <= curr.val:
                # 情况 1：当前节点本来就比前一个大，直接后移指针，不需要移动节点
                last_sorted = last_sorted.next
            else:
                # 情况 2：当前节点比前一个小，需要从头遍历已排序部分，找到插入位置
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                
                # 将 curr 节点从原位置删掉，并插入到 prev 之后
                last_sorted.next = curr.next  # 断开 curr
                curr.next = prev.next         # curr 指向插入位置的下一个
                prev.next = curr              # prev 指向 curr
                
            # 移动到原链表的下一个待处理节点
            curr = last_sorted.next
            
        return dummy.next
#inplace修改，much better