class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Construct adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()
        queue = deque([0])
        parent = {}
        parent[0] = -1
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in visited:
                    return False
                parent[neighbor] = node
                visited.add(neighbor)
                queue.append(neighbor)
        return True if len(visited) == n else False
 
