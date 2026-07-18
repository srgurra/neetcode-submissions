class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()
        components = 0

        def dfs(node: int) -> None:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)

        return components