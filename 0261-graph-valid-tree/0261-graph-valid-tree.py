class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]

        for a, v in edges:
            adj[a].append(v)
            adj[v].append(a)

        visited = set()
        parent = {}
        q = deque([0])
        parent[0] = -1

        while q:
            node = q.popleft()
            visited.add(node)
            for nei in adj[node]:
                if nei == parent[node]:
                    continue
                if nei in visited:
                    return False
                parent[nei] = node
                q.append(nei)
                visited.add(nei)
        print(visited)
        print(n)
        return len(visited) == n