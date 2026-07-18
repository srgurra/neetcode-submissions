class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(node: int) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1: int, node2: int) -> bool:
            root1 = find(node1)
            root2 = find(node2)

            if root1 == root2:
                return False

            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root1] += 1

            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]

        return []