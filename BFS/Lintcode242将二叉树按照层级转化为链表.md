[题目链接](https://www.lintcode.com/problem/convert-binary-tree-to-linked-lists-by-depth/description)
  
  由于leetcode上面很多需要升级会员之类的，之后的代码刷题转移到lintcode上面。
 #### 题目分析
 这道题采用BFS的方法，在每一层将二叉树的结点串联起来即可。同时我们有一个小trick，就是用tail数组保存每一层链表的尾结点，这样就不用每次遍历了，代码如下：
 ```Python
 
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
 ```