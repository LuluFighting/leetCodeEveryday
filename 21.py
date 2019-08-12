# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        p1,p2=l1,l2
        phead,pcur = None,None
        while p1 and p2:
            if p1.val <= p2.val:
                if not pcur:
                    phead,pcur = p1,p1
                else:
                    pcur.next = p1
                    pcur = p1
                p1 = p1.next
            else:
                if not pcur:
                    phead,pcur = p2,p2
                else:
                    pcur.next = p2
                    pcur = p2
                p2 = p2.next
        while p1:
            pcur.next = p1
            pcur = p1
            p1 = p1.next
        while p2:
            pcur.next = p2
            pcur = p2
            p2 = p2.next
        return phead
