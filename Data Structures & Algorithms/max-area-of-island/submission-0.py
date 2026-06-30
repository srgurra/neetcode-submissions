class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n= len(grid[0])

        def valid(row, col):
            return 0<= row<m and 0<= col< n and grid[row][col]==1 and (row, col) not in visited
        def dfs(row, col):
            if not valid(row, col):
                return 0

            curr=1
            visited.add((row, col))
            for dx, dy in directions:
                curr_row, curr_col= row+dx, col+dy
                curr+=dfs(curr_row, curr_col)
            return curr

                

        directions = [[0,1], [0, -1], [1,0], [-1, 0]]
        ans=0
        for i in range(m):
            for j in range(n):
                ans= max(ans, dfs(i, j))
        return ans
                



        