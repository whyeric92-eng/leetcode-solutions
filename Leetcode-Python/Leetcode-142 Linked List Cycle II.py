# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre=head
        cur=head.next
        hashtable={}
        while cur:
            if cur in hashtable:
                return cur
            hashtable[pre]=1
            pre=pre.next
            cur=cur.next
        return None

class Solution(object):
    def detectCycle(self, head):
        visited = set() # 使用集合代替字典
        cur = head
        
        while cur:
            if cur in visited:
                return cur
            visited.add(cur)
            cur = cur.next
            
        return None
#用hashtable可以一个指针就搞定

class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        
        # 第一步：判断是否有环
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
                
        # 如果没有环，直接返回 None
        if not has_cycle:
            return None
            
        # 第二步：寻找环的入口
        # 让一个指针回到起点，另一个指针留在相遇点，两者同速前进
        #此时两个的差距一定是整数倍的环的长度(数学推导)
        curr = head
        while curr != slow:
            curr = curr.next
            slow = slow.next
            
        return curr