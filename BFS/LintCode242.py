
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if root is None:
            return []
        myQueue = [root]
        lastNode,nextNode = root,root
        ret,tail,index = [],[],0
        while len(myQueue)!=0:
            curNode = myQueue[0]
            myQueue.pop(0)
            listNode = ListNode(curNode.val)
            if len(ret)< index+1:
                ret.append(listNode)
                tail.append(listNode)
            else:
                tail[index].next = listNode
                tail[index] = tail[index].next
            if curNode.left is not None:
                myQueue.append(curNode.left)
                nextNode = curNode.left
            if curNode.right is not None:
                myQueue.append(curNode.right)
                nextNode = curNode.right
            if curNode == lastNode:
                lastNode = nextNode
                index+=1
        return ret