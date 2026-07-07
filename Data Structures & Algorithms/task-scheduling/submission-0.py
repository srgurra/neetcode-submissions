class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)

        time = 0
        cooldown = deque()  # (available_time, remaining_count)

        while heap or cooldown:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)  # execute one task

                if cnt != 0:
                    cooldown.append((time + n, cnt))

            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(heap, cnt)

        return time