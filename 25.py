# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self,p,k):
        pre,last,p1,p2,p3 = None,None,p,p.next,p.next.next
        sum=1
        while p2 is not None:
            p2.next = p1
            pre = p2
            sum+=1
            if sum==2:
                last = p1
            p1 = p2
            p2 = p3
            if p2 is None or sum==k:
                break
            p3 = p3.next
        return pre,last,p3

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        if not head.next or k==1:
            return head
        length,pcur = 0,head
        while pcur is not None:
            length+=1
            pcur = pcur.next
        epoch,sum = 0,1
        last,p1 = None,head
        while p1 is not None:
            if length- epoch*k < k:
                break
            pres1,pres2,pres3 = self.reverse(p1,k)  #对p1做翻转
            if not last:
                head = pres1
            else:
                last.next = pres1
            last = pres2
            epoch+=1
            p1 = pres3
        if last is not None:
            last.next = p1
        return head

p = ListNode(1)
p.next = ListNode(2)
obj = Solution()
obj.reverseKGroup(p,2)

