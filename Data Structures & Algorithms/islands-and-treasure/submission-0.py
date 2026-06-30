class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m= len(grid)
        n= len(grid[0])
        directions= [[0,1], [0, -1], [1, 0], [-1, 0]]
        def valid(row, col):

            return row<0 or row>=m or col<0 or col>=n or grid[row][col]== -1
            

        def dfs(row, col, curr):

            if valid(row, col) or grid[row][col]<curr:
                return

            grid[row][col]= curr

            for dx, dy in directions:
                curr_row, curr_col = row+dx, col+dy
                dfs(curr_row, curr_col, curr+1)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    dfs(i, j, 0)
