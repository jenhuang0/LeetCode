class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Construct adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        queue = deque([0])
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
        
        # Check if all nodes are visited
        return len(visited) == n and len(edges) == n - 1

