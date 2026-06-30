class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m= len(grid)
        n= len(grid[0])

        queue = deque()
        visited = set()

        fresh =0

        for i in range(m):
            for j in range(n):
                if grid[i][j]== 2:
                    queue.append((i,j))
                elif grid[i][j]== 1:
                    fresh+=1
        ans=-1

        if fresh == 0:
            return 0

        def valid(row, col):
            return 0<=row<m and 0<= col< n and grid[row][col]== 1
        directions= [[0,1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            l= len(queue)
            ans+=1
            for i in range(l):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    if valid(x+dx, y+dy):
                        fresh-=1
                        grid[x+dx][y+dy]=2
                        queue.append((x+dx, y+dy))
        return ans if fresh ==0 else -1