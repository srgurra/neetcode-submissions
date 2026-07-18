class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for next_course in graph[current]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        if len(order) == numCourses:
            return order

        return []