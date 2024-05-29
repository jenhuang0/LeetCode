class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj= [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        parent = {}
        queue = deque([0])
        parent[0] = -1

        while queue:
            node = queue.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                if nei in visited:
                    return False
                parent[nei] = node
                visited.add(nei)
                queue.append(nei)
        return len(visited) == n 
