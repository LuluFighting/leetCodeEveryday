class Solution:
    def findOrder(self, numCourses: int, prerequisites) :
        if not prerequisites or numCourses==0:
            return [i for i in range(numCourses)]
        visited = [ 0 for j in range(numCourses)]
        adj = [set() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            for j in range(1,len(prerequisite)):
                adj[prerequisite[0]].add(prerequisite[j])
        def dfs(curindex):  #有环返回True
            if visited[curindex]==-1:
                return False
            if visited[curindex]==1:
                return True
            visited[curindex]=1
            adjacentList = adj[curindex]
            for adjacentNode in adjacentList:
                if dfs(adjacentNode)==True:
                    return True
            path.append(curindex)
            visited[curindex] = -1
            return False
        path = []
        for i in range(numCourses):
            if dfs(i)== True:
                return []
        return path

obj = Solution()
print(obj.findOrder(2,[[0,1]]))