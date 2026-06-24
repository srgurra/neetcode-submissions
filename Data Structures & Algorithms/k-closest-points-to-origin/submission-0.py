class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for i, point in enumerate(points):
            distance = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(heap, (-distance, i))
            if len(heap)>k:
                heapq.heappop(heap)
        for h in heap:
            ans.append(points[h[1]])
        return ans
