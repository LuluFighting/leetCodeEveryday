# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length,pcur = 0,head
        while pcur is not None:
            length+=1
            pcur=pcur.next
        k = k%length
        if k==0:
            return head
        p1,p2,count  = head,head,0
        while p2.next is not None:
            p2 = p2.next
            if count>=k:
                p1 = p1.next
            count+=1
        p2.next = head
        head = p1.next
        p1.next =None
        return head