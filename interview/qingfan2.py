class Solution:
    def canFinish(self, numCourses: int, prerequisites) :
        if not prerequisites or numCourses==0:
            return True
        visited = [ 0 for j in range(numCourses)]
        hashmap = {}
        for i in range(len(prerequisites)):  #用hashmap来表示邻接表
            if prerequisites[i][0] not in hashmap.keys():
                hashmap[prerequisites[i][0]] = set()
            for j in range(1,len(prerequisites[i])):
                hashmap[prerequisites[i][0]].add(prerequisites[i][j])
        def dfs(curindex):  #有环返回True
            if visited[curindex]==-1:
                return False
            if visited[curindex]==1:
                return True
            if visited[curindex]==0:
                visited[curindex]=1
            if not curindex in hashmap.keys():
                visited[curindex]=-1
                return False
            adjacentList = hashmap[curindex]
            for adjacentNode in adjacentList:
                if dfs(adjacentNode)==True:
                    return True
            visited[curindex] = -1
            return False

        for i in range(numCourses):
            if dfs(i)== True:
                return False
        return True

obj = Solution()
print(obj.canFinish(2,[[1,0]]))