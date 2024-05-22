class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses # edge of each node
        adj = [[]for i in range(numCourses)] #each node's pre

        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
            indegree[pre[0]] += 1 #edge going to that node
        queue = []
        #search for the node that doesnt have any edge going into 
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            node = queue.pop(0)
            visited += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return visited == numCourses
