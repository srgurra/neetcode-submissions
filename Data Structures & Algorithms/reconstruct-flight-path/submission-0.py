class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for source, destination in tickets:
            heapq.heappush(graph[source], destination)

        itinerary = []

        def dfs(airport: str) -> None:
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)

            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]