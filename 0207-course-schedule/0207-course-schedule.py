class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # our goal is to find if there's a loop in the graph (topological sort)
        # in order to do that, is we first look for the node that dont have previous edge
        # we can use indegree to track each node's being pointed edge
        indegree = [0] * numCourses  #track the edge of the node is pointed(index = node, val = edge)
        adj = [[] for x in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        queue = []
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