from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA=headA
        pointerB=headB
        hashtable={}
        while pointerA or pointerB:
            if pointerA and pointerA in hashtable:
                return pointerA
            elif pointerA:
                hashtable[pointerA]=1
            if pointerB and pointerB in hashtable:
                return pointerB
            elif pointerB:
                hashtable[pointerB]=1
            pointerA=pointerA.next if pointerA else pointerA
            pointerB=pointerB.next if pointerB else pointerB
        return None
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
#你走过我走过的路，我们终将相遇