class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for prerec in prerequisites:
            adj[prerec[1]].append(prerec[0])
            indegree[prerec[0]] += 1
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = []
        
        while queue:
            node = queue.pop(0)
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return res if len(res)==numCourses else []
