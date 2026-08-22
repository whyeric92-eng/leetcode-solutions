# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        res=dummy
        temp=None
        add=True
        if not head or not head.next:
            return head
        while head:
            if temp is None:
                temp=head.val
                head=head.next
            elif head.val==temp:
                head=head.next
                add=False
            elif head.val!=temp:
                if add:
                    res.next=ListNode(temp)
                    res=res.next
                add=True
                temp=head.val
                head=head.next
        if add:
            res.next=ListNode(temp)
        return dummy.next
#自己想的解法，就是遍历，然后在遍历过程中
#缺点就是不是in place修改，有待提高
class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0, head)
        prev = dummy # prev 指向确定要保留的最后一个节点
        
        while head:
            # 如果发现当前节点和下一个节点值相同
            if head.next and head.val == head.next.val:
                # 这一步是核心：跳过所有重复的节点
                while head.next and head.val == head.next.val:
                    head = head.next
                # 跳过所有重复节点后，prev.next 指向重复段之后的节点
                # 注意：此时不移动 prev，因为 head.next 仍可能是下一个重复段的开始
                prev.next = head.next 
            else:
                # 如果没有重复，说明当前 head 是安全的，prev 向前移动
                prev = prev.next
                
            head = head.next
            
        return dummy.next