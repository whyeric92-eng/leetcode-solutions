# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        dummy = ListNode(-1)
        cur = dummy
        h = []
        for i, node in enumerate(lists):      
            if node:                         
                heapq.heappush(h, (node.val, i, node))
        #这个地方的小细节，就是ListNode没法被直接比较，然后只加一个node.val的话无法避免两个val相同的情况，加上index来避免出现无法比较的情况
        while h:
            val, i, node = heapq.heappop(h)
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next