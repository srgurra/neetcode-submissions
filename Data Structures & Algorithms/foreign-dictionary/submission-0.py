class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}

        for word in words:
            for char in word:
                indegree[char] = 0

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return ""

            for char1, char2 in zip(first, second):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        indegree[char2] += 1
                    break

        queue = deque(
            char for char in indegree
            if indegree[char] == 0
        )

        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) != len(indegree):
            return ""

        return "".join(order)