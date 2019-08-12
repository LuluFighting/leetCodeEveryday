# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or head.next is None:
            return None
        pre,p1,p2 = None,head,head
        for i in range(1,n):
            p1=p1.next
        while p1.next is not None:
            p1 = p1.next
            pre = p2
            p2 = p2.next
        if p2 == head:
            head = p2.next
            p2.next=None
        else:
            pre.next = p2.next
        return head
