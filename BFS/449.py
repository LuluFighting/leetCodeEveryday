# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        ret,myQueue = [],[root]
        lastNode,nextNode = root,root
        while len(myQueue)!=0:
            curNode = myQueue[0]
            myQueue.pop(0)
            ret.append(str(curNode.val))
            ret.append(' ')
            if curNode.left is not None:
                myQueue.append(curNode.left)
                nextNode = curNode.left
            else:
                myQueue.append(TreeNode('#'))
            if curNode.right is not None:
                myQueue.append(curNode.right)
                nextNode = curNode.right
            else:
                myQueue.append(TreeNode('#'))
            if lastNode == curNode:
                if lastNode == nextNode:
                    break
                lastNode = nextNode
        return ''.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        splitData = data.split()
        def deserial(index=0):
            if index>=len(splitData):
                return None
            if splitData[index]=='#':
                return None
            pnew = TreeNode(int(splitData[index]))
            pnew.left = deserial(2*index+1)
            pnew.right = deserial(2*index+2)
            return pnew
        ret = deserial()
        return ret







class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        ret = []
        def postSerialize(root):
            if not root:
                ret.append('# ')
                return
            ret.append(str(root.val)+' ')
            postSerialize(root.left)
            postSerialize(root.right)
        postSerialize(root)
        return ''.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        splitData = data.split()
        def deserial():
            if splitData[0]=='#':
                splitData.pop(0)
                return None
            pnew = TreeNode(int(splitData[0]))
            splitData.pop(0)
            pnew.left = deserial()
            pnew.right = deserial()
            return pnew
        ret = deserial()
        return ret