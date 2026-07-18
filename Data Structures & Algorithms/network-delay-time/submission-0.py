class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for source, target, time in times:
            graph[source].append((time, target))

        min_heap = [(0, k)]
        shortest_time = {}

        while min_heap:
            current_time, node = heapq.heappop(min_heap)

            if node in shortest_time:
                continue

            shortest_time[node] = current_time

            for travel_time, neighbor in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(
                        min_heap,
                        (current_time + travel_time, neighbor)
                    )

        if len(shortest_time) != n:
            return -1

        return max(shortest_time.values())