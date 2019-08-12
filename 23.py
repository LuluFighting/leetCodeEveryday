# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self,p1, p2):
        if not p1 and not p2:
            return None
        elif not p1:
            return p2
        elif not p2:
            return p1
        phead, pcur = None, None
        while p1 and p2:
            if p1.val < p2.val:
                if not pcur:
                    phead, pcur = p1, p1
                else:
                    pcur.next = p1
                pcur = p1
                p1 = p1.next
            else:
                if not pcur:
                    phead, pcur = p2, p2
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
    def mergeK(self,lists):
        if len(lists)==1:
            return lists[0]
        i,j=0,len(lists)-1
        result = []
        while i<=j:
            if i==j:
                result.append(lists[i])
                break
            result.append(self.mergeTwoLists(lists[i],lists[j]))
            i+=1
            j-=1
        return self.mergeK(result)
    def mergeKLists(self, lists) -> ListNode:
        if not lists:
            return None
        if len(lists)==1:
            return lists[0]
        phead = self.mergeK(lists)
        return phead
p1 = ListNode(1)
p1.next = ListNode(2)
p1.next.next = ListNode(3)
p2 = ListNode(4)
p2.next = ListNode(5)
p2.next.next = ListNode(6)
p2.next.next = ListNode(7)
a = [p1,p2]
obj = Solution()
obj.mergeKLists(a)