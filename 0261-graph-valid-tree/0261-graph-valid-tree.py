class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj= [[] for i in range(n)]

        for v, u in edges:
            adj[v].append(u)
            adj[u].append(v)

        
        visited = set()
        parent = {}
        q=deque([0])
        parent[0] = -1

        while q:
            node = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                if nei in visited:
                    return False
                q.append(nei)
                parent[nei] = node

        return len(visited) == n