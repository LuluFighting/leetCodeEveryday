"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        myQueue = [node]
        hashmap = {}
        clone = Node(node.val,[])
        hashmap[node] =clone
        while len(myQueue)!=0:
            curNode = myQueue[0]
            myQueue.pop(0)
            for neighbor in curNode.neighbors:
                if neighbor not in hashmap.keys():
                    myQueue.append(neighbor)
                    hashmap[neighbor] = Node(neighbor.val,[])
                hashmap[curNode].neighbors.append(hashmap[neighbor])
        return clone
    def cloneGraph(self,node):
        if not node:
            return None
        hashmap = {}
        def dfs(curNode):
            if not curNode:return
            if curNode not in hashmap.keys():
                hashmap[curNode] = Node(curNode.val,[])
            for i in range(len(curNode.neighbors)):
                if not curNode.neighbors[i] in hashmap.keys():
                    dfs(curNode.neighbors[i])
                if not curNode.neighbors[i] in hashmap.keys():
                    clone = Node(curNode.neighbors[i].val,[])
                    hashmap[curNode.neighbors[i]] = clone
                    hashmap[curNode].neighbors.append(clone)
                else:
                    hashmap[curNode].neighbors.append(hashmap[curNode.neighbors[i]])

        dfs(node)
        return hashmap[node]