# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        pre,p1,p2 = None,head,head.next
        while p2 is not None:
            p1.next = p2.next
            p2.next = p1
            if pre is not None:
                pre.next = p2
            else:
                head = p2
            pre = p2
            p1 = p2.next
            if p1 is None:
                break
            p2 = p1.next
        return head
