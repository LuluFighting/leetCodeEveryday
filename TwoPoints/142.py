class ListNode:
    def __init__(self,val):
        self.next = None
        self.val = val
class Solution(object):
    def judgeCycle(self,head):
        p1,p2 = head,head
        while p2 is not None and p2.next is not None:
            p2 = p2.next.next
            p1 = p1.next
            if p1==p2:
                return True,p1
        return False,None
    def findEntrance(self,pos,head):
        p1,p2,ret = head,pos,0
        while p1!=p2:
            p1 = p1.next
            p2 = p2.next
            ret+=1
        return ret
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        judgeAns,pos = self.judgeCycle(head)
        if judgeAns == False:
            return -1
        return self.findEntrance(pos,head)

l1 = ListNode(3)
l1.next = ListNode(2)
l1.next.next = ListNode(0)
l1.next.next.next = ListNode(-4)
l1.next.next.next.next = l1.next

obj = Solution()
print(obj.detectCycle(l1))