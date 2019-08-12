class Node:
    def __init__(self,val,step):
        self.step = step
        self.val = val
class Solution:
    def chooseClass(self,n):  #完成n个学分，返回最少的选课次数
        myQueue= []
        classes = (1,2,4)
        for val in classes:
            myQueue.append(Node(val,1))
        while True:
            curNode = myQueue[0]
            myQueue.pop(0)
            if curNode.val == n:
                return curNode.step
            for val in classes:
                myQueue.append(Node(curNode.val+val,curNode.step+1))


