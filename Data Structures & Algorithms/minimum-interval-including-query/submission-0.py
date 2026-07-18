class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(
            (query, index)
            for index, query in enumerate(queries)
        )

        result = [-1] * len(queries)
        min_heap = []
        interval_index = 0

        for query, original_index in sorted_queries:

            while (
                interval_index < len(intervals)
                and intervals[interval_index][0] <= query
            ):
                left, right = intervals[interval_index]
                length = right - left + 1

                heapq.heappush(min_heap, (length, right))
                interval_index += 1

            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)

            if min_heap:
                result[original_index] = min_heap[0][0]

        return result